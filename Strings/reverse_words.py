input_string =input("Enter the string for reverse: ")
ans=input_string.split()
reversed_words = ' '.join([word[::-1] for word in ans])

print("Reversed Words String:", reversed_words)
