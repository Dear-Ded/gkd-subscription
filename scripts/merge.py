#!/usr/bin/env python3
"""清净 · GKD 精选订阅合并脚本（多源版）。

合并优先级（高 → 低）：自有层 custom.json5 > 底座 > 各增量源（按 SOURCES 顺序）。
合并粒度为 app / group：同 app 同名 group 以高优先级层为准；低层独有的 app、group
补入并重排 key；globalGroups 同名只保留高层一份。categories 取底座的。
自有层：同名 group 整体替换；disable 列表可将任意 group 置 enable:false；
globalGroups 同名替换、新名追加。
内容哈希未变化时不升版本（--bump 时内容变化才 version+1）。
无 state.json 时，从已发布的 dist 回读版本号与内容哈希，避免误把版本打回 1。

guard=True 的来源只补缺口，不改写已有规则，并丢掉易误触的组：
  选择器已被更高优先级规则完整覆盖、空选择器、信息流滑动、action=back、
  支付/登录/删除/签到领取/打开通知，以及过宽的开屏「跳过」。
skip_globals=True 时不并入该来源的全局组（过宽全局改由自有层手工收紧后补入）。

来源清单（SOURCES，顺序即优先级，底座在最前）：
  aisouler      AIsouler 最终版 v406，精选底座（已停更）
                https://github.com/AIsouler/GKD_subscription
  linarm        Lin-arm，每日更新的主增量
                https://github.com/Lin-arm/GKD_subscription
  aoguai        奥怪的GKD订阅（id 86，GPL-3.0，全局规则见长）
                https://github.com/aoguai/subscription
  ganlinte      甘霖的GKD订阅（id 233，MIT，仍在维护）
                https://github.com/ganlinte/GKD-subscription
  mengnian      梦念逍遥のGKD订阅（id 1，仍在维护）
                https://github.com/MengNianxiaoyao/gkd-subscription
  mrlc          Mrlc的GKD订阅（id 2，仍在维护）
                https://github.com/mrlctate/gkd-mrlc
  adpro         AdproのGKD订阅（id 825，2025-02 停更，精选存量大）
                https://github.com/Adpro-Team/GKD_subscription
  jiuqianyuan   九千院的GKD订阅（id 717，2025-07 停更，覆盖面广）
                https://github.com/jiuqianyuan/GKD_subscription
  akun777       少年阿鲲的GKD订阅（id 777，少数应用深度规则）
                https://github.com/Lin-arm/gkd-Rules
  muqi          言木七的附加订阅（id 808，GPL-3.0，仍在维护）
                https://github.com/yanmuq/muqi_gkd
  aisouler404   AIsouler 停更后的自用续订（id 404，快照齐全）
                https://github.com/AIsouler/gkd-subscription
  ling          Ling 自用规则（偏细分，快照齐全；滑动类被守卫丢掉）
                https://github.com/cjy0812/Ling033_GKD_Rules
  lemon         GK-Lemon-D，作为 id667 的补充
                https://github.com/LenorEric/GK-Lemon-D
  volcano       火山虾的GKD订阅（id 557）
                https://github.com/VolcanoSAhrimp/gkd-rule
  yachengmu     YaChengMu 精简续更（id 303）
                https://github.com/YaChengMu/gkd_subscription_min
每个来源的 url 为其 dist 文件直链。快照默认缓存在 sources/，不入库。
"""
import argparse
import copy
import hashlib
import json
import re
import urllib.request
from pathlib import Path

import json5

ROOT = Path(__file__).resolve().parent.parent
SUB_ID = 2026
SUB_NAME = '清净 · GKD 精选订阅'
AUTHOR = 'Dear-Ded'
RAW_BASE = 'https://raw.githubusercontent.com/Dear-Ded/gkd-subscription/main/dist'
UPDATE_URL = f'{RAW_BASE}/gkd.json5'
CHECK_URL = f'{RAW_BASE}/gkd.version.json5'
SUPPORT_URI = 'https://github.com/Dear-Ded/gkd-subscription'

