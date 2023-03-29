A, B = map(int, input().split())
# 최대공약수
for i in range(min(A, B), 0, -1):
    if A % i == 0 and B % i == 0:
        print(i)
        #최소공배수 방법 1
        print(A*B // i)
        break
# 최소공배수 방법 2
# for j in range(max(A, B), A*B + 1):
    # if j % A == 0 and j % B == 0:
        # print(j)
        # break