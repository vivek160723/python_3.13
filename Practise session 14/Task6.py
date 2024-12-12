try:
    file = open("/rPractise/sourcefile.txt", 'r')
    file1=file.read()
    file2=open("/rPractise/Destinationfile.txt", 'a')
    file2.write(file1)
    file.close()
    print("Finish")
except Exception as e:
    print(e)