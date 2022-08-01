T = int(input())
for test_case in range(T):
    n, input_str = input().split()
    n = int(n)
    ans_str = ''
    for idx in range(len(input_str)):
        if idx == n-1:
            continue
        else:
            ans_str += input_str[idx]
    print(ans_str)