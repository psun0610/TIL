list_ = []
for i in range(10):
    list_.append(int(input()) % 42)
print(len(list(set(list_))))