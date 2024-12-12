try:
    with open("/Users/vivekkumar/Desktop/BEBO/python/python_3.13/rPractise/document.txt", "r") as file:
        content = file.read()
        lines = content.splitlines()  # Splitting the content into lines
        words = content.split()  # Splitting content into words
        word_count = len(words)  # Counting words
        alphabet_count = sum(1 for char in content if char.isalpha())  # Counting alphabetic characters
        line_count = len(lines)  # Counting lines

    # Printing the results
    print(f"The number of words in 'document.txt' is: {word_count}")
    print(f"The number of alphabetic characters in 'document.txt' is: {alphabet_count}")
    print(f"The number of lines in 'document.txt' is: {line_count}")

except FileNotFoundError:
    print("The file 'document.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

# try:
#     file_name = input("Enter the name of the file: ")
#
#     # Open the user-provided file
#     with open(f"/Users/vivekkumar/Desktop/BEBO/python/python_3.13/rPractise/{file_name}", "r") as file:
#         lines = file.readlines()
#
#     # Open the document.txt file
#     with open("/Users/vivekkumar/Desktop/BEBO/python/python_3.13/rPractise/document.txt", "r") as file:
#         content = file.read()
#         words = content.split()
#         word_count = len(words)
#         alphabet_count = sum(1 for char in content if char.isalpha())
#         line_count = len(lines)
#
#     print(f"The number of words in 'document.txt' is: {word_count}")
#     print(f"The number of alphabetic characters in 'document.txt' is: {alphabet_count}")
#     print(f"The number of lines in 'document.txt' is: {line_count}")
# except FileNotFoundError as e:
#     print(f"File not found: {e}")
# except Exception as e:
#     print(f"An error occurred: {e}")