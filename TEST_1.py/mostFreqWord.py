# def most_frequent_word(sentence):
#     words = sentence.split()
#     word_count = {}
#
#     for word in words:
#         word = word.lower()
#         word_count[word] = word_count.get(word, 0) + 1  # Increment word count
#
#     # Find the word with the highest frequency
#     most_frequent = max(word_count, key=word_count.get)
#     return most_frequent, word_count[most_frequent]
#
# # Example usage
# sentence = "apple mango banana apple apple mango "
# word, count = most_frequent_word(sentence)
# print(f"The most frequent word is '{word}' with a count of {count}.")

######################################################################################################################

sentence="apple mango mango apple apple apple banana"
words=sentence.split()
ans={}
for word in words:
    word=word.lower()
    ans[word]=ans.get(word,0)+1
most_freq=max(ans,key=ans.get)

print(most_freq,ans[most_freq])