# 신문의 헤드라인을 편집하기 위해, 주어지는 문자열의 알파벳 소문자를 모두 대문자로 바꾸는 프로그램을 개발 중이다.

# 입력으로 주어진 문장에 모든 소문자 알파벳을 찾아 대문자로 변환한 다음, 그 결과를 출력하는 프로그램을 작성하라.


# [예제 풀이]
# The_headline_is_the_text_indicating_the_nature_of_the_article_below_it.
# 위와 같은 문자열이 입력으로 주어졌을 때, 출력은 다음과 같다.
# THE_HEADLINE_IS_THE_TEXT_INDICATING_THE_NATURE_OF_THE_ARTICLE_BELOW_IT.

# [제약 사항]
# 문자열의 최대 길이는 80 bytes 이다.

# [입력]
# 입력으로 80 bytes 이하의 길이를 가진 문자열이 주어진다.

# [출력]
# 문자열의 소문자를 모두 대문자로 변경한 결과를 출력한다.

mystr = input()
print(mystr.upper())