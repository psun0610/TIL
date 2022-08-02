import heapq

numbers = [5, 3, 2, 4, 1]

heapq.heapify(numbers)
heapq.heappop(numbers)
heapq.heappop(numbers)
heapq.heappush(numbers, 10)
heapq.heappush(numbers, 0)
print(numbers)