# 名称里出现这些片段的规则组直接丢弃（支付、登录、删除、签到领取、滑动倍速等）。
HARD_DENY = (
    '倍速', '乘车码', 'debug', '无响应', '永久删除', '自动删除', '指纹', '直接支付',
    '马上抢', '自动打卡', '自动登录', '自动授权', '自动允许', '一键已读', '重新检索',
    '免费畅听', '返回商家', '收付款', '自动领红包', '打开链接', 'ADB', '进入应用升级',
    '清空回收站', '看视频领取', '自动抽奖', '刷点券', '开心收下', '卡卡领取', '跳转微信',
    '领福利', '点击抽奖', '无线电', '好物沉浸', '自动签到', '立即抽奖', '确认登录',
    '自动打开', '免费领取', '迷你播放器', '防诈骗', '免密支付',
)
# 点击目标是「去打开通知」而不是关掉授权弹窗。
BAD_CLICK = re.compile(
    r'text(?:\*|~|\^|\$)?="[^"]*(?:打开通知|开启通知|允许通知|立即开启|去开启)[^"]*"'
)
DANGER_SEL = re.compile(r'直接支付|永久删除|指纹登录|马上抢|立即抽奖|看视频领取|确认登录电脑端')
BROAD_SPLASH = re.compile(r'跳过|skip', re.I)

# 顺序即优先级：第一个为底座（提供 categories），其余为增量源，依次并入。
# guard 源排在最后，只填已有十源没有的组。
SOURCES = [
    {'key': 'aisouler', 'file': 'sources/aisouler-gkd.json5',
     'repo': 'https://github.com/AIsouler/GKD_subscription',
     'url': 'https://raw.githubusercontent.com/AIsouler/GKD_subscription/main/dist/AIsouler_gkd.json5'},
    {'key': 'linarm', 'file': 'sources/lin-arm-gkd.json5',
     'repo': 'https://github.com/Lin-arm/GKD_subscription',
     'url': 'https://raw.githubusercontent.com/Lin-arm/GKD_subscription/main/dist/gkd.json5'},
    {'key': 'aoguai', 'file': 'sources/aoguai-gkd.json5',
     'repo': 'https://github.com/aoguai/subscription',
     'url': 'https://raw.githubusercontent.com/aoguai/subscription/custom/dist/aoguai_gkd.json5'},
    {'key': 'ganlinte', 'file': 'sources/ganlinte-gkd.json5',
     'repo': 'https://github.com/ganlinte/GKD-subscription',
     'url': 'https://raw.githubusercontent.com/ganlinte/GKD-subscription/main/dist/ganlin_gkd.json5'},
    {'key': 'mengnian', 'file': 'sources/mengnian-gkd.json5',
     'repo': 'https://github.com/MengNianxiaoyao/gkd-subscription',
     'url': 'https://raw.githubusercontent.com/MengNianxiaoyao/gkd-subscription/main/dist/gkd.json5'},
    {'key': 'mrlc', 'file': 'sources/mrlc-gkd.json5',
     'repo': 'https://github.com/mrlctate/gkd-mrlc',
     'url': 'https://raw.githubusercontent.com/mrlctate/gkd-mrlc/main/dist/gkd.json5'},
    {'key': 'adpro', 'file': 'sources/adpro-gkd.json5',
     'repo': 'https://github.com/Adpro-Team/GKD_subscription',
     'url': 'https://raw.githubusercontent.com/Adpro-Team/GKD_subscription/main/dist/Adpro_gkd.json5'},
    {'key': 'jiuqianyuan', 'file': 'sources/jiuqianyuan-gkd.json5',
     'repo': 'https://github.com/jiuqianyuan/GKD_subscription',
     'url': 'https://raw.githubusercontent.com/jiuqianyuan/GKD_subscription/main/dist/gkd.json5'},
    {'key': 'akun777', 'file': 'sources/linarm-rules-gkd.json5',
     'repo': 'https://github.com/Lin-arm/gkd-Rules',
     'url': 'https://raw.githubusercontent.com/Lin-arm/gkd-Rules/main/dist/gkd.json5'},
    {'key': 'muqi', 'file': 'sources/muqi-gkd.json5',
     'repo': 'https://github.com/yanmuq/muqi_gkd',
     'url': 'https://raw.githubusercontent.com/yanmuq/muqi_gkd/main/dist/gkd.json5'},
    {'key': 'aisouler404', 'file': 'sources/aisouler404-gkd.json5',
     'repo': 'https://github.com/AIsouler/gkd-subscription',
     'url': 'https://raw.githubusercontent.com/AIsouler/gkd-subscription/main/dist/gkd.json5',
     'guard': True, 'skip_globals': True},
    {'key': 'ling', 'file': 'sources/ling-gkd.json5',
     'repo': 'https://github.com/cjy0812/Ling033_GKD_Rules',
     'url': 'https://raw.githubusercontent.com/cjy0812/Ling033_GKD_Rules/main/dist/gkd.json5',
     'guard': True, 'skip_globals': True},
    {'key': 'lemon', 'file': 'sources/lemon-gkd.json5',
     'repo': 'https://github.com/LenorEric/GK-Lemon-D',
     'url': 'https://raw.githubusercontent.com/LenorEric/GK-Lemon-D/main/dist/GK-LEMON-D.json5',
     'guard': True, 'skip_globals': True,
     'deny_extra': ('getPrev',)},
    {'key': 'volcano', 'file': 'sources/volcano-gkd.json5',
     'repo': 'https://github.com/VolcanoSAhrimp/gkd-rule',
     'url': 'https://raw.githubusercontent.com/VolcanoSAhrimp/gkd-rule/main/dist/gkd.json5',
     'guard': True, 'skip_globals': True},
    {'key': 'yachengmu', 'file': 'sources/yachengmu-gkd.json5',
     'repo': 'https://github.com/YaChengMu/gkd_subscription_min',
     'url': 'https://raw.githubusercontent.com/YaChengMu/gkd_subscription_min/main/dist/gkd.json5',
     'guard': True, 'skip_globals': True},
]


