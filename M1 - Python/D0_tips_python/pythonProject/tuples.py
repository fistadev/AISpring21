# coordinates = (4, 5)
# print(coordinates)
# print(coordinates[0])
# print(coordinates[1])




# list_coordinates = [(4, 5), (7, 3), (9, 6), (44, 17)]
# print(list_coordinates)





# Tuples
# Which does the same thing as the following code?:

lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)

# Does the same thing than the above
print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )