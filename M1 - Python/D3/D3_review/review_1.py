# # Your functions
# a = [2, 4, 6, 12, 15, 99, 100]
# count = 0
# for item in a:
#     if item % 3 == 0:
#         count += 1

# print(max(a))
# print(min(a))
# print(count)


# Your functions
def main():
    """
    a = [2, 4, 6, 12, 15, 99, 100]
    100
    2
    4
    """
    a = [2, 4, 6, 12, 15, 99, 100]
    a.sort()
    a.sort()
    smallest = a[0]
    largest = a[len(a)-1]
    count = 0
    for n in a:
        if n % 3 == 0:
            count += 1
    print(count)
    return [smallest, largest, count]


main()
