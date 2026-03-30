# Create list to store (name, SPI)
students = []

# Input data
for i in range(3):
    name = input(f"Enter name of student {i+1}: ")
    spi = float(input(f"Enter SPI of {name}: "))
    students.append((name, spi))

# Display data
print("\nStudent SPI Records:")
for student in students:
    print(f"Name: {student[0]}, SPI: {student[1]}")