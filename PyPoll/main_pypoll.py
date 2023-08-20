#!/usr/bin/env python
# coding: utf-8

# In[71]:


#Read in csv
import os
import csv

#Load File
election_import = os.path.join(".", "Resources", "election_data.csv")

votes = []
candidates = []
names_list = []
winner = []

with open(election_import, encoding="utf") as csvfile:
    election_reader = csv.reader(csvfile, delimiter=",")
    
#Header Row
    election_header = next(election_reader)
    #print(f"Header: {election_header}")

#Total Votes
    for col in election_reader:
        votes.append(col[0])
        candidates.append(col[2])
    total = len(votes)
#Each candidate's total votes and percent of votes
    def names(candidates):
        for x in candidates:
            if x not in names_list:
                names_list.append(x)
    names(candidates)
    
    vote_count1 = candidates.count("Charles Casper Stockham")
    vote_count2 = candidates.count("Diana DeGette")
    vote_count3 = candidates.count("Raymon Anthony Doane")
    
    percent1 = round(vote_count1 / total * 100, 3)
    percent2 = round(vote_count2 / total * 100, 3)
    percent3 = round(vote_count3 / total * 100, 3)

#Winner
    if vote_count1 > vote_count2 and vote_count1 > vote_count3:
        winner.append(names_list[0])
    elif vote_count2 > vote_count1 and vote_count2 > vote_count3:
        winner.append(names_list[1])
    elif vote_count3 > vote_count1 and vote_count3 > vote_count2:
        winner.append(names_list[2])  

#Analysis
    print(f"Election Results")
    print()
    print(f"-------------------------")
    print()
    print(f"Total Votes: {total}")
    print()
    print(f"-------------------------")
    print()
    print(f"{names_list[0]}: {percent1}% ({vote_count1})")
    print()
    print(f"{names_list[1]}: {percent2}% ({vote_count2})")
    print()
    print(f"{names_list[2]}: {percent3}% ({vote_count3})")
    print()
    print(f"-------------------------")
    print()
    print(f"Winner: {winner[0]}")
    print()
    print(f"-------------------------")
    
#Export File)
election_export = os.path.join(".", "analysis", "pypoll_analysis.txt")

with open(election_export, "w") as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Total Votes: {total}\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"{names_list[0]}: {percent1}% ({vote_count1})\n")
    txtfile.write(f"{names_list[1]}: {percent2}% ({vote_count2})\n")
    txtfile.write(f"{names_list[2]}: {percent3}% ({vote_count3})\n")
    txtfile.write(f"-------------------------\n")
    txtfile.write(f"Winner: {winner[0]}\n")
    txtfile.write(f"-------------------------")


# In[ ]:





# In[ ]:




