# Write a Python script to prompt users to enter two values; 
#then perform the basic arithmetical operations of addition, 
#subtraction, multiplication and division on the values. 



num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2


print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)


if num2 != 0:
    division = num1 / num2
    print("Division:", division)
else:
    print("Division: Cannot divide by zero")