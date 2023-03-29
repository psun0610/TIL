# N = int(input())
# for i in range(N):
#     print('* '*N if i%2 == 0 else ' *'*N)

N = int(input())
for i in range(1, N+1):
    if i % 2 == 0:
        print(' ', end='')
    for j in range(1, N+1):
        print('*', end=' ')
    print()