# Import Dependenices

import csv
import os
import collections

# files to load and output
input_data ='Resources/election_data.csv'
txt_output ='Analysis/election_analysis.txt'

#Variable to count votes
total_votes = 0

#To select candidates and vote counts
candidate_choice = []
candidate_vots = {}

#Variables to determin the winning candidate and count tracker
Winning_can = ""
Winning_count = 0

# Read the csv file and convert it into a list of dictionaries
with open(input_data) as election_data:
    reader= csv.DictReader(election_data)
    
    #loop through each row
    for row in reader:

        #total vote count
        total_votes = total_votes  + 1 

        #Determine candidate name from each row
        candidate_name = row["Candidate"]

        #Build conditional statement to determine candidate vote count
        if candidate_name not in candidate_choice:

            #Add to list of candidates
            candidate_choice.append(candidate_name)

            #Track candidate's voter count
            candidate_vots[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_vots[candidate_name] = candidate_vots[candidate_name] + 1 


#print final vote count and save to txt
with open(txt_output, "w") as txt_file: 
    
    #Print final vote count
    results = (
        f'\nElection Results\n'
        f'--------------------\n'
        f'Total Votes: {total_votes}\n'
        f'-----------------------\n'
    )
    print(results)

    txt_file.write(results)

    #Determine winner by looping through counts
    for candidate in candidate_vots:

        #Retrieve the count and percentage
        votes = candidate_vots.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        #Determine winning vote count and candidate
        if (votes > Winning_count):
            Winning_count = votes
            Winning_can = candidate

        #Print candidate results and save to txt
        voter_output1 = f'{candidate}: {vote_percentage:.3f}% ({votes})\n'
        print(voter_output1)
    
        txt_file.write(voter_output1)
    

    #Print winner results
    winner_output = (
        f'-----------------\n'
        f'Winner: {Winning_can}\n'
        f'-----------------\n'
    )

    #Print winner results
    print(winner_output)

    #Save to txt file
    txt_file.write(winner_output)
