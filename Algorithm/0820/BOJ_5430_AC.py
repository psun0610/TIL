T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    numbers = input()
    numbers = numbers.strip('[]')
    if n > 0:
        numbers = list(map(int, numbers.split(',')))
    
    if p.count('D') > n:    # D명령이 n의 개수보다 많으면 error
        print('error')
    else:
        for AC in p:
            if AC == 'R':   # R: 뒤집기
                numbers = numbers[::-1]
            elif AC == 'D': # D: 첫 번째 수 버리기
                numbers.pop(0)
        print(numbers)
            