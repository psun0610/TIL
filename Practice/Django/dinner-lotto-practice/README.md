# Django 실습

> 🗓 프로젝트 기간: 2022.09.22 ~ 2022.09.23
>
> 🚩프로젝트 목적: localhost로 서버를 열고 django 사용하는 연습
>
> 🧾 프로젝트 설명: `training`앱에 `lotto/`, `dinner/` url을 요청 받으면 `view`의 `lotto`, `dinner` 메소드가 실행되고, `lotto.html`, `dinner.html`문서로 응답을 보낸다.
>
> 💻사용 기술: python, django, html, css, bootstrap
>
> ⭐ 나의 역할/ 개발 내용: 
>
> 💡 배운 점: django를 처음으로 사용해보는 실습이어서 낯설었지만 template 안에서 반복문과 조건문을 쓰는 연습을 할 수 있어서 좋았고, 웹의 흐름을 알 수 있었다. (클라이언트가 URL로 요청을 하면 VIEW에서 처리를 하고 문서로 응답하는 흐름!)

 &nbsp;

## Lotto 번호 추천

`view`에서 난수를 생성하여 `lotto.html`에 보내면 난수를 받아서 다음과 같은 화면을 그린다.

지난 주 로또 당첨 번호와 비교해서 등수를 매기고, 당첨 번호와 같은 공만 다른 색으로 나타낸다.

1부터 10까지는 노란색, 11부터 20까지는 파란색 등, 수에 따라 공의 색을 다르게 한다.

![로또추천번호생성기](https://raw.githubusercontent.com/psun0610/Image-upload/image/img/로또추천번호생성기.gif)

&nbsp;

## 저녁 메뉴 추천

`dinner` url을 누르면 떡볶이, 닭발, 삼겹살, 연어 초밥 등 여러 음식 중에서 랜덤으로 메뉴를 보여준다.

메뉴의 이름에 맞는 이미지 src 주소로 사진도 함께 보여준다.

![저메추](https://raw.githubusercontent.com/psun0610/Image-upload/image/img/저메추.gif)