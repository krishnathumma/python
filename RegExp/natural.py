import re
import nltk

with open("miracle_in_the_andes.txt", "r", encoding='UTF8') as txtfile:
    book = txtfile.read()

# most user words
pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())

d = {}
for words in findings:
    if words in d.keys():
        d[words] = d[words] + 1
    else:
        d[words] = 1

d_list = [(value, key) for (key, value) in d.items()]
final = sorted(d_list, reverse=True)

from nltk.corpus import stopwords

english_stopwords = stopwords.words("english")

filtered_words = []
for count, words in d_list:
    if words not in english_stopwords:
        filtered_words.append({words, count})

print(filtered_words)
