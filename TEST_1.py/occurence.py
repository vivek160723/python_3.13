# write a code to find the occurrence of each word in a sentence
def occur(sentence):
    ans=sentence.split()
    result={}
    count=0
    for word in ans:
            result[word]=result.get(word,0)+1
    return result
sent="one two one one three five one"
result=occur(sent)
print(result)