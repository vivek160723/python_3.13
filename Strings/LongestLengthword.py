s = input("Enter the string: ")
words = s.split()

longest_word = ""
length = 0

for word in words:
    if len(word) > length:
        longest_word = word
        length = len(word)

print(f"The longest word is: {longest_word} with length: {length}")
