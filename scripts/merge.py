#!/usr/bin/env python3
"""Dear-Ded 精选 GKD 订阅合并脚本。

三层合并：
  底座 AIsouler 最终版（精选，已停更） > 增量 Lin-arm（每日更新） > 自有层 custom.json5（最高优先级）
合并粒度为 app / group：同 app 同名 group 以高优先级层为准；低层独有的 app、group 补入并重排 key。
自有层：同名 group 整体替换；disable 列表可将任意 group 置 enable:false。
内容哈希未变化时不升版本。
"""
import argparse, copy, hashlib, json, sys
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


def load_json5(path):
    with open(path, encoding='utf-8') as f:
        return json5.load(f)


def next_key(groups):
    keys = [g.get('key', -1) for g in groups if isinstance(g.get('key', -1), int)]
    return (max(keys) + 1) if keys else 0


def merge_apps(base_apps, incr_apps, stats):
    merged = {}
    order = []
    for app in base_apps:
        merged[app['id']] = copy.deepcopy(app)
        order.append(app['id'])
    for app in incr_apps:
        aid = app['id']
        if aid not in merged:
            merged[aid] = copy.deepcopy(app)
            order.append(aid)
            stats['apps_from_incr'] += 1
            continue
        target = merged[aid]
        names = {g.get('name') for g in target.get('groups', [])}
        for g in app.get('groups', []):
            if g.get('name') in names:
                stats['groups_base_kept'] += 1
                continue
            g2 = copy.deepcopy(g)
            g2['key'] = next_key(target['groups'])
            target['groups'].append(g2)
            names.add(g2.get('name'))
            stats['groups_from_incr'] += 1
    return [merged[aid] for aid in order]


def merge_global(base_g, incr_g, stats):
    out = copy.deepcopy(base_g)
    names = {g.get('name') for g in out}
    for g in incr_g:
        if g.get('name') in names:
            continue
        g2 = copy.deepcopy(g)
        g2['key'] = next_key(out)
        out.append(g2)
        names.add(g2.get('name'))
        stats['global_from_incr'] += 1
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

    base = load_json5(ROOT / 'aisouler-gkd.json5')
    incr = load_json5(ROOT / 'lin-arm-gkd.json5')
    custom_path = ROOT / 'custom.json5'
    custom = load_json5(custom_path) if custom_path.exists() else {'apps': [], 'disable': []}
    state_path = ROOT / 'state.json'
    state = json.loads(state_path.read_text(encoding='utf-8')) if state_path.exists() else {'version': 0, 'hash': ''}

    stats = {'apps_from_incr': 0, 'groups_from_incr': 0, 'groups_base_kept': 0,
             'global_from_incr': 0, 'apps_from_custom': 0, 'groups_from_custom': 0,
             'groups_custom_replaced': 0, 'groups_disabled': 0}

    apps = merge_apps(base.get('apps', []), incr.get('apps', []), stats)
    apps = apply_custom(apps, custom, stats)
    apps.sort(key=lambda a: a['id'])
    global_groups = merge_global(base.get('globalGroups', []), incr.get('globalGroups', []), stats)
    categories = copy.deepcopy(base.get('categories', []))

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
    n_groups, n_rules = count_rules(chk['apps'])
    state.update({'version': version, 'hash': digest,
                  'baseVersion': base.get('version'), 'incrVersion': incr.get('version')})
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=1), encoding='utf-8')
    print(json.dumps({'version': version, 'changed': changed, 'apps': len(ids),
                      'groups': n_groups, 'rules': n_rules,
                      'bytes': len(out_text.encode('utf-8')), 'stats': stats},
                     ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
