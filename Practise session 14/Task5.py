file = open("/rPractise/data.csv", 'r')
for i in file:
    print(file.readline())
file.close()