def load_json5(path):
    with open(path, encoding='utf-8') as f:
        return json5.load(f)


def next_key(groups):
    keys = [g.get('key', -1) for g in groups if isinstance(g.get('key', -1), int)]
    return (max(keys) + 1) if keys else 0


def iter_rules(g):
    rules = g.get('rules', [])
    if isinstance(rules, (str, dict)):
        return [rules]
    if isinstance(rules, list):
        return rules
    return []


def n_rules(g):
    rules = g.get('rules', [])
    if isinstance(rules, list):
        return len(rules)
    return 1 if rules else 0


def sel_strings(rule):
    out = set()
    if isinstance(rule, str):
        text = rule.strip()
        if text:
            out.add(text)
        return out
    if not isinstance(rule, dict):
        return out
    for key in ('matches', 'anyMatches'):
        value = rule.get(key)
        if isinstance(value, str) and value.strip():
            out.add(value.strip())
        elif isinstance(value, list):
            out.update(item.strip() for item in value if isinstance(item, str) and item.strip())
    return out


def group_sels(g):
    sels = set()
    for rule in iter_rules(g):
        sels |= sel_strings(rule)
    return sels


def click_selectors(g):
    """会被点到的选择器：matches 数组取最后一项（GKD 点击最后一项）。"""
    out = []
    for rule in iter_rules(g):
        if isinstance(rule, str):
            out.append(rule)
            continue
        if not isinstance(rule, dict):
            continue
        matches = rule.get('matches')
        if isinstance(matches, list) and matches:
            last = matches[-1]
            if isinstance(last, str):
                out.append(last)
        elif isinstance(matches, str):
            out.append(matches)
        elif not matches:
            any_matches = rule.get('anyMatches')
            if isinstance(any_matches, str):
                out.append(any_matches)
            elif isinstance(any_matches, list):
                out.extend(item for item in any_matches if isinstance(item, str))
    return out


def risky_action(g):
    if g.get('swipeArg') or g.get('action') in ('swipe', 'back'):
        return g.get('action') or 'swipe'
    for rule in iter_rules(g):
        if not isinstance(rule, dict):
            continue
        if rule.get('swipeArg') or rule.get('action') == 'swipe':
            return 'swipe'
        if rule.get('action') == 'back':
            return 'back'
    return None


def broad_splash(name, sels):
    if '开屏' not in (name or ''):
        return False
    for sel in sels:
        if not BROAD_SPLASH.search(sel):
            continue
        if not any(token in sel for token in ('length', 'width', 'vid=', 'id=', 'desc=')):
            return True
    return False


