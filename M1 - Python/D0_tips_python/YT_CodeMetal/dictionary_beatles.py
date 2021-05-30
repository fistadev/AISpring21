# Criando um dicionario basico em Python
keys = ['John', 'Paul', 'George', 'Ringo']
values = ['guitar', 'bass', 'solo guitar', 'drums']

data = dict(zip(keys, values))

print(data)
# print(data['Paul'])
# print(data['Martin']) # error (not available)
data['Martin'] = 'production' # adding values
print(data)

del data['John'] # remove values
print(data)