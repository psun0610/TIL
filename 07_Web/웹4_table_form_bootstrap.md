# ✔table

> 표를 만들기 위한 태그

|  ID  |  이름  |      전공      |
| :--: | :----: | :------------: |
|  1   | 박선영 | 소프트웨어학과 |
|  2   | 신짱구 |   스포츠학과   |
|  3   | 김철수 |    경영학과    |
| 총계 |        |      3명       |

<center>1반 학생 명단</center>

## table 태그 사용법

- table의 각 영역을 명시하기 위해 `<thead>` `<tbody>` `<tfoot>` 요소 활용

- `<tr>`은 가로 줄 (table row), 내부에는 `<th>` 혹은 `<td>`로 셀 구성함

- `colspan`, `rowspan` 속성을 활용하여 셀을 병합함

- `<caption>`을 통해 표 설명 또는 제목을 나타냄



## 코드 보기

```html
  <table>
    <thead>
      <tr>
        <th>ID</th>
        <th>이름</th>
        <th>전공</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>1</td>
        <td>박선영</td>
        <td>소프트웨어학과</td>
      </tr>
      <tr>
        <td>2</td>
        <td>신짱구</td>
        <td>스포츠학과</td>
      </tr>
      <tr>
        <td>3</td>
        <td>김철수</td>
        <td>경영학과</td>
      </tr>
    </tbody>
    <tfoot>
      <tr>
        <td>총계</td>
        <!--colspan 속성으로 셀 병합-->
        <td colspan="2">2명</td>
      </tr>
    </tfoot>
    <!--caption 태그를 통해 표 설명 또는 제목 나타냄-->
    <caption>1반 학생 명단</caption>
  </table>
```



# ✔form

> 정보(데이트)를 서버에 제출하기 위해 사용하는 태그

```html
<form action="/search" method="GET">
    
</form>
```



## form 기본 속성

- `action`: form을 처리할 서버의 URL (데이터를 보낼 곳)
- `method`: form을 제출할 때 사용할 HTTP 메소드 (GET 혹은 POST)
- `enctype`: method가 POST인 경우 데이터의 유형



## ◻ input

> 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
>
> value(값)이 name(이름)으로 매핑되어 서버에 전송됨

```html
<form action="/search" method="GET">
  <input type="text" name="q">
</form>
```

- 만약 구글창에 HTML을 검색하면 주소창은 `https://www.google.com/search?q=HTML`이 된다.



### input 대표적인 속성

- `name`: form control에 적용되는 이름 (이름/값 페어로 전송됨)
- `value`: form control에 적용되는 값 (이름/값 페어로 전송됨)
- `required`, `readonly`, `autofocus`, `autocomplete`, `disabled` 등



### input 타입

- 일반

  - *타입별로 HTML 기본 검증 혹은 추가 속성을 활용할 수 있음*
  - `text`: 일반 텍스트 입력

  - `password`: 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현

  - `email`: 이메일 형식이 아닌 경우 form 제출 불가

  - `number`: min, max, step 속성을 활용하여 숫자 범위 설정 가능

  - `file`: accept 속성을 활용하여 파일 타입 지정 가능

- 항목 중 선택

  - *일반적으로 `label`태그와 함께 사용하여 선택 항목 작성*
  - **동일 항목에 대하여는 `name`을 지정하고, 선택된 각 항목에 대한 `value`를 지정함**
  - `checkbox`: 다중 선택
  - `radio`: 단일 선택

- 기타

  - *다양한 종류의 `input`을 위한 `picker`를 제공*
  - `color`: color picker
  - `date`: date picker
  - *`hidden input`을 사용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값 설정*
  - `hidden`: 사용자에게 보이지 않는 input



## ◻ input label

> `label`을 클릭하여 `input` 자체의 초점을 맞추거나 활성화 시킬 수 있음
>
> => 사용자가 선택할 수 있는 영역이 늘어나 웹/모바일(터치) 환경에서 편하게 사용할 수 있음
>
> => `label`과 `input` 입력의 관계는 시각적인 효과 뿐만 아니라 화면리더기에서도 `label`을 읽어 쉽게 내용을 확인 할 수 있도록 함

- `<input>`에는 `id속성`을, `<label>`에는 `for속성`을 활용하여 상호 연관 시킴



## 코드 보기

```html
  <form action="">
      
    <!--autofocus, label 확인-->
    <div class="input-group">
      <label for="username">아이디</label>
    </div>
    <input type="text" name="username" id="username" autofocus>
	
    <!--disabled, value 확인-->
    <div class="input-group">
      <label for="name">이름</label>
    </div>
    <input type="text" name="name" value="홍길동" id="name" disabled>

    <!--label 확인-->
    <div class="input-group">
      <label for="agreement">개인정보 수집에 동의합니다.</label>
    </div>
    <input type="checkbox" name="agreement" id="agreement">

    <div class="input-group">
      <!--label에 for, input에 id 속성을 안 줘서 연결이 안됨-->
      <label>최종 제출을 확인합니다.</label>
    </div>
    <input type="checkbox">
  </form>
  <input type="submit" value="제출">
```



# ✔Bootstrap

> 반응형 웹 개발을 더 빠르게 할 수 있도록 도와주는 프레임워크

[부트스트랩 공식문서](https://getbootstrap.com/docs/5.2/getting-started/introduction/)

## CDN

> Content Delivery(distribution) Network
>
> 컨텐츠를 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템
>
> 개별 유저의 가까운 서버를 통해 빠르게 전달 가능, 외부 서버를 활용함으로써 본인 서버의 부하가 적어짐



## 사용하기

> `head`에 다음을 추가함

- CSS only

  ```html
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
  ```

- JavaScript Bundle with Popper

  ```html
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.5/dist/umd/popper.min.js" integrity="sha384-Xe+8cL9oJa6tN/veChSP7q+mnSPaj5Bcu9mPX5F5xIGE0DVittaqT5lorf0EI7Vk" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.min.js" integrity="sha384-ODmDIVzN+pFdexxHEHFBQH3/9/vQ9uori45z4JjnFsRydbmQbmL5t1tQ0culUzyK" crossorigin="anonymous"></script>
  ```



## spaing (Margin and padding)

> 부트스트랩 css 사용해서 마진과 패딩 조절하기

`{property}{sides}-{size}`

=> `mt-3`

```html
<div class="mt-3 ms-5">bootstrap-spacing</div>
```

- `{property}`
  - `m`: for classes that set **margin**
  - `p`: for classes that set **padding**
- `{sides}`
  - `t`: for classes that set **margin-top** or **padding-top**
  - `b`: for classes that set **margin-bottom** or **padding-bottom**
  - `s`(start): for classes that set **margin-left** or **padding-left** in LTR, **margin-right** or **padding-right** in RTL
  - `e`(end): for classes that set **margin-right** or **padding-right** in LTR, **margin-left** or **padding-left** in RTL
  - `x`: for classes that set both ***-left** and ***-right**
  - `y`: for classes that set both ***-top** and ***-bottom**
  - `blank`: for classes that set a **margin** or **padding** on all 4 sides of the element
- `{size}`
  - `0`: margin or padding by setting it to 0
  - `1`: margin or padding to **&spacer * .25**
  - `2`: margin or padding to **&spacer * .5**
  - `3`: margin or padding to **&spacer** (1rem)
  - `4`: margin or padding to **&spacer * 1.5**
  - `5`: margin or padding to **&spacer * 3**
  - `auto`: for classes that set the margin to auto

