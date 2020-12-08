# 08-03. TEXT PROCESSING [More Exercises]
# 01. Extract Person Information

special_char = ['@', '|', '#', '*']
n = int(input())

for i in range(n):
    line = input()
    idx = {}
    for j, char in enumerate(line):
        if char in special_char:
            idx[char] = j
    name = line[idx['@']+1:idx['|']]
    age = line[idx['#']+1:idx['*']]
    print(f'{name} is {age} years old.')
