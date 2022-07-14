import os
root_dir = r'C:\Users\nc67322\PycharmProjects\pythonProject\samplepractice\Root'
file_list = []
for sub_dir, dirs, files in os.walk(root_dir):
    for file in files:
        file_list.append(os.path.join(sub_dir, file))
emp_list = []
stud_list = []
fruit_list = []
for file_name in file_list:
    with open(file_name,'r') as handle:
        file_data = handle.read().split('\n')[1:-1]
        if 'emp' in file_name:
            for line in file_data:
                emp_list.append(line.split(','))
        if 'stud' in file_name:
            for line in file_data:
                stud_list.append(line.split(','))
        if 'Fruit' in file_name:
            for line in file_data:
                fruit_list.append(line.split(','))
count_dat_files = len(file_list)
total_emp_count = len(emp_list)
count_male_emp = 0
count_female_emp = 0
unique_depts = set()
total_salary = 0
for employee in emp_list:
    if employee[2]=='m':
        count_male_emp += 1
    else:
        count_female_emp += 1
        unique_depts.add(employee[3])
        total_salary += int(employee[4])
total_quantity = 0
unique_fruits = set()
quantity_list = [0, 0, 0] #Apple, orange, grapes
apples_quantity = 0
oranges_quantity = 0
grapes_quantity = 0
for fruit in fruit_list:
    print(fruit[1].lower())
    total_quantity += int(fruit[3])
    unique_fruits.add(fruit[1])
    if fruit[1].lower() == 'apple':
        quantity_list[0] += int(fruit[3])
    elif fruit[1].lower() == 'orange':
        quantity_list[1] += int(fruit[3])
    elif fruit[1].lower() == 'grapes':
        quantity_list[2] += int(fruit[3])
count_male_stud = 0
count_female_stud = 0
total_stud_count = len(stud_list)
stud_pass_count = 0
stud_fail_count = 0
for student in stud_list:
    if student[2]=='m':
        count_male_stud += 1
    else:
        count_female_stud += 1
    if int(student[4][:-1])<35:
        stud_fail_count += 1
    else:
        stud_pass_count += 1
print(f'Number of male employees: {count_male_emp}')
print(f'Number of female employees: {count_female_emp}')
print(f'Number of male students: {count_male_stud}')
print(f'Number of female students: {count_female_stud}')
print(f'Quantity(in Kgs) of Apples, Oranges and Grapes: {quantity_list}')
print(f'Unique list of departments of employees: {unique_depts}')
print(f'Unique list of fruits: {unique_fruits}')
print(f'Total salaries: {total_salary}')
print(f'Count of .dat files: {count_dat_files}')
print(f'Count of passed students: {stud_pass_count}')
print(f'Count of failed students: {stud_fail_count}')
print(f'Total quantity of fruits(in Kgs): {total_quantity}')
print(f'Total count of employees: {total_emp_count}')
print(f'Total count of students: {total_stud_count}')