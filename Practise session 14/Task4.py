from itertools import count
try:
    with open("/rPractise/document.txt", "r") as file:
        content = file.read()
        words = content.split()
        word_count = len(words)

        print(f"The number of words in 'document.txt' is: {word_count}")
except FileNotFoundError:
    print("The file 'document.txt' was not found.")