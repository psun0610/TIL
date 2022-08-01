T = int(input())
for test_case in range(T):
    parenth = input()
    stack_ = []
    vps = ''
    for char in parenth:
        if char == '(':
            stack_.append(1)
        else:
            if len(stack_) != 0:
                stack_.pop()
            else:
                vps = 'NO'
                stack_.append(1)
                break

    if len(stack_) == 0:
        vps = 'YES'
    else:
        vps = 'NO'
    print(vps)
