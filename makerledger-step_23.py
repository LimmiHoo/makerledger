# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: MakerLedger
def tag_add(item, key, value):
    if key not in item.get('tags', {}):
        item.setdefault('tags', {})
        item['tags'][key] = []
    if isinstance(value, str) and value not in item['tags'][key]:
        item['tags'][key].append(value)

def tag_remove(item, key, value):
    tags = item.get('tags') or {}
    if key in tags:
        t = tags[key]
        if value in t:
            t.remove(value)

def tag_summary(records):
    summary = {}
    for r in records:
        for k, vlist in (r.get('tags') or {}).items():
            for v in vlist:
                key = f"{k}:{v}"
                summary[key] = summary.get(key, 0) + 1
    return summary
