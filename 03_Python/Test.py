# class Person:
#     species = '사람'
    
#     # 생성자 메서드
#     def __init__(self, name):
#         # 개별 인스턴스에 각각 name 속성 지정
#         self.name = name

#     # 모든 인스턴스 메서드에는 self
#     def greeting(self):
#         print(f'안녕하세요, {self.name}입니다.')

# iu = Person('지은')
# iu.greeting()
# iu.test()

# print(Person.species)


# # 로또
# import random
# numbers = range(1, 46)
# result = random.sample(numbers, 6)
# result.solt()
# print(result)

from functools import reduce
print(reduce(lambda x, y: y + x, 'abcde'))
print(reduce(lambda x, y: y + x, range(11)))
print(list(range(11)),type(list((range(11)))))