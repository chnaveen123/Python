import csv
from prettytable import PrettyTable

with open("Employee.csv", "r") as CSVR:
    emp_details = csv.reader(CSVR)

    """colName = next(emp_details)
    print(colName)"""

    emp_table = PrettyTable(next( emp_details))

    for rec in emp_details:

        emp_table.add_row(rec)

CSVR.close()

print(emp_table)