def broad_webview_image(sels):
    for sel in sels:
        if 'Image[text=""]' in sel and not re.search(r'close|关闭|跳过|取消|不感兴趣', sel, re.I):
            return True
    return False


def guard_reason(g, aid, known_sels, opt):
    """返回丢弃原因；None 表示可以并入。仅 guard 源调用。"""
    name = g.get('name') or ''
    sels = group_sels(g)
    blob = name + '\n' + '\n'.join(sels)
    if any(token in name for token in HARD_DENY):
        return 'deny-name'
    if any(token in blob for token in opt.get('deny_extra') or ()):
        return 'deny-extra'
    if name.startswith('功能类') and ('关闭' not in name and '弹窗' not in name):
        return 'functional'
    if risky_action(g):
        return 'gesture'
    if DANGER_SEL.search('\n'.join(sels)) and not any(token in name for token in ('关闭', '跳过', '取消', '弹窗')):
        return 'danger-selector'
    if any(BAD_CLICK.search(sel) for sel in click_selectors(g)):
        return 'opens-permission'
    if not sels:
        return 'empty'
    if aid in known_sels and sels <= known_sels[aid]:
        return 'duplicate-selector'
    if broad_splash(name, sels):
        return 'broad-splash'
    if broad_webview_image(sels):
        return 'broad-image'
    return None


def remember_sels(known_sels, aid, groups):
    bucket = known_sels.setdefault(aid, set())
    for group in groups:
        bucket |= group_sels(group)


def merge_layer(merged, order, src_apps, st, known_sels, opt):
    """把一个来源的 apps 并入已合并集合（merged: id->app, order: id 顺序）。

    新 app 整体补入；已有 app 中同名 group 以先到（高优先级）层为准，
    独有 group 追加并重排 key。guard 源再经 guard_reason 过滤。
    """
    guard = bool(opt.get('guard'))
    for app in src_apps:
        aid = app['id']
        groups = app.get('groups') or []
        if guard:
            kept = []
            for group in groups:
                reason = guard_reason(group, aid, known_sels, opt)
                if reason:
                    st['groups_skipped'] += 1
                    st['skip_reasons'][reason] = st['skip_reasons'].get(reason, 0) + 1
                    continue
                kept.append(group)
            groups = kept
        if aid not in merged:
            if guard and not groups:
                st['apps_skipped_empty'] += 1
                continue
            app2 = copy.deepcopy(app)
            if guard:
                app2['groups'] = copy.deepcopy(groups)
            merged[aid] = app2
            order.append(aid)
            st['apps_added'] += 1
            st['groups_added'] += len(app2.get('groups') or [])
            st['rules_added'] += sum(n_rules(g) for g in app2.get('groups') or [])
            remember_sels(known_sels, aid, app2.get('groups') or [])
            continue
        target = merged[aid]
        target.setdefault('groups', [])
        names = {g.get('name') for g in target['groups']}
        for group in groups:
            if group.get('name') in names:
                st['groups_shadowed'] += 1
                continue
            group2 = copy.deepcopy(group)
            group2['key'] = next_key(target['groups'])
            target['groups'].append(group2)
            names.add(group2.get('name'))
            st['groups_added'] += 1
            st['rules_added'] += n_rules(group2)
            remember_sels(known_sels, aid, [group2])
    return merged, order


def merge_global_layer(out, src_globals, st):
    names = {g.get('name') for g in out}
    for group in src_globals:
        if group.get('name') in names:
            st['globals_shadowed'] += 1
            continue
        group2 = copy.deepcopy(group)
        group2['key'] = next_key(out)
        out.append(group2)
        names.add(group2.get('name'))
        st['globals_added'] += 1
    return out


