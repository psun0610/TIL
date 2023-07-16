import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
Pn = input()
status = "I"
cnt = 0
answer = 0
standard = 3 + 2 * (n - 1)

for P in Pn:
    # IO 번갈아 나오는지 확인
    if P == status:
        cnt += 1
        if status == "I":
            status = "O"
        else:
            status = "I"
    else:
        if P == "I":
            if cnt >= standard:
                answer += (cnt // 2) - (n + 1) + 2
            cnt = 1
            status = "O"
        else:
            if cnt >= standard:
                answer += ((cnt - 1) // 2) - (n + 1) + 2
            cnt = 0
            status = "I"
    print(f"P: {P} // cnt: {cnt} // status: {status} // answer: {answer}")

print(answer)
