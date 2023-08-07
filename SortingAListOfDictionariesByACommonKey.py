from operator import itemgetter

rows = [
    {'fname': 'John', 'lname': "Dow", 'uid': 1001},
    {'fname': 'Den', 'lname': "Brown", 'uid': 1002},
    {'fname': 'Ken', 'lname': "Cock", 'uid': 1003}
]

rows_by_fname = sorted(rows, key= itemgetter('fname'))
rows_by_lname = sorted(rows, key= lambda x: x['lname'])
print(rows_by_fname)
print(rows_by_lname)