# 1. 길이가 짧은 것
# 2. 자리수 합이 작은 것 (숫자만 더함)
# 3. 사전 순 비교 (숫자가 알파벳보다 사전순으로 작음)

n = int(input())
serial = []
for _ in range(n):
    number = input()
    num_sum = 0

    for i in number:
        if 49 <= ord(i) <= 57:
            num_sum += int(i)
    
    serial.append((number, num_sum))

serial.sort(key = lambda x : (len(x[0]), x[1], x[0]))

for number in serial:
    print(number[0])