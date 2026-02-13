#  Write a program to read text file data and create a dictionary of 
# all keywords in the text file. The program should count how many 
# times each word is repeated inside the text file and then find the 
# keyword with a highest repeated number.The program should 
# display both the keywords dictionary and the most repeated word.



with open("sample.txt", "r") as file:
    content = file.read().lower()  


words = content.split()


word_counts = {}

for word in words:
    
    word = word.strip(".,!?\"'()[]")
    
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


most_repeated = max(word_counts, key=word_counts.get)


print("--- Word Frequency Dictionary ---")
print(word_counts)

print("\n--- Result ---")
print(f"The most repeated word is '{most_repeated}' with {word_counts[most_repeated]} occurrences.")