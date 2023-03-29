import sys

sys.stdin = open("_Flatten.txt")

for test_case in range(1, 11):
    n = int(input())
    box = list(map(int, input().split()))
    for i in range(n):
        max_ = box.index(max(box))
        min_ = box.index(min(box))

        if max_ == min_:                    # max와 min의 인덱스가 같다면 평탄화가 끝난 것이므로 break
            break

        box[max_] -= 1
        box[min_] += 1

    print(f'#{test_case} {max(box) - min(box)}')