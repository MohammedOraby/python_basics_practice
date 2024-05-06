## get frequency of letters

def get_letter_freq (string) :
    letters_freq = {}
    string = string.lower()
    for letter in string :
        letters_freq[letter] = letters_freq.get(letter,0)+1
    return letters_freq
result = get_letter_freq("aAaMmFsfffss")
print(result)