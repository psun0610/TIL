# 방법 1
docum = input()
word = input()
ans = docum.replace(word, '1')
print(ans.count('1'))

# 방법 2
docum = input()
word = input()
print(docum.count(word))