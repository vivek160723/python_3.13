def long_word(str):
    ans=str.split()
    max_length=0
    word=""
    for i in ans:
        count=0
        for j in i:
            count+=1
        if count>max_length:
            max_length=count
            word=i
    print(word,max_length)

long_word("my name is chaudhary vivek")