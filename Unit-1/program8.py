# Write a program to prompt users to enter an age; then check 
# whether each person is a child, a teenager, an adult, or a senior. 
# Display a proper message.




age = int(input("Enter age: "))


if age < 0:
    print("Invalid age entered.")

elif age <= 12:
    print("The person is a Child.")

elif age <= 19:
    print("The person is a Teenager.")

elif age <= 59:
    print("The person is an Adult.")

else:
    print("The person is a Senior.")