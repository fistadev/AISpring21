phone = input("Phone: ")

number_dig = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
}
output = ""
for ch in phone:
    output += number_dig.get(ch, "!") + " "
print(output)


# customer = {
#     "name": "John Smith",
#     "age": 30,
#     "is_verified": True
# }
#
# print(customer.get("name"))
# print(customer["age"])
# print(customer["is_verified"])


# monthConvertions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",
# }

# print(monthConvertions["Nov"])
# print(monthConvertions.get("Dec"))
# print(monthConvertions.get("Owww", "Not a valid key"))