# Import text file
f = open('pg16317.txt', 'r')


# # Visibility of all unique characters
# char_set = set()
# for c in f.read():
#     char_set.add(c)
# print(list(dict.fromkeys(char_set)))
# # ['s', 'd', 'S', '{', 'u', 'i', 't', '!', 'ë', '”', 'Æ', 'R', 'ö', '—', '3', 'A',
# #  '_', 'H', 'Z', 'L', '(', 'é', 'K', 'z', '$', 'W', 'U', ' ', 'w', 'P', '0', 'G',
# #  '4', '\ufeff', 'F', 'h', '*', '5', ']', '7', '.', '1', ';', 'Q', '|', 'x', '™',
# #  'æ', '?', '6', 'e', '8', 'B', 'T', '/', 'j', '“', '‘', 'f', 'C', 'ê', 'n', 'p',
# #  'V', '\n', 'a', 'J', 'O', 'b', '•', 'Y', '%', ',', '[', 'v', '}', '’', 'c', '2',
# #  'o', 'l', '"', 'y', '-', 'N', '=', 'g', ':', 'M', 'k', '#', 'q', "'", 'D', 'ô',
# #  'I', 'm', 'r', 'X', 'E', '9', ')', 'è']


# Initialize database
# Using defaultdict is preferred here (third party library)
word_freq = dict()


# Count frequency
# This can be performed in parallel (third party library)
for line in f.readlines():
    # Splitting text
    delimiters = ["--"]
    for d in delimiters:
        line = line.replace(d, " ")
    words = line.split()

    # Preprocessing step
    # Using a tokenizer is usually preferred here. (third party library)
    for word in words:

        # Casefolding
        word = word.lower()

        # Removal of punctuations
        # Using a regex is usually preferred here. (third party library)
        # Here I will just remove first or last few punctuations
        punc = "'" + '.,()#:="“”‘’{}[]%•/?™|;*$_!'
        word = word.strip(punc)

        # Increment the seen word in database
        if word not in word_freq:
            word_freq[word] = 0

        word_freq[word] += 1


# Sort the words by frequency
sorted_word_freq = list(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
# print(sorted_word_freq)


# Return words ranked from 10th (inclusive) to 20th (exclusive)
result = sorted_word_freq[9:19]
print("Words ranked from 10th to 20th by frequency:")
for k, v in result:
    print(k + ": " + str(v))