try:
    with open("/rPractise/document.txt", "r") as file:
        lines = file.readlines()

    with open("/rPractise/document.txt", "r") as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        alphabet_count = 0
        for char in content:
            if char.isalpha():
                alphabet_count += 1
        line_count = len(lines)

        print(f"The number of words in 'document.txt' is: {word_count}")
        print(f"The number of alphabetic characters in 'document.txt' is: {alphabet_count}")
        print(f"The number of lines in 'document.txt' is: {line_count}")
except FileNotFoundError:
    print("The file 'document.txt' was not found.")