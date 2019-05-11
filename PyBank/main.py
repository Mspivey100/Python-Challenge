import csv
import os

csvpath = os.path.join('budget_data.csv')

with open (csvpath,newline='') as csvfile:

   csvreader = csv.reader(csvfile,delimiter=' ')

   print(csvreader)

   csv_header = next(csvreader)
   print(f"Csv header: {csv_header}")

   for row in csvreader:
       print(row) 
