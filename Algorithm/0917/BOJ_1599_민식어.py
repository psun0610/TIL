# a b c d e f g h i j k l m n o p q r s t u v w x y z
# a b 'k' d e g h i '' l m n 'ng' o p r s t u w y

n = int(input())
minsik = []
for _ in range(n):
    word = input()
    word = word.replace('k', 'c')
    word = word.replace('ng', 'nz')
    minsik.append(word)

minsik.sort()

for word in minsik:
    word = word.replace('c', 'k')
    word = word.replace('nz', 'ng')
    print(word)