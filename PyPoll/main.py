import csv
import os

csvpath = os.path.join('Resources' , 'election_data.csv')

total_votes = 0
candidate_list = []
candidate_dict = {}

winning_vote = 0
winner = ""

with open(csvpath, newline="") as csvfile:

        csvreader = csv.reader(csvfile, delimiter=",")
        reader = csv.reader(csvfile)
        next(reader, None)

        for row in reader:
            total_votes += 1

            candidate = row[2]
            if candidate not in candidate_list:
                candidate_list.append(candidate)
                candidate_dict[candidate] = 0
            candidate_dict[candidate] +=1
output_file = 'Analysis/election_results.txt'
with open(output_file, "w" , newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    print(f"Election Results")
    print(f"--------------------")
    print(f"Total Votes: {total_votes}")
    print(f"---------------------")

    csvwriter.writerow([f"Election Results"])
    csvwriter.writerow([f"-------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow([f"--------------------"])

    for candidate in candidate_dict:
        percentage = round(float(candidate_dict[candidate])/float(total_votes),2)

        print(f"{candidate}: {percentage:.3%} ({candidate_dict[candidate]})/n")
        csvwriter.writerow([f"{candidate}: {percentage:.3%} ({candidate_dict[candidate]})/n"])

        votes = candidate_dict[candidate]
        if votes > winning_vote:
            winning_vote = votes
            winner = candidate

    print([f"---------------------"])
    print([f"Winner: {winner}"])
    print([f"-----------------------"])
    csvwriter.writerow([f"----------------------"])
    csvwriter.writerow([f"winner: {winner}"])
    csvwriter.writerow([f"-----------------------"])