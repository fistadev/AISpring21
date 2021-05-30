# # Count number of same letters 'a'
# word = 'paralelepipedo'
# count = 0
# for letter in word:
#     if letter == 'p':
#         count = count + 1
# print(count)




# count_vowels

phrase = input("please add a word or phrase: ")


def count_vowels(word):
    count = 0
    for vowel in word:
        if vowel in "aAeEiIoOuU":
            count = count + 1
    return count


print(count_vowels(phrase))




# # String and functions
# coisa = 'death metal'
# for n in coisa:
#     print(n)
#
# # print(len(coisa))




# # Search using boolean variable
# found = False
# print('Before', found)
# for value in [9, 41, 12, 3, 74, 15]:
#     if value == 3:
#         found = True
#     print(found, value)
# print('After', found)




# # Filtering a loop
# print('Before')
# for value in [9, 41, 12, 3, 74, 15]:
#     if value > 20:
#         print('Large number:', value)
# print('After')




# # Finding average in a loop
# count = 0
# sum = 0
# print('Before:', count, sum)
# for value in [9, 41, 12, 3, 74, 15]:
#     count = count + 1
#     sum = sum + value
#     print(count, sum, value)
# print('After:', count, sum, sum / count)




# # Summing in a loop from 1 to 10
# sum = 0
# print('Before:', sum)
# for thing in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum = sum + thing
#     print(sum, thing)
# print('After:', sum)




# # Counting a loop
# zork = 0
# print('Before:', zork)
# for thing in [9, 41, 12, 3, 74, 15]:
#     zork = zork + 1
#     print(zork, thing)
# print('After:', zork)




# # Smallest number
# smallest = None
# print("Before:", smallest)
# for itervar in [13, 41, 12, 9, 74, 15]:
#     if smallest is None or itervar < smallest:
#         smallest = itervar
#         # break
#     print("Loop:", itervar, smallest)
# print("Smallest:", smallest)


# friends = ["Jim", "Karen", "Kevin"]
# for index in range(5):
#     if index == 0:
#         print("first iteration")
#     else:
#         print("Not first")


# friends = ["Jim", "Karen", "Kevin"]
# for index in range(len(friends)):
#     print(friends[index])


# friends = ["Jim", "Karen", "Kevin"]
# for name in friends:
#     print(name)


# for index in range(10):
#     print(index)


# for index in range(1, 7):
#     print(index)


# for letter in "Heavy Metal":
#     print(letter)