def rev(sen):
    words=sen.split()
    ans=[]

    for word in words:
        rev_word=""
        for j in word:
            rev_word=j+rev_word
        ans.append(rev_word)

    return " ".join(ans)

sent="one two three"
res=rev(sent)
print(res)