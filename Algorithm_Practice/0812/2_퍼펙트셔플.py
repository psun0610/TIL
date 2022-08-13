import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    card = list(input().split())
    if len(card) % 2 == 0:
        card1 = card[:len(card)//2]         # 카드덱 반으로 나누기 (카드 덱이 5장인 경우(홀수인 경우) 3, 2로 나눠야 하므로 if로 경우 나눠줌)
        card2 = card[len(card)//2:]
    else:
        card1 = card[:len(card)//2 + 1]
        card2 = card[len(card)//2+1:]

    ans = []                            # 정답을 저장할 리스트
    # print(card1, card2)
    for i in range(len(card)//2):
        ans.append(card1.pop(0))
        ans.append(card2.pop(0))

    if len(card1) > 0:                      # 카드덱이 홀수일 경우에는 card1 덱에 하나가 남기 때문에 남는다면 pop해줌
        ans.append(card1.pop(0))

    print(f'#{test_case}', end = ' ')
    for c in ans:
        print(c, end = ' ')
    print()