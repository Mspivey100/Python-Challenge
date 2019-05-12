import csv
import os

voteCount=0
khanCount=0
correyCount=0

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



print(f'votes: {voteCount}')
print(f'Khan: {khanCount}')
print(f'Correy:{correyCount}')
   