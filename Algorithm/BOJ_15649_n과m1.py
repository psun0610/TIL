import itertools

n, m = map(int, input().split())
list_ = [i for i in range(1, n + 1)]
result = itertools.permutations(list_, m)

for i in result :
    print(*i)