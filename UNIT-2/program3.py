# Write a program to compare tuples of integers and tuples of 
# strings.


t1 = (1, 2, 3)
t2 = (1, 2, 4)

if t1 == t2:
    print("Integer tuples are equal")
else:
    print("Integer tuples are not equal")


s1 = ("apple", "banana", "cherry")
s2 = ("apple", "banana", "cherry")

if s1 == s2:
    print("String tuples are equal")
else:
    print("String tuples are not equal")