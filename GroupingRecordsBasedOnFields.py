from collections import defaultdict
from itertools import groupby
from operator import itemgetter

rows=[
    {'address': '5412 N Clark', 'date': '07/01/2015'},
    {'address': '5413 N Clark', 'date': '07/01/2015'},
    {'address': '5409 N Clark', 'date': '07/02/2015'},
    {'address': '5309 N Clark', 'date': '07/03/2015'},
    {'address': '5419 N Clark', 'date': '07/03/2015'}
]
rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key =itemgetter('date')):
    print(date)
    for i in items:
        print(i)

print('============')

rows_by_date = defaultdict(list)

for row in rows:
    rows_by_date[row['date']].append(row)
    print(rows_by_date)
for r in rows_by_date['07/01/2015']:
    print(r)