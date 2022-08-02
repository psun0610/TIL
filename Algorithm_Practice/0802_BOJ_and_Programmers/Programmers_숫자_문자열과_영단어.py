# 딕셔너리 만들기

def solution(s):
    answer = s
    numbers = {'zero': '0',
           'one': '1',
           'two': '2',
           'three': '3',
           'four': '4',
           'five': '5',
           'six': '6',
           'seven': '7',
           'eight': '8',
           'nine': '9'}

    for number in numbers:
        answer = answer.replace(number, numbers.get(number))
    return int(answer)

neo = input()
print(solution(neo))
