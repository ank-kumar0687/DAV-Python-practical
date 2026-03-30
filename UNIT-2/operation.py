

s = input("Enter a string: ")


vowels = "aeiouAEIOU"
vowel_count = 0
for ch in s:
    if ch in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)


length = 0
for ch in s:
    length += 1

print("Length of string:", length)


reverse = ""
for ch in s:
    reverse = ch + reverse

print("Reversed string:", reverse)


find_word = input("Enter word to find: ")
replace_word = input("Enter word to replace: ")

new_string = s.replace(find_word, replace_word)
print("After replace:", new_string)


if s == reverse:
    print("String is Palindrome")
else:
    print("String is NOT Palindrome")