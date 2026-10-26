#!/usr/bin/env python3
"""清净 · GKD 精选订阅合并脚本（多源版）。

合并优先级（高 → 低）：自有层 custom.json5 > 底座 > 各增量源（按 SOURCES 顺序）。
合并粒度为 app / group：同 app 同名 group 以高优先级层为准；低层独有的 app、group
补入并重排 key；globalGroups 同名只保留高层一份。categories 取底座的。
自有层：同名 group 整体替换；disable 列表可将任意 group 置 enable:false。
内容哈希未变化时不升版本（--bump 时内容变化才 version+1）。

来源清单（SOURCES，顺序即优先级，底座在最前）：
  aisouler     AIsouler 最终版 v406，精选底座（已停更）
               https://github.com/AIsouler/GKD_subscription
  linarm       Lin-arm，每日更新的主增量
               https://github.com/Lin-arm/GKD_subscription
  aoguai       奥怪的GKD订阅（id 86，仍在维护，全局规则见长）
               https://github.com/aoguai/subscription
  ganlinte     甘霖的GKD订阅（id 233，仍在维护，覆盖面最大）
               https://github.com/ganlinte/GKD-subscription
  mengnian     梦念逍遥のGKD订阅（id 1，仍在维护）
               https://github.com/MengNianxiaoyao/gkd-subscription
  mrlc         Mrlc的GKD订阅（id 2，仍在维护）
               https://github.com/mrlctate/gkd-mrlc
  adpro        AdproのGKD订阅（id 825，2025-02 停更，精选存量大）
               https://github.com/Adpro-Team/GKD_subscription
  jiuqianyuan  九千院的GKD订阅（id 717，2025-07 停更，覆盖面广）
               https://github.com/jiuqianyuan/GKD_subscription
  akun777      少年阿鲲的GKD订阅（id 777，Lin-arm/gkd-Rules 发布，少数应用深度规则）
               https://github.com/Lin-arm/gkd-Rules
  muqi         言木七的附加订阅（id 808，附加型订阅，仍在维护）
               https://github.com/yanmuq/muqi_gkd
每个来源的 url 为其 dist 文件直链，便于日后刷新 sources/ 快照。
"""
import argparse, copy, hashlib, json
from pathlib import Path

import json5

ROOT = Path(__file__).resolve().parent
SUB_ID = 2026
SUB_NAME = '清净 · GKD 精选订阅'
AUTHOR = 'Dear-Ded'
RAW_BASE = 'https://raw.githubusercontent.com/Dear-Ded/gkd-subscription/main/dist'
UPDATE_URL = f'{RAW_BASE}/gkd.json5'
CHECK_URL = f'{RAW_BASE}/gkd.version.json5'
SUPPORT_URI = 'https://github.com/Dear-Ded/gkd-subscription'

