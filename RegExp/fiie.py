import  re
with open("miracle_in_the_andes.txt", "r", encoding='UTF8') as txtfile:
    book = txtfile.read()

    # with String Function
    print(book.count("Chapter"))

# with Regular Expressions
pattern = re.compile("Chapter [0-9]+")
finds = re.findall(pattern, book)
print(len(finds))


# Which are the sentence where "Love" used
pattern = re.compile("[A-Z]{1}[^. ]*[^a-zA-Z]+love[^a-zA-Z][^. ]*.")
finds = re.findall(pattern, book)
print(len(finds))

# What are most used words
pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())
d = {}
for words in findings:
    if words in d.keys():
        d[words] = d[words]+1
    else:
        d[words] = 1


d_list = [(value, key) for (key, value) in d.items()]
final = sorted(d_list, reverse=True)
print(final)

