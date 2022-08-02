# A의 원소개수 an, B의 원소개수 bn
an, bn = map(int, input().split())
# A집합과 B 집합
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# 두 리스트를 합치고 set으로 중복을 2번 제거하여 길이 출력할 거임
# 두 리스트의 중복 개수: (an + bn) - len(set(A + B))
print(2 * len(set(A + B)) - (an + bn))