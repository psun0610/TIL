def solution(cap, n, deliveries, pickups):
    answer = 0
    while deliveries != [0] * n and pickups != [0] * n:
        cur = 0
        max1 = 0
        # 배달하기
        for i in range(n-1, -1, -1):
            # 멀리 있는 것부터 체크하는데,
            # 배달할 것이 0개면 그 앞 집 체크함 (멀리 있는 순서대로 체크 가능)
            if deliveries[i] == 0:
                continue
            # 만약 지금 실을 수 있는 개수보다 많으면 그 앞 집 체크함
            if cap - cur < deliveries[i]:
                continue
            # 멀리 있는 택배 실음
            cur += deliveries[i]
            deliveries[i] = 0

            # max1에는 한 번 택배 보내러 간 거리 더함
            if i+1 > max1:
                max1 = i+1

        cur = 0

        # 수거하기
        for i in range(max1-1, -1, -1):
            # 멀리 있는 것부터 수거할 게 없으면 앞 집 체크함
            if pickups[i] == 0:
                continue
            # 만약 지금 실을 수 있는 개수보다 수거할 개수가 더 많으면 앞 집 체크함
            if cap - cur < pickups[i]:
                continue
            
            cur += pickups[i]
            pickups[i] = 0

        # 수거 2
        max2 = 0
        if deliveries == [0, 0, 0, 0, 0] and pickups != [0, 0, 0, 0, 0]:
            for i in range(n-1, -1, -1):
                if pickups[i] == 0:
                    continue
                if cap - cur < pickups[i]:
                    continue
                if i+1 > max2:
                    max2 = i+1

        answer += max1 * 2 + max2 * 2


    return answer


cap = 2
n = 7
deliveries = [1, 0, 2, 0, 1, 0, 2]
pickups = [0, 2, 0, 1, 0, 2, 0]

print(solution(cap, n, deliveries, pickups))