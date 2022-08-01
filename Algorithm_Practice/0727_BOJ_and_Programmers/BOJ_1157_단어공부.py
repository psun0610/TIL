# 리스트에 한 글자씩 집어넣음
word = input()
# 모든 글자를 대문자로 바꿈
word = word.upper()
# 하나하나 리스트에 넣음
word = list(map(str, word))
ans = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for char in word:
    # 대문자 A는 65이므로 ord()한 것에 65를 빼서 A가 0이 되도록 만듬
    # 이 값을 ans 리스트의 인덱스로 사용하여 1을 더해줌
    ans[ord(char) - 65] += 1

# 리스트 중 가장 큰 값의 인덱스 구하기
max_ = max(ans)
mode_ = -1
overlap = 0
for i in range(26):
    # ans[i]의 값이 ans의 최대값과 같다면 mode_에 최빈값 등록
    if ans[i] == max_:
        mode_ = i
        overlap += 1
    # 중복되는 값이 있다면 ?출력
    if overlap > 1:
        mode_ = ord('?') - 65
print(chr(mode_ + 65))
