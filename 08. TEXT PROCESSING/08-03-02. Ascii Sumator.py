# 08-03. TEXT PROCESSING [More Exercises]
# 02. Ascii Sumator

start = ord(input())
end = ord(input())
string = input()
ascii_sum = 0

for char in string:
    if start < ord(char) < end:
        ascii_sum += ord(char)

print(ascii_sum)
