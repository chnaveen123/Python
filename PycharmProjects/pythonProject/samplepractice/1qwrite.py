import csv


import firstq

import csv
from prettytable import PrettyTable

with open("firstq.py", "r") as CSVR:
    emp_details = csv.reader(CSVR)



    emp_table = PrettyTable(next( emp_details))

    for rec in emp_details:

        emp_table.add_row(rec)



data = "emp_table"



with open("result.csv","w", newline="") as CSVW:
    writer = csv.writer(CSVW)


    for row in data:
        writer.writerow(row)

CSVW.close()

CSVR.close()

print(emp_table)