T = int(input())
for i in range(1, T + 1):
    N = int(input())
    books = map(int, input().split())
    tmp_list = []
    for book in books:
        # 리스트의 마지막 요소 + 1 이 book과 같은 것이 있다면 그 리스트에 book 추가하기
        # 없다면 새로운 리스트 생성후 book 추가하기
        isTrue = -1
        for t in range(len(tmp_list)):
            if tmp_list[t][-1] + 1 == book:
                isTrue = t
        if isTrue != -1:
            tmp_list[isTrue].append(book)
        else:
            tmp_list.append([book])

    print(f"#{i} {len(tmp_list)}")
