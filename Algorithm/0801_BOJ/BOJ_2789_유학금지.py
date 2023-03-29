delete_str = 'CAMBRIDGE'
input_str = input()
answer_str = ''
for char in input_str:
    if char not in delete_str:
        answer_str += char
print(answer_str)