def apply_custom(apps, custom, stats):
    by_id = {a['id']: a for a in apps}
    for capp in custom.get('apps', []):
        aid = capp['id']
        if aid not in by_id:
            apps.append(copy.deepcopy(capp))
            by_id[aid] = apps[-1]
            stats['apps_from_custom'] += 1
            continue
        target = by_id[aid]
        names = {g.get('name'): g for g in target.get('groups', [])}
        for group in capp.get('groups', []):
            if group.get('name') in names:
                keep_key = names[group['name']].get('key')
                idx = target['groups'].index(names[group['name']])
                group2 = copy.deepcopy(group)
                group2['key'] = keep_key
                target['groups'][idx] = group2
                stats['groups_custom_replaced'] += 1
            else:
                group2 = copy.deepcopy(group)
                group2['key'] = next_key(target['groups'])
                target['groups'].append(group2)
                stats['groups_from_custom'] += 1
    for dis in custom.get('disable', []):
        app = by_id.get(dis.get('appId'))
        if not app:
            continue
        for group in app.get('groups', []):
            if group.get('name') == dis.get('groupName'):
                group['enable'] = False
                stats['groups_disabled'] += 1
    return apps


def apply_custom_globals(global_groups, custom, stats):
    names = {g.get('name'): i for i, g in enumerate(global_groups)}
    for group in custom.get('globalGroups') or []:
        if group.get('name') in names:
            idx = names[group['name']]
            group2 = copy.deepcopy(group)
            group2['key'] = global_groups[idx].get('key')
            global_groups[idx] = group2
            stats['globals_custom_replaced'] += 1
            continue
        group2 = copy.deepcopy(group)
        group2['key'] = next_key(global_groups)
        global_groups.append(group2)
        names[group2.get('name')] = len(global_groups) - 1
        stats['globals_from_custom'] += 1
    return global_groups


def count_rules(apps):
    n_groups = 0
    n_rules = 0
    for app in apps:
        for group in app.get('groups', []):
            n_groups += 1
            n_rules += n_rules_of(group)
    return n_groups, n_rules


def n_rules_of(group):
    return n_rules(group)


def payload_hash(payload):
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, sort_keys=True).encode('utf-8')
    ).hexdigest()


def bootstrap_state(state_path, dist_dir):
    if state_path.exists():
        return json.loads(state_path.read_text(encoding='utf-8'))
    version = 0
    prev_hash = ''
    ver_file = dist_dir / 'gkd.version.json5'
    sub_file = dist_dir / 'gkd.json5'
    if ver_file.exists():
        version = json.loads(ver_file.read_text(encoding='utf-8')).get('version') or 0
    if sub_file.exists():
        old = load_json5(sub_file)
        prev = {
            'categories': old.get('categories'),
            'globalGroups': old.get('globalGroups'),
            'apps': old.get('apps'),
        }
        prev_hash = payload_hash(prev)
    return {'version': version, 'hash': prev_hash}


