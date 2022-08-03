###
# 목적: {파일 이름} + {문제 번호}.py 형식의 파일을 6099번까지 자동 생성
# 조건: codeup 문제 풀이를 저장하고 있는 같은 디렉토리(폴더)에서 실행해 주세요.

import os

#현재 파일의 폴더 경로; 작업 파일 기준
print(os.path.dirname(os.path.realpath(__file__)))





###### 입력 1. 시작 번호
print("\n")
print("*반복문 시작할 문제 번호 \n*(4자리 숫자 형식으로 입력) // ex. 6019")
print("\n")
F_num = int(input("시작할 문제 번호: ")) 


###### 입력 2. 파일명
print("\n")
print("*기존 코드업 문제 정리해둔 파일의 이름 형식 \n*(영어로 입력 + 번호 구분용 언더바) // ex. codeup_")
print("*한글 입력이 지워지지 않는 것은 무시해도 괜찮습니다.")
print("\n")
F_name = input("파일 이름 형식: ") 


###### for문으로 파일 생성 (코드업 기초 100제 마지막 문제: 6098번)
for num in range(F_num, 6099):
    f = open(f"{os.path.dirname(os.path.realpath(__file__))}/{F_name}{num}.py", "w")
    print(f"생성: {num}")