# 이중포문을 써서 시간 초과가 난 사례
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    test = []
    cnt = 0

    # 입력 받은 두 성적 순위를 튜플 형태로 리스트에 넣음
    for _ in range(n):
        a, b = map(int, input().split())
        test.append((a, b))
    
    # 먼저 서류심사 순위을 기준으로 정렬을 함
    test.sort(key=lambda x: x[0])
    
    # 정렬된 리스트를 순회함
    for applicant in test:
        # 현재 비교중인 applicant보다 서류심사 순위가 더 높은 사람들과만 면접 성적의 순위를 비교하면 됨
        # 그래서 applicant[0]-1만큼 또 순회함
        for j in range(applicant[0]-1):
            # 만약 현재 applicant의 면접 순위가 더 낮으면 이 사람은 선발대상이 아니므로 break
            if applicant[1] > test[j][1]:
                break
        # 만약 for문을 break없이 다 돌았다면 이 사람은 선발대상이기 때문에 카운트 + 1 해줌
        else:
            cnt += 1

    # 카운트 출력
    print(cnt)


# =================================================
# 위 코드에서 이중포문 부분을 for 1개로 해결함
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    test = []
    cnt = 0

    # 입력 받은 두 성적 순위를 튜플 형태로 리스트에 넣음
    for _ in range(n):
        a, b = map(int, input().split())
        test.append((a, b))
    
    # 먼저 서류심사 순위을 기준으로 정렬을 함
    test.sort(key=lambda x: x[0])
    
    # 어차피 서류심사 순위가 더 높은 사람보다 면접성적 순위가 높아야 하므로
    # 서류심사 순위가 높은 사람들 중 제일 높은 면접 순위를 best 변수에 넣을 거임
    # 그래서 일단 서류심사 1등인 사람의 면접 순위를 넣어 놓음
    best = test[0][1]

    # 반복을 돌건데 현재 applicant가 best보다 순위가 더 높으면 (숫자가 더 낮으면)
    # best를 바꿔주고 카운트 + 1 해줌
    for applicant in test:
        if applicant[1] <= best:
            best = applicant[1]
            cnt += 1

    print(cnt)


# =================================================
# 위 두가지는 sort메소드 + lambda함수를 사용했는데
# 이 문제에는 동석차가 없다는 가정이 있기 때문에 리스트의 인덱스를 이용하여
# sort도 안쓰고 입력 받을 때 바로 정렬을 할 수 있음!
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    cnt = 0

    # 먼저 지원자 수만큼 0으로 초기화해둠
    score = [0] * (n + 1)
    for _ in range(n):
        x, y = map(int, input().split())
        # 그리고 리스트에 넣을 때 서류심사 순위를 인덱스로 넣고 면접 순위를 값으로 재할당해줌
        score[x] = y

    # 아래는 2번째 방법과 같은 방식임
    best = score[1]
    # 순위는 1위부터 있으므로 range는 1부터 n+1까지로 둠
    for i in range(1, n+1):
        # 만약 best 면접순위보다 현재 지원자의 면접순위가 더 높다면
        if best >= score[i]:
            # best를 바꿔주고
            best = score[i]
            # 카운트 + 1 해줌
            cnt += 1

    print(cnt)