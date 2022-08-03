# 리스트 이용 -> 백준 시간초과남
n = int(input())
log = []
# enter 하면 log에 추가, leave 하면 log에 삭제
for i in range(n):
    name, status = input().split()
    if status == 'enter':
        log.append(name)
    else:
        log.remove(name)
log.sort(reverse = True)

for person in log:
    print(person)


# 딕셔너리 이용
n = int(input())
log = {}
ans = []
for i in range(n):
    name, status = input().split()
    log[name] = status

for l in log:
    if log[l] == 'enter':
        ans.append(l)
ans.sort(reverse = True)
for a in ans:
    print(a)