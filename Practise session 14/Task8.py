try:
    with open("/rPractise/file1.txt", 'r') as file1:
        file1_content = file1.read()

    with open("/rPractise/file2.txt", 'a') as file2:
        file2.write(file1_content)

    with open("/rPractise/file2.txt", 'r') as file3:
        file2_content = file3.read()

    with open("/rPractise/merged.txt", 'a') as file4:
        file4.write(file2_content)

    print("Finish")
except Exception as e:
    print(f"Error: {e}")