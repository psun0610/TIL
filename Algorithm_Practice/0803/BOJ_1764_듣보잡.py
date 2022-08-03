n, m = map(int, input().split())
listen = [input() for _ in range(n)]
watch = [input() for _ in range(m)]
answer = []

for l in listen:
    if watch.count(l) == 1:
        answer.append(l)
answer.sort()

print(len(answer))
for a in answer:
    print(a)

#============================================
dict_ = dict()
n, m = map(int, input().split())
for _ in range(n):
    dict_[input()] = '듣도 못한 사람'

list_ = []
for _ in range(m):
    name = input()
    if name in dict_:
        list_.append(name)

list_.sort()
print(len(list_))
for p in list_:
    print(p)