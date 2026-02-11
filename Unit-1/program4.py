'''Write a Python program to prompt users to enter a Celsius 
value; then convert Celsius to Fahrenheit, where T(°F) = T(°C) x 
1.8 + 32. Display the result. '''



celsius = int(input("Enter temperature in Celsius: "))


fahrenheit = celsius * 1.8 + 32


print("Temperature in Fahrenheit:", fahrenheit)