import csv
import os

csvpath = os.path.join('budget_data.csv')
totalMonth = 0
totalNet = 0
average = 0
maxNum = 0
minNum = 0

with open (csvpath,newline='') as csvfile:
   
   csvreader = csv.reader(csvfile,delimiter=',')

   print(csvreader)

   csv_header = next(csvreader)
   print(f"Csv header: {csv_header}")
       
   for row in csvreader:
       totalMonth= totalMonth+1
       totalNet += float(row[1])
       average = round(totalNet / totalMonth,2)
       maxNum = max(maxNum,float(row[1]))
       minNum = min(minNum,float(row[1]))

       



       


print(f'Financial Analysis')
print(f'___________________________')
print(f'Total Months: {totalMonth}')
print(f'net total: ${totalNet}')
print(f'average: ${average}')
print(f'Greatest Increase in Profits: {month} ${maxNum}')
print(f'Greatest Decrease in Profits: ${minNum}')
   


