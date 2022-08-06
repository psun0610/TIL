import heapq

numbers = [5, 6, 3, 2, 1]
heapq.heapify(numbers)
print(numbers)
heapq.heappop(numbers)
print(numbers)
heapq.heappush(numbers, 10)
print(numbers)
heapq.heappush(numbers, 0)
print(numbers)
heapq.heappush(numbers, 4)
print(numbers)
