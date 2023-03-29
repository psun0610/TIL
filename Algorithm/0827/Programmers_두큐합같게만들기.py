# 방법 1 - while문 사용 (시간초과)
from collections import deque

def solution(queue1, queue2):
    
    d1 = deque(queue1)
    d2 = deque(queue2)
    cmp1 = deque(queue1)
    cmp2 = deque(queue2)
    answer = 0
    
    sum1 = sum(d1)
    sum2 = sum(d2)
    
    if sum1 == sum2:
        return answer
    
    while sum1 != sum2:
        if d1 == cmp2 and d2 == cmp1:
            return -1
        
        if sum1 > sum2:
            pop_ = d1.popleft()
            d2.append(pop_)
            sum1 -= pop_
            sum2 += pop_
        else:
            pop_ = d2.popleft()
            d1.append(pop_)
            sum1 += pop_
            sum2 -= pop_
        answer += 1

    return answer


#########################################################################
# 방법 2 - for문 사용
from collections import deque

def solution(queue1, queue2):
    
    d1 = deque(queue1)
    d2 = deque(queue2)
    answer = 0
    
    sum1 = sum(d1)
    sum2 = sum(d2)
    
    if sum1 == sum2:
        return answer

    length = max(len(d1), len(d2))
    for i in range(length * 3):
        
        if sum1 > sum2:
            pop_ = d1.popleft()
            d2.append(pop_)
            sum1 -= pop_
            sum2 += pop_
            answer += 1
        elif sum1 < sum2:
            pop_ = d2.popleft()
            d1.append(pop_)
            sum1 += pop_
            sum2 -= pop_
            answer += 1
        else:
            return answer
    else:
        return -1

print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))
print(solution([3, 2, 7, 2], [4, 6, 5, 1]))