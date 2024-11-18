text = input("Enter a string: ")
result = ""
ans = True

for char in text:
    if char.isspace():
        result += char
        ans = True
    elif ans:
        result += char.upper()
        ans = False
    else:
        result += char.lower()

print("Title Case:", result)
