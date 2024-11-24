def long(sentence):
    words=sentence.split()
    max_len=0
    for i in words:
        current_length=0
        for j in i:
            current_length += 1
        if current_length>max_len:
            max_len=current_length
    return max_len

str1="i am vivek"
result=long(str1)
print(result)
