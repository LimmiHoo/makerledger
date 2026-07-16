# === Stage 26: Add weekly summary calculations ===
# Project: MakerLedger
def weekly_summary(records, start_date):
    from datetime import timedelta
    week = {start_date.strftime('%Y-%W'): {'materials': 0, 'tasks': 0, 'costs': 0, 'experiments': 0}}
    for r in records:
        if isinstance(r, dict) and 'date' in r:
            d = r['date'] + timedelta(days=1) if not (isinstance(d, datetime.date)) else d
            week_key = d.strftime('%Y-%W')
            if week_key not in week:
                week[week_key] = {'materials': 0, 'tasks': 0, 'costs': 0, 'experiments': 0}
            if isinstance(r, dict):
                if r.get('type') == 'material' and 'quantity' in r:
                    week[week_key]['materials'] += r['quantity'] * (r.get('unit_cost', 0) or 0)
                elif r.get('type') == 'task':
                    week[week_key]['tasks'] += 1
                elif r.get('type') == 'cost' and 'amount' in r:
                    week[week_key]['costs'] += r['amount']
                elif r.get('type') == 'experiment' and 'result' in r:
                    week[week_key]['experiments'] += 1
    return week
