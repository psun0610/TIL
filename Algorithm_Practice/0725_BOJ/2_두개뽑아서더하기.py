# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    # numbers 리스트의 인덱스를 이용할 것이므로 range(), len()을 이용함
    for i in range(len(numbers)):
        # 인덱스가 겹치지 않고 다른 수를 더해야하므로 i+1부터 numbers의 마지막까지 반복함
        for j in range(i+1, len(numbers)):
            # sum변수에 더한 값을 저장
            sum = numbers[i] + numbers[j]
            # answer리스트에 sum을 요소로 추가함
            answer.append(sum)
    # answer 리스트를 set으로 중복을 제거하고, sorted()함수로 오름차순 정렬함
    answer = sorted(list(set(answer)))
    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
