# File handling in Python is an essential concept that allows you to create, read, write, and
# manipulate files. Python provides built-in functions and methods to handle files efficiently.
# open() keyword,write() keyword, close() keyword
# file = open('filename.txt', mode)
# Modes:
# 	•	r: Read mode (default). File must exist.
# 	•	w: Write mode. Creates a file if it doesn’t exist; overwrites if it does.
# 	•	x: Create mode. Fails if the file already exists.
# 	•	a: Append mode. Adds data to the end of the file.
# 	•	b: Binary mode. For binary files (use with rb, wb, etc.).
# 	•	t: Text mode (default). For text files.
# 	•	+: Read and write mode.
#######################################--write file---##################################################

import os

# file = open("/Users/vivekkumar/Desktop/BEBO/python/python_3.13/rPractise/practise2.py", 'w')
# file.write("""n = 5
# a, b = 0, 1
# for i in range(n+1):
#     print(a)
#     a, b = b, a + b
# """)
# file.close()
# print("Completed")

#########################################---read file---############################################

# file = open("/Users/vivekkumar/Desktop/BEBO/python/python_3.13/rPractise/file.txt", 'r')
# print(file.readline())
# file.close()

#########################################---append file---##########################################

# file = open("/Users/vivekkumar/Desktop/BEBO/python/python_3.13/rPractise/file.txt", 'a')
# file.write(""" hi this is the file which
# i append for learning purpose""")
# file.close()

#########################################---remove fileffw---##########################################

try:
    os.remove("/Users/vivekkumar/Desktop/BEBO/python/python_3.13/rPractise/file.txt")
    print("File deleted successfully")
except Exception as e:
    print(e)