def ensure_source(src, force):
    path = ROOT / src['file']
    if path.exists() and path.stat().st_size > 100 and not force:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(src['url'], headers={'User-Agent': 'qingjing-gkd-merge'})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = resp.read()
    except Exception as exc:
        raise SystemExit(f"fetch failed: {src['key']} {src['url']} ({exc})") from exc
    if len(data) < 100:
        raise SystemExit(f"fetch too small: {src['key']} ({len(data)} bytes)")
    path.write_bytes(data)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bump', action='store_true', help='内容变化时版本 +1')
    ap.add_argument('--fetch', action='store_true', help='重新拉取全部上游快照')
    args = ap.parse_args()

    for src in SOURCES:
        ensure_source(src, args.fetch)

    loaded = []  # (source_config, parsed_subscription)
    for src in SOURCES:
        path = ROOT / src['file']
        if not path.exists():
            raise SystemExit(f"source file missing: {src['file']} (key={src['key']})")
        loaded.append((src, load_json5(path)))

    custom_path = ROOT / 'custom.json5'
    custom = load_json5(custom_path) if custom_path.exists() else {'apps': [], 'disable': []}
    dist = ROOT / 'dist'
    state_path = ROOT / 'state.json'
    state = bootstrap_state(state_path, dist)

    per_source = {}
    merged = {}
    order = []
    global_groups = []
    categories = []
    known_sels = {}
    for i, (src, data) in enumerate(loaded):
        st = {'apps_added': 0, 'groups_added': 0, 'groups_shadowed': 0,
              'rules_added': 0, 'groups_skipped': 0, 'apps_skipped_empty': 0,
              'globals_added': 0, 'globals_shadowed': 0, 'globals_skipped': 0,
              'skip_reasons': {}, 'src_version': data.get('version')}
        if i == 0:  # 底座：初始化集合、categories、globalGroups
            for app in data.get('apps', []):
                if app['id'] not in merged:
                    merged[app['id']] = copy.deepcopy(app)
                    order.append(app['id'])
                    st['apps_added'] += 1
                    st['groups_added'] += len(app.get('groups') or [])
                    st['rules_added'] += sum(n_rules(g) for g in app.get('groups') or [])
                    remember_sels(known_sels, app['id'], app.get('groups') or [])
            global_groups = copy.deepcopy(data.get('globalGroups', []))
            st['globals_added'] = len(global_groups)
            categories = copy.deepcopy(data.get('categories', []))
        else:
            merged, order = merge_layer(
                merged, order, data.get('apps', []), st, known_sels, src)
            if src.get('skip_globals'):
                st['globals_skipped'] = len(data.get('globalGroups') or [])
            else:
                global_groups = merge_global_layer(global_groups, data.get('globalGroups', []), st)
        per_source[src['key']] = st

    apps = [merged[aid] for aid in order]
    custom_stats = {'apps_from_custom': 0, 'groups_from_custom': 0,
                    'groups_custom_replaced': 0, 'groups_disabled': 0,
                    'globals_from_custom': 0, 'globals_custom_replaced': 0}
    apps = apply_custom(apps, custom, custom_stats)
    global_groups = apply_custom_globals(global_groups, custom, custom_stats)
    apps.sort(key=lambda a: a['id'])

    payload = {'categories': categories, 'globalGroups': global_groups, 'apps': apps}
    digest = payload_hash(payload)
    changed = digest != state.get('hash')
    version = state.get('version', 0)
    if version == 0:
        version = 1
    elif changed and args.bump:
        version += 1

    sub = {
        'id': SUB_ID,
        'name': SUB_NAME,
        'version': version,
        'author': AUTHOR,
        'updateUrl': UPDATE_URL,
        'checkUpdateUrl': CHECK_URL,
        'supportUri': SUPPORT_URI,
        'categories': categories,
        'globalGroups': global_groups,
        'apps': apps,
    }
    dist.mkdir(exist_ok=True)
    out_text = json.dumps(sub, ensure_ascii=False, separators=(',', ':'))
    (dist / 'gkd.json5').write_text(out_text, encoding='utf-8')
    (dist / 'gkd.version.json5').write_text(
        json.dumps({'id': SUB_ID, 'version': version}, ensure_ascii=False), encoding='utf-8')

    # 校验：回读解析、重复 id、组 key 唯一、组名唯一、全局组 key/名唯一
    chk = json5.load(open(dist / 'gkd.json5', encoding='utf-8'))
    ids = [a['id'] for a in chk['apps']]
    assert len(ids) == len(set(ids)), 'duplicate app ids!'
    for app in chk['apps']:
        keys = [g.get('key') for g in app.get('groups', [])]
        assert len(keys) == len(set(keys)), f'group key dup in {app["id"]}'
        gnames = [g.get('name') for g in app.get('groups', [])]
        assert len(gnames) == len(set(gnames)), f'group name dup in {app["id"]}'
    gkeys = [g.get('key') for g in chk.get('globalGroups', [])]
    assert len(gkeys) == len(set(gkeys)), 'global group key dup!'
    ggnames = [g.get('name') for g in chk.get('globalGroups', [])]
    assert len(ggnames) == len(set(ggnames)), 'global group name dup!'
    assert chk.get('id') == SUB_ID and isinstance(chk.get('version'), int)
    n_groups, rules = count_rules(chk['apps'])
    state.update({'version': version, 'hash': digest,
                  'baseVersion': loaded[0][1].get('version'),
                  'incrVersion': loaded[1][1].get('version'),
                  'sources': {src['key']: data.get('version') for src, data in loaded}})
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding='utf-8')
    print(json.dumps({'version': version, 'changed': changed, 'apps': len(ids),
                      'groups': n_groups, 'rules': rules,
                      'globalGroups': len(chk.get('globalGroups', [])),
                      'bytes': len(out_text.encode('utf-8')),
                      'per_source': per_source, 'custom': custom_stats},
                     ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
