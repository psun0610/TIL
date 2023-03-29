n = int(input())
l = []
for i in range(n):
    a = input()
    l += a
l.sort()
for j in range(n):
    print(l[j])