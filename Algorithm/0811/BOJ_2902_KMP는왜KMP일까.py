long_name = input()
short_name = ''
for char in long_name:
    if ord('A') <= ord(char) <= ord('Z'):
        short_name += char
print(short_name)