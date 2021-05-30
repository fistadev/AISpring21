# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for row in matrix:
#     for item in row:
#         print(item)


# append()
# insert()
# remove()
# clear()
# pop()
# index()
# count()
# sort()
# copy()

# Exercise 1: remove duplicates on a list

# numbers = [2, 3, 2, 4, 6, 7, 6, 4, 2, 3, 5, 7]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)



# Exercise 2: remove duplicates on a list, count original list and list without duplicates

countries = [
    "Brazil",
    "Italia",
    "USA",
    "Brazil",
    "Norway",
    "Brazil",
    "Brazil",
    "Italy",
    "Norway",
    "Norway",
    "USA",
    "Mexico",
    "Portugal",
    "France",
    "France"
]
uniques = []
for country in countries:
    if country not in uniques:
        uniques.append(country)
print(uniques)
print(f'{len(countries)} countries')
print(f'{len(uniques)} unique countries')






# matrix [0] [1] = 20
# print(matrix[0][1])