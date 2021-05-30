# Counting words line by line.
# Counting words in blakepoems.txt.

with open("text-files/blakepoems.txt",) as fp:
    lines = (line.rstrip() for line in fp)
    print(lines)
    lines = list(line for line in lines if line)  # Non-blank lines in a list


def word_counter(lines):
    word_count = {}
    for i in range(len(lines)):        # count line by line
        line = lines[i]
        words = line.split()

        for word in words:
            word = word.lower()
            count_holder = word.count(word)
            if word in word_count:                      # checks if key already existing
                count_holder_dict = word_count[word]
                # this killed me till i got how to add the values to the key seems like a workaround :/
                count = count_holder + count_holder_dict
                word_count[word] = count
            else:
                word_count[word] = count_holder
    # sort if x[0]alphabtically key if [0] values //reversed=False change order reversed=True
    return sorted(word_count.items(), key=lambda x: x[0])


word_counter(lines)
