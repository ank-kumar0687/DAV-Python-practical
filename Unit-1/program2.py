''' Write a Python script to prompt users to enter the first and last 
values and generate some random values between the two 
entered values.'''


import random



start = int(input("Enter the first value: "))
end = int(input("Enter the last value: "))


print("Random values between", start, "and", end, ":")

for i in range(5):  
    print(random.randint(start, end))