n = int(input())
list_ = []
for _ in range(n):
    age, name = input().split()
    list_.append((int(age), name))

# list_.sort(key = lambda x : x[0])
list_.sort()

for age, name in list_:
    print(age, name)

# age int로 안바꾸면 틀림