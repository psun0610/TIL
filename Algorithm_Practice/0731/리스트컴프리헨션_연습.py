n = int(input())
numbers = [i**2 for i in range(1, n+1)]
print(numbers)

n = int(input())
numbers = ["No."+ str(i) for i in range(1, n+1)]
print(numbers)

numbers = [int(input()) for i in range(9)]
max_ = max(numbers)
index_ = numbers.index(max_) + 1

print(max_, index_, sep='\n')