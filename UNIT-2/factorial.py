num = int(input("Enter a number: "))

fact = 1

# Check for negative number
if num < 0:
    print("Factorial not possible for negative numbers")
else:
    for i in range(1, num + 1):
        fact = fact * i

    print("Factorial of", num, "is:", fact)