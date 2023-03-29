def Rev(num):
    num = int(str(num)[::-1])
    return num

x, y = map(int, input().split())
print(Rev(Rev(x) + Rev(y)))