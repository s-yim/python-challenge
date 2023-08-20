#!/usr/bin/env python
# coding: utf-8

# In[60]:


#Read in csv
import os
import csv

#Load File
budget_import = os.path.join(".", "Resources", "budget_data.csv")

months = []
total = []
changes = []  

with open(budget_import, encoding="utf") as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=",")
   
#Header Row
    budget_header = next(budget_reader)
    #print(f"Header: {budget_header}")
    
#Total Months
    for col in budget_reader:
        months.append(col[0])
#Total
        total.append(int(col[1]))
#Average Change
    for row in range(len(total) - 1):
        changes.append(int(total[row + 1]) - int(total[row]))
    average = round((sum(changes) / (len(months) - 1)), 2)    
#Greatest Increase
    increase = max(changes)
    i = changes.index(increase)
#Greatest Decrease
    decrease = min(changes)
    j = changes.index(decrease)
      
#Analysis
    print("Financial Analysis")
    print()
    print("----------------------------")
    print()
    print(f"Total Months: {len(months)}")
    print(f"Total: ${sum(total)}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {months[i + 1]} (${increase})")
    print(f"Greatest Decrease in Profits: {months[j + 1]} (${decrease})")

#Export File
budget_export = os.path.join(".", "analysis", "pybank_analysis.txt")

with open(budget_export, "w") as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"Total Months: {len(months)}\n")
    txtfile.write(f"Total: ${sum(total)}\n")
    txtfile.write(f"Average Change: ${average}\n")
    txtfile.write(f"Greatest Increase in Profits: {months[i + 1]} (${increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {months[j + 1]} (${decrease})")


# In[ ]:




