# Input strings
string1 = "listen"
string2 = "silent"

# Remove spaces and convert to lowercase
string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

# Check if lengths are the same (quick fail case for non-anagrams)
if len(string1) != len(string2):
    print(f"'{string1}' and '{string2}' are not anagrams.")
else:
    # Create frequency dictionaries for both strings
    freq1 = {}
    freq2 = {}

    for char in string1:
        freq1[char] = freq1.get(char, 0) + 1

    for char in string2:
        freq2[char] = freq2.get(char, 0) + 1

    # Compare the frequency dictionaries
    if freq1 == freq2:
        print(f"'{string1}' and '{string2}' are anagrams.")
    else:
        print(f"'{string1}' and '{string2}' are not anagrams.")
