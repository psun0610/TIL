n, m = map(int, input().split())
card = list(map(int, input().split()))
max_sum = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            sum_ = card[i] + card[j] + card[k]
            if sum_ > max_sum and sum_ <= m:
                max_sum = sum_
            
            if max_sum == m:
                break
print(max_sum)