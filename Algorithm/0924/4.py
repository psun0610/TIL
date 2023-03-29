def binary(num):
    save = []
    
    while True:
        a = int(num / 2)
        b = int(num % 2)
        save.insert(0, b)
        
        if a != 0:
            num = a
        else:
            break
            
    final = ''.join(map(str, save))
    print(final)

def solution(numbers):
    binary_list = []
    for num in numbers:
        binary_list.append(binary(num))

    answer = []
    return answer

solution([63, 111, 95])
