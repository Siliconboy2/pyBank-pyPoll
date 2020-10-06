import csv

vote_count = 0
unfiltered_candidates = []
candidate_list = []

names = [{'name': 'Khan', 'votes': 0, 'percent':  0},
         {'name': 'Correy', 'votes': 0, 'percent': 0},
         {'name': 'Li', 'votes': 0, 'percent': 0},
         {'name': "O'Tooley", 'votes': 0, 'percent': 0}]

def total(candidate):
    if row['Candidate'] == candidate['name']:
        candidate['votes'] += 1
    candidate['percent'] = round((candidate['votes'] / vote_count) * 100, 2)

with open('/Users/northwestern/PycharmProjects/homework/PyPoll/election_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        vote_count += 1
        unfiltered_candidates.append(row['Candidate'])
        for i in names:
            total(i)
    for i in unfiltered_candidates:
        if i not in candidate_list:
            candidate_list.append(i)
print('Election Results\n-------------------------')
print(f'Total Votes: {vote_count}\n-------------------------')
for i in names:
    print(f"{i['name']}: {i['percent']}% ({i['votes']})")
winnerTuple = max([(d['votes'], d['name']) for d in names])
print(f'-------------------------\nWinner: {winnerTuple[1]}\n-------------------------')
