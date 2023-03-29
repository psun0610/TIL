a, b, c = map(int, input().split())
parking_time = [[] for _ in range(3)]
for i in range(3):
    arrival, departure = map(int, input().split())
    for j in range(arrival + 1, departure + 1):
        parking_time[i].append(j)
    

parking_fee = 0
for i in range(min(map(min, parking_time)), max(map(max, parking_time)) + 1):
    if i in parking_time[0] and i in parking_time[1] and i in parking_time[2]:
        parking_fee += c * 3
    elif (i in parking_time[0] and i in parking_time[1]) or (i in parking_time[1] and i in parking_time[2]) or (i in parking_time[2] and i in parking_time[0]):
        parking_fee += b * 2
    elif i in parking_time[0] or i in parking_time[1] or i in parking_time[2]:
        parking_fee += a

print(parking_fee)