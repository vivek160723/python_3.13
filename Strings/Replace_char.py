s = input("Enter the string: ")
new_string = ""
a=input("Enter the character:")
c=input("Enter the chracter by which to replce: ")
for char in s:
    if char == a:
        new_string += c
    else:
        new_string += char

print(new_string)
