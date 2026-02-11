'''Write a program to prompt users to enter their working hours 
and rate per hour to calculate gross pay. The program should 
give the employee 1.5 times the hours worked above 30 hours. If 
Enter Hours is 50 and Enter Rate is 10, then the calculated 
payment is Pay: 550.0. '''



hours = int(input("Enter Hours: "))
rate = int(input("Enter Rate: "))


if hours > 30:
    overtime_hours = hours - 30
    gross_pay = (30 * rate) + (overtime_hours * rate * 1.5)
else:
    gross_pay = hours * rate


print("Pay:", gross_pay)