# 顺序即优先级：第一个为底座（提供 categories），其余为增量源，依次并入。
SOURCES = [
    {'key': 'aisouler', 'file': 'aisouler-gkd.json5',
     'repo': 'https://github.com/AIsouler/GKD_subscription',
     'url': 'https://raw.githubusercontent.com/AIsouler/GKD_subscription/main/dist/AIsouler_gkd.json5'},
    {'key': 'linarm', 'file': 'lin-arm-gkd.json5',
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
]


def load_json5(path):
    with open(path, encoding='utf-8') as f:
        return json5.load(f)


def next_key(groups):
    keys = [g.get('key', -1) for g in groups if isinstance(g.get('key', -1), int)]
    return (max(keys) + 1) if keys else 0


def merge_layer(merged, order, src_apps, st):
    """把一个来源的 apps 并入已合并集合（merged: id->app, order: id 顺序）。

    新 app 整体补入；已有 app 中同名 group 以先到（高优先级）层为准，
    独有 group 追加并重排 key。
    """
    for app in src_apps:
        aid = app['id']
        if aid not in merged:
            merged[aid] = copy.deepcopy(app)
            order.append(aid)
            st['apps_added'] += 1
            continue
        target = merged[aid]
        target.setdefault('groups', [])
        names = {g.get('name') for g in target['groups']}
        for g in app.get('groups', []):
            if g.get('name') in names:
                st['groups_shadowed'] += 1
                continue
            g2 = copy.deepcopy(g)
            g2['key'] = next_key(target['groups'])
            target['groups'].append(g2)
            names.add(g2.get('name'))
            st['groups_added'] += 1
    return merged, order


def merge_global_layer(out, src_globals, st):
    names = {g.get('name') for g in out}
    for g in src_globals:
        if g.get('name') in names:
            st['globals_shadowed'] += 1
            continue
        g2 = copy.deepcopy(g)
        g2['key'] = next_key(out)
        out.append(g2)
        names.add(g2.get('name'))
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
        for g in capp.get('groups', []):
            if g.get('name') in names:
                keep_key = names[g['name']].get('key')
                idx = target['groups'].index(names[g['name']])
                g2 = copy.deepcopy(g)
                g2['key'] = keep_key
                target['groups'][idx] = g2
                stats['groups_custom_replaced'] += 1
            else:
                g2 = copy.deepcopy(g)
                g2['key'] = next_key(target['groups'])
                target['groups'].append(g2)
                stats['groups_from_custom'] += 1
    for dis in custom.get('disable', []):
        app = by_id.get(dis.get('appId'))
        if not app:
            continue
        for g in app.get('groups', []):
            if g.get('name') == dis.get('groupName'):
                g['enable'] = False
                stats['groups_disabled'] += 1
    return apps


def count_rules(apps):
    n_groups = 0
    n_rules = 0
    for a in apps:
        for g in a.get('groups', []):
            n_groups += 1
            r = g.get('rules', [])
            n_rules += len(r) if isinstance(r, list) else 1
    return n_groups, n_rules


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bump', action='store_true', help='内容变化时版本 +1')
    args = ap.parse_args()

    loaded = []  # (source_config, parsed_subscription)
    for src in SOURCES:
        path = ROOT / src['file']
        if not path.exists():
            raise SystemExit(f"source file missing: {src['file']} (key={src['key']})")
        loaded.append((src, load_json5(path)))

    custom_path = ROOT / 'custom.json5'
    custom = load_json5(custom_path) if custom_path.exists() else {'apps': [], 'disable': []}
    state_path = ROOT / 'state.json'
    state = json.loads(state_path.read_text(encoding='utf-8')) if state_path.exists() else {'version': 0, 'hash': ''}

    per_source = {}
    merged = {}
    order = []
    global_groups = []
    categories = []
    for i, (src, data) in enumerate(loaded):
        st = {'apps_added': 0, 'groups_added': 0, 'groups_shadowed': 0,
              'globals_added': 0, 'globals_shadowed': 0,
              'src_version': data.get('version')}
        if i == 0:  # 底座：初始化集合、categories、globalGroups
            for app in data.get('apps', []):
                if app['id'] not in merged:
                    merged[app['id']] = copy.deepcopy(app)
                    order.append(app['id'])
                    st['apps_added'] += 1
            global_groups = copy.deepcopy(data.get('globalGroups', []))
            st['globals_added'] = len(global_groups)
            categories = copy.deepcopy(data.get('categories', []))
        else:
            merged, order = merge_layer(merged, order, data.get('apps', []), st)
            global_groups = merge_global_layer(global_groups, data.get('globalGroups', []), st)
        per_source[src['key']] = st

    apps = [merged[aid] for aid in order]
    custom_stats = {'apps_from_custom': 0, 'groups_from_custom': 0,
                    'groups_custom_replaced': 0, 'groups_disabled': 0}
    apps = apply_custom(apps, custom, custom_stats)
    apps.sort(key=lambda a: a['id'])

    payload = {'categories': categories, 'globalGroups': global_groups, 'apps': apps}
    digest = hashlib.sha256(json.dumps(payload, ensure_ascii=False, sort_keys=True).encode('utf-8')).hexdigest()
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
    dist = ROOT / 'dist'
    dist.mkdir(exist_ok=True)
    out_text = json.dumps(sub, ensure_ascii=False, separators=(',', ':'))
    (dist / 'gkd.json5').write_text(out_text, encoding='utf-8')
    (dist / 'gkd.version.json5').write_text(json.dumps({'id': SUB_ID, 'version': version}), encoding='utf-8')

    # 校验：回读解析、重复 id、组 key 唯一
    chk = json5.load(open(dist / 'gkd.json5', encoding='utf-8'))
    ids = [a['id'] for a in chk['apps']]
    assert len(ids) == len(set(ids)), 'duplicate app ids!'
    for a in chk['apps']:
        ks = [g.get('key') for g in a.get('groups', [])]
        assert len(ks) == len(set(ks)), f'group key dup in {a["id"]}'
    gks = [g.get('key') for g in chk.get('globalGroups', [])]
    assert len(gks) == len(set(gks)), 'global group key dup!'
    n_groups, n_rules = count_rules(chk['apps'])
    state.update({'version': version, 'hash': digest,
                  'baseVersion': loaded[0][1].get('version'),
                  'incrVersion': loaded[1][1].get('version'),
                  'sources': {src['key']: data.get('version') for src, data in loaded}})
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding='utf-8')
    print(json.dumps({'version': version, 'changed': changed, 'apps': len(ids),
                      'groups': n_groups, 'rules': n_rules,
                      'globalGroups': len(chk.get('globalGroups', [])),
                      'bytes': len(out_text.encode('utf-8')),
                      'per_source': per_source, 'custom': custom_stats},
                     ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
