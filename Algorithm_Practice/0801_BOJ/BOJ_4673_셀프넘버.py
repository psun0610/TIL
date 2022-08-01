# d(n)은 n과 n의 각 자리수를 더하는 함수, 이때 n은 d(n)의 생성자
tmplist = []
for i in range(1, 10001):
    notself = i + sum(map(int, str(i)))
    tmplist.append(notself)

for i in range(1, 10001):
    if i not in tmplist:
        print(i)