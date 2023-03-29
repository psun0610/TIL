N = int(input())
for i in range(1, N+1):
    digits = sum(list(map(int, str(i))))
    if i + digits == N:
        print(i)
        break
    if i == N:
        print(0)