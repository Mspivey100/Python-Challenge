import csv
import os

voteCount=0
khanCount=0
correyCount=0
liCount=0
toolCount=0
khanPercent = 0
correyPercent = 0
liPercent = 0
toolPercent = 0

def percentCalc(votes):
    return votes / voteCount



csvpath = os.path.join('election_data.csv')
with open (csvpath,newline='') as csvfile:
   
   csvreader = csv.reader(csvfile,delimiter=',')
   csv_header = next(csvreader)
   print(f"Csv header: {csv_header}")

   for row in csvreader:
       voteCount= voteCount+1
       if row[2] == "Khan":
           khanCount = khanCount + 1
       elif row[2] == "Correy":
           correyCount = correyCount + 1
       elif row[2] == "Li":
           liCount = liCount + 1
       elif row[2] == """O'Tooley""":
           toolCount = toolCount + 1
        
       khanPercent = percentCalc(khanCount)
       correyPercent = percentCalc(correyCount)
       liPercent = percentCalc(liCount)
       toolPercent = percentCalc(toolCount)
       




print(f'votes: ({voteCount})')
print(f'Khan: {khanPercent} ({khanCount})')
print(f'Correy: {correyPercent} ({correyCount})')
print(f'Li: {liPercent} ({liCount})')
print(f"""O'tooley: {toolPercent} ({toolCount})""")
   