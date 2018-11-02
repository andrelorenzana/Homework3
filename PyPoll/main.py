import csv

def main():
    with open('election_data.csv', 'r', newline = '', encoding='utf-8') as csvfile:
        election_data = list(csv.reader(csvfile, delimiter=","))

        total_votes = 0
        candidates = {}

        for i in range(1,len(election_data)):
            total_votes = total_votes + 1

            if election_data[i][2] not in candidates.keys():
                candidates[election_data[i][2]] = 1
            else:
                candidates[election_data[i][2]] = candidates[election_data[i][2]] + 1

    results_string = """Election Results\n
-------------------------\n
Total Votes: {}\n
-------------------------\n
""".format(total_votes)

    winner = list(candidates.keys())[0]
    winner_vote_count = candidates[winner]

    for candidate in candidates.keys():
        if candidates[candidate] > winner_vote_count:
            winner = candidate
            winner_vote_count = candidates[candidate]

        vote_share = round((candidates[candidate]/total_votes)*100, 3)
        results_string = results_string + '{}: {}% ({})\n'.format(candidate, vote_share, candidates[candidate])

    results_string = results_string + """-------------------------\n
Winner: {}\n-------------------------\n""".format(winner)
    print(results_string)

    with open('election_results_output.txt', 'w', newline = '', encoding='utf-8') as output_file:
        output_file.write(results_string)


if __name__ == '__main__':
    main()
