import csv
import os

csvpath = os.path.join('budget_data.csv')
totalMonth = 0

with open (csvpath,newline='') as csvfile:
   
   csvreader = csv.reader(csvfile,delimiter=' ')

   print(csvreader)

   csv_header = next(csvreader)
   print(f"Csv header: {csv_header}")

   for row in csvreader:
       totalMonth= totalMonth+1

print(f'Financial Analysis')
print(f'___________________________')
print(f'Total Months: {totalMonth}')
   


