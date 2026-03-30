
students = {}


for i in range(3):
    name = input(f"Enter name of student {i+1}: ")
    spi = float(input(f"Enter SPI of {name}: "))
    students[name] = spi


print("\nStudent SPI Records:")
for name, spi in students.items():
    print(f"Name: {name}, SPI: {spi}")