# N부터 1까지 출력하기
def func(n):
    if n == 0:
        return
    print(n)
    func(n-1)

# 1부터 N까지의 합 구하기
def func2(n):
    if n == 0:
        return 0
    return n + func2(n-1)

func(10)
print(func2(10))