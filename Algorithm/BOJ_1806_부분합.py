import sys

input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
left, right = 0, 0
sum_ = 0
answer = 1000000000

while 1:
    if sum_ >= s:
        answer = min(answer, right - left)
        sum_ -= nums[left]
        left += 1
    elif right == n:
        break
    else:
        sum_ += nums[right]
        right += 1

if answer == 1000000000:
    print(0)
else:
    print(answer)
