count = dict()
text = input('Enter a phrase: ')
words = text.split()
for word in words:
    count[0] = count.get(word[0])

print(count)