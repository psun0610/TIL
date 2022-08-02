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


# 백준에서 시간 초과 뜸!!!!
# 시간 제한 1초..
