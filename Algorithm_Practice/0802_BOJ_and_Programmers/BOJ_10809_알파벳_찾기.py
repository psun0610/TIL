word = input()
for i in range(26):
    print(word.find(chr(i + 97)), end = ' ')