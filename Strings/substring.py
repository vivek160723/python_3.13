sen="abcdabc"
n=(len(sen))
max_length=0
long_substring=""

for i in range(n):
    for j in range(i,n):
        curr_sub=sen[i:j+1]
        if len(set(curr_sub))==len(curr_sub):
            if len(curr_sub)>max_length:
                max_length=len(curr_sub)
                long_substring=curr_sub
print(long_substring)