from datetime import datetime

# 1. Write a program to display a person's name, age and address in three different lines.
name = input("enter your name : ")
age = int(input("enter your age : "))
address = input("enter your address : ")
print(f"name: {name}\nage: {age}\naddress: {address}")

# 2. Write a program to swap two variables.
num1 = int(input("enter number 1 : "))
num2 = int(input("enter number 2 : "))
print(f"before swapping num1 = {num1} and num2 = {num2}")
num1, num2 = num2, num1
print(f"after swapping num1 = {num1} and num2 = {num2}")

# 3. Write a program to convert a float into integer.
salary = float(input("enter the salary of your's : "))
print(f"type of salary is : {type(salary)}")
salary = int(salary)
print(f"your salary is {salary}")
print(f"type of salary after conversion {type(salary)}")

# 4. Write a program to take details from a student for ID-card and then print it in different lines.
std_sn = int(input("enter your roll number : "))
std_name = input("enter your name : ")
std_dob = input("enter your dob in formate dd-mm-yyyy : ")
std_dob_date, std_dob_month, std_dob_year = map(int, std_dob.split("-"))
current_date = datetime.now()
dob = datetime(std_dob_year, std_dob_month, std_dob_date)
age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))
print(f"Roll Number: {std_sn} \nName: {std_name} \nDOB: {std_dob} \nAge: {age} ")







