#  Write a program to prompt users to enter a value;then check 
# whether the entered value is positive or negative value and 
# display a proper message.




num = int(input("Enter a number: "))


if num > 0:
    print("The entered value is Positive.")

elif num < 0:
    print("The entered value is Negative.")

else:
    print("The entered value is Zero.")