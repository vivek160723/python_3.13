def freq(str):
    ans={}
    for i in str:
        if i in ans:
            ans[i]+=1
        else:
            ans[i]=1
    print(ans)

sentence="aaabbbccc"
freq(sentence)

