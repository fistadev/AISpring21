# Heavy Metal
# Death Metal
# Black Metal
# Thrash Metal
# Speed Metal
# Power Metal

styles = {
    'Jazz': 'Jazz',
    'Blues': 'Blues',
    'Rock': ['Classic Rock', 'Hard Rock', 'Rockabilly', 'Prog Rock'],
    'Metal': ['Heavy Metal', 'Death Metal', 'Black Metal', 'Thrash Metal', 'Speed Metal', 'Power Metal', 'Prog Metal']
}

# 3 solutions for the same thing
for key, value in styles.items():
    print(key, ':', value)

# for key in styles:
#     print(key, ':', styles[key])

# [print(key, ':', value) for key, value in styles.items()]