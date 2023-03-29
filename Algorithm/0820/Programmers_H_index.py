def solution(citations):
    answer = 0
    for h in range(max(citations)):
        acnt, bcnt = 0, 0
        for c in citations:
            if c >= h:
                acnt += 1
            else:
                bcnt += 1
        if acnt >= h and bcnt <= h and h > answer:
            answer = h
    return answer

citations = [3, 0, 6, 1, 5]	
print(solution(citations))