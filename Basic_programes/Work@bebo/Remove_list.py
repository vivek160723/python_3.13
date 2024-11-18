list = [1, 2, 3, 2, 4, 1, 5, 3]
ans = []
for i in list:
    duplicate = False
    for j in ans:
        if j == i:
            duplicate = True
            break
    if not duplicate:
        ans.append(i)


print("Original List:", list)
print("List Without Duplicates:", ans)
