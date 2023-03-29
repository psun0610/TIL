n = int(input())
books = {}
for _ in range(n):
    book = input()
    # books 딕셔너리에 book 키가 없으면 books[book] = 1
    # 키가 있으면 + 1
    books[book] = books.get(book, 0) + 1
    
best = []
for book in books:
    if books[book] == max(books.values()):
        best.append(book)

best.sort()
print(best[0])