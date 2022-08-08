N = int(input())
guest = list(map(int, input().split()))
print(len(guest) - len(set(guest)))