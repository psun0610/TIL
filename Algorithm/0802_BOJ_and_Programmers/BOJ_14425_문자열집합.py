n, m = map(int, input().split())
s = ()
words = ()

for _ in range(n):
    s.add(input())
for _ in range(m):
    words.add(input())

# 방법 1
count = 0
for word in words:
    if word in s:       # s를 리스트로 받아왔다면 set(s)와 s를 비교하는 것의 시간 차이를 보자
        count += 1      # 밖에서 set(s)를 변수로 선언하고 쓰는 것과 반복문 안에 set(s)를 바로 쓰는 것 중 뭐가 더 빠른지도 보기
print(count)

# 방법 2
print(len(words & s))