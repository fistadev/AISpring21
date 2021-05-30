# Counting words in blakepoems.txt.

# open file
with open("text-files/blakepoems.txt",) as fp:
    lines = (line.rstrip() for line in fp)
    print(lines)
    # Non-blank lines in a list
    lines = list(line for line in lines if line)


def word_counter(lines):
    word_count = {}
    # count line by line
    for i in range(len(lines)):
        line = lines[i]
        words = line.split()

        for word in words:
            word = word.lower()
            count_holder = word.count(word)
            # checks if key already existing
            if word in word_count:
                count_holder_dict = word_count[word]
                # this killed me till i got how to add the values to the key seems like a workaround :/
                count = count_holder + count_holder_dict
                word_count[word] = count
            else:
                word_count[word] = count_holder
    # sort if x[0]alphabtically key if [0] values //reversed=False change order reversed=True
    return sorted(word_count.items(), key=lambda x: x[0])


word_counter(lines)


# Counting words in blakepoems.txt
fp = open("./text-files/blakepoems.txt", "r")

f = dict()


def clean_all_file(text):


['word', 'a', 'b']


def build_dict(1):


def main():
    b = clean_all_file(a)
    c = build_dict(b)


main()


# counts = dict()
# files = open('text-files/blakepoems.txt')


# def readfile(txt):
#     for file in files.readlines():
#         file.count(file)


# def countwords(line):
#     for word in words:
#         words = files.split()
#         counts[word] = counts.get(word, 0) + 1


# def main(x):
#     print(f'Count: {x}')


# if __name__ == '__main__':
#     main(counts)
