# working with dictionaries, input and open external files
# for / in / if / is / None / or

name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
    print(line.strip())

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print('\n')
print(bigword, bigcount)





# # Dictionaries
# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key in counts:
#     if counts[key] > 10:
#         print(key, counts[key])





# # counting number of words in a phrase
# counts = dict()
# line = input('Enter a line of text:')
# words = line.split()
#
# print('Words:', words)
# print('Counting...')
#
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# print('Counts', counts)





