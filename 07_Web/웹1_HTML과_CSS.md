# ✔웹 사이트

## 웹 사이트의 구성 요소

- HTML: 구조
- CSS: 표현
- Javascript: 동작



## 웹 표준

> 웹 사이트는 브라우저를 통해 동작하는데, 브라우저마다 동작이 조금씩 달라서 문제가 생기는 경우가 많다.
>
> 이에 대한 해결책으로 웹 표준이 등장했다.

> 웹에서 표준적으로 사용되는 기술이나 규칙
>
> 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함 (크로스 브라우징)



# ✔HTML

> 웹 페이지를 작성(구조화)하기 위한 언어
>
> Hyper Text Markup Language

- Hyper Text: 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
- Markup Language: 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어, ex) HTML, Markdown..



## HTML 기본 구조

- html: 문서의 최상위(root) 요소
- head: 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
- body: 문서 본문 요소
  - 실제 화면 구성과 관련된 내용

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
        
</body>
</html>
```



### head 예시

- `<title>` : 브라우저 상단 타이틀
- `<meta>`: 문서 레벨 메타데이터 요소
- `<link>`: 외부 리소스 연결 요소 (CSS파일, favicon 등)
- `<script>`: 스크립트 요소 (JavaScript 파일/ 코드)
- `<style>`: CSS 직접 작성

```html
<head>
	<title>HTML 수업</title>
	<meta charset="UTF-8">
	<link href="style.css" rel="stylesheet">
	<script src="javascript.js"></script>
	<style>
		p {
			color: black;
		}
	</style>
</head>
```

### Open Graph Protocol

> 메타데이터를 표현하는 새로운 규약

- HTML 문서의 메타데이터를 통해 문서의 정보를 전달
- 메타데이터에 해당하는 제목, 설명 등을 쓸 수 있도록 정의

```
[메타 데이터란?]
데이터에 대한 데이터
예를 들어서 사진 데이터가 있다면, 이 사진을 찍은 위치, 조리개 값, 사진을 찍은 시간 등의 데이터를 뜻한다.
```



## HTML의 요소

> HTML의 요소는 시작 태그와 종료 태그, 내용(contents)으로 구성되고 그 정보의 성격과 의미를 정의함
>
> 내용이 없는 태그들도 존재함 (닫는 태그가 없음)	ex) br, hr, img, input, link, meta
>
> 요소는 중첩될 수 있고 중첩을 통해 하나의 문서를 구조화함
>
> 여는 태그와 닫는 태그의 쌍을 잘 확인해야 함!

```html
<h1> contents </h1>
```



## 속성(attribute)

> 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
>
> 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공함
>
> 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재함
>
> 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)도 있음

```html
<a href="https://google.com"></a>
```

- 태그 별로 사용할 수 있는 속성은 다름

- 공백 사용 X, 쌍 따옴표 사용하기



## HTML Global Attribute

> 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성

- `id`: 문서 전체에서 유일한 고유 식별자 지정
- `class`: 공백으로 구분된 해당 요소의 클래스의 목록 (CSS, JS에서 요소를 선택하거나 접근함)
- `data-*`: 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용함
- `style`: inline 스타일
- `title`: 요소에 대한 추가 정보 지정
- `tabindex`: 요소의 탭 순서



## 렌더링

> 웹사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정



## DOM 트리 (Document Object Model)

> 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
>
> HTML 문서에 대한 모델을 구성하고 HTML 문서 내의 각 요소에 접근하여 수정에 필요한 프로퍼티와 메소드를 제공함



## 인라인 요소/ 블록 요소

- 인라인 요소: 글자처럼 취급
- 블록 요소: 한 줄 모두 사용



## 텍스트 요소

- `<a></a>`: href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성
- `<b></b>`: 볼드체 (굵은 글씨)
- `<strong></strong>`: 중요한 강조하고자 하는 요소를 굵은 글씨로 표현
- `<i></i>`: 이탤릭체 (기울임 글씨)
- `<em></em>`: 중요한 강조하고자 하는 요소를 기울임 글씨로 표현
- `<br>`: 텍스트 내에 줄 바꿈 생성
- `<img>`: src 속성을 활용하여 이미지를 표현하고, alt 속성을 활용하여 대체 텍스트
- `<span></span>`: 인라인 컨테이너



## 그룹 요소

- `<p></p>`: 하나의 문단 (paragraph)
- `<hr>`: 수평선, 문단 레벨 요소에서의 주제의 분리
- `<ol></ol>`: 순서가 있는 리스트 (ordered list)
- `<ul></ul>`: 순서가 없는 리스트 (unordered list)
- `<pre></pre>`: 작성한 내용을 그대로 표현(고정폭 글꼴이 사용되고 공백 문자를 유지함)
- `<blockquote></blockquote>`: 텍스트가 긴 인용문, 주로 들여쓰기를 한 것으로 표현됨
- `<div></div>`: 블록 컨테이너



# ✔CSS 기초

> Cascading Style Sheets, 스타일을 지정하기 위한 언어

## CSS 정의 방법

1. 인라인(inline)
2. 내부 참조(embedding) - `<style>`
3. 외부 참조(link file) - 분리된 CSS 파일



### 1) 인라인으로 CSS 정의

> 해당 태그에 직접 style 속성 활용

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>
<body>
	<h1 style="color: blue; font-size: 100px;">Hello</h1>
</body>
</html>
```



### 2) 내부 참조로 CSS 정의

> `<head>` 태그 내에 `<style>`에 지정

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        h1 {
            color: blue;
            font-size: 100px;
        }
    </style>
</head>
<body>
</body>
</html>
```



### 3) 외부 참조로 CSS 정의

> 외부 CSS 파일을 `<head>`내 `<link>`를 통해 불러오기

- CSS 파일

```css
<--mystyle.css-->
h1 {
    color: blue;
    font-size: 100px;
}
```

- HTML 파일

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
    <link rel="stylesheet" href="mystyle.css"
	<title>Document</title>
</head>
<body>
	<h1>Hello</h1>
</body>
</html>
```



## CSS 기초 선택자

> **아이디 선택자 > 클래스 선택자 > 요소 선택자** 순으로 선택됨

- 요소 선택자
  - HTML 태그를 직접 선택
- 클래스(class) 선택자
  - `.`마침표로 시작함
  - 해당 클래스가 적용된 항목을 선택
- 아이디(id) 선택자
  - `#`문자로 시작하고, 해당 아이디가 적용된 항목을 선택
  - 일반적으로 *하나의 문서에 1번만 사용*
  - 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장함



## CSS with 개발자 도구

- `styles`: 해당 요소에 선언된 모든 CSS
- `computed`: 해당 요소에 최종 계산된 CSS



# ✔참고 자료

- [MDN: HTMI 문서](https://developer.mozilla.org/ko/docs/Web/HTML)

- [MDN: CSS 문서](https://developer.mozilla.org/ko/docs/Web/CSS)

- [네이버 온라인 웹 접근성 체험](https://nax.naver.com/index)



# ✔태그별 정리

- `<head></head>`
  - 메타데이터를 담음 (제목, 스크립트, 스타일 시트)
- `<title></title>`
  - 브라우저의 제목 표시줄이나 페이지 탭에 보이는 문서 제목을 정의함
  - 텍스트만 포함할 수 있음
  - `<head>`태그 안에서 사용해야 함

- `<body></body>`

  - HTML 문서의 내용을 나타냄
  - 한 문서에 하나만 존재할 수 있음

- `<footer></footer>`

  - 일반적으로 구획의 작성자, 저작권 정보, 관련 문서 등의 내용을 담는다.

- `<article></article>`

  - 문서, 페이지, 애플리케이션, 사이트 안에서 독립적으로 구분해 재사용할 수 있는 구획
  - 게시판, 블로그 글, 매거진, 뉴스 기사 등

- `<section></section>`

  - HTML문서의 독립적인 구획을 나타냄
  - 딱히 적합한 의미를 가진 요소가 없는데 구획을 나눌 때 사용함

- `<aside></aside>`

  - 문서의 주요 내용과 간접적으로 연관된 부분을 나타냄
  - 주로 사이드바 혹은 콜아웃 박스로 표현함

- `<p></p>`

  - 문단을 나타냄

- `<div></div>`

  - 혼자는 아무것도 표현하지 않음
  - class나 id 속성으로 꾸미기 쉽도록 돕거나, 문서의 특정 구역이 다른 언어임을 표시하는 등의 용도로 사용할 수 있음
  - `<article>`이나 `<nav>`등의 의미를 가진 다른 요소가 적절하지 않을 때만 사용해야 함
  - **블록 요소**임

- `<span></span>`

  - 혼자는 아무것도 표현하지 않음
  - div와 매우 유사하게 CSS로 스타일을 적용하는 등으로 사용함
  - **인라인 요소**임

- `<ul></ul>`

  - 순서가 없는 정렬되지 않은 리스트 표현

  - `<li>`로 목록의 항목을 나타냄

  - ```html
    <ul>
        <li>first item</li>
        <li>second item
        	<ul>
                <li>item1</li>
            	<li>item2</li>
        	</ul>
        </li>
        <li>third item</li>
    </ul>
    ```

- `<ol></ol>`

  - 순서가 있는 정렬된 리스트 표현

  - ```html
    <ol>
        <li>first item</li>
        <li>second item
        	<ol>
                <li>item1</li>
            	<li>item2</li>
        	</ol>
        </li>
        <li>third item</li>
    </ol>
    ```

- `<img src="~.jpg">`

  - 문서에 이미지를 넣음
  - `src`속성은 필수이며 이미지의 경로를 지정함
  - `alt`속성은 이미지의 텍스트 설명이며 필수는 아니지만 **접근성 차원에서 매우 유용**함 (스크린 리더가 `alt`의 값을 읽어 사용자에게 이미지를 설명하기 때문)
  - `alt`속성은 또한 이미지를 표시할 수 없는 경우에도 이 속성 값을 대신 보여줌
  - 닫는 태그 X

- `<audio></audio>`

  - 문서에 소리 콘텐츠를 포함할 때 사용
  - `src`속성 또는 `<source>`요소를 사용하여 한 개 이상의 오디오 소스를 지정할 수 있음
  - 다수를 지정한 경우 가장 적절한 소스를 브라우저가 고름
  - 태그 안의 컨텐츠는 오디오가 지원되지 않을 때 보여짐

- `<video></video>`

  - 영상 삽입
  - 태그 안의 컨텐츠는 비디오가 지원되지 않을 때 보여짐

- `<canvas> 캔버스 내용 설명하는 대체 텍스트 </canvas>`

  - `canvas api`와 함께 사용하여 그래픽과 애니메이션을 그릴 수 있음

- `<datalist></datalist>`

  - 다른 컨트롤에서 고를 수 있는 선택지를 나타내는 여러 `<option>`요소를 담음

  - ```html
    <label for="myBrowser">아래 목록에서 브라우저를 선택하세요:</label>
    <input list="browsers" id="myBrowser" name="myBrowser" />
    <datalist id="browsers">
      <option value="Chrome">
      <option value="Internet Explorer">
    </datalist>
    ```

- `<details></details>`

  - "열림" 상태일 때 내부 정보를 보여주는 위젯을 생성함
  - 레이블 옆의 작은 삼각형이 돌아가면서 열림/닫힘 상태를 나타냄
  - 요약이나 레이블(제목)은 `<summary>`요소를 통해 제공함, `<summay>`의 콘텐츠를 위젯의 레이블로 사용함
  - `<summary>`를 사용하지 않으면 레이블이 그냥 'details'로 표현됨 (브라우저 기본 설정이 표시됨)

- `<pogress></progress>`

  - 작업의 완료 정도를 나타내고 진행 표시줄 형태임

- `<embed>`

  - 외부 컨텐츠를 나타냄

- `<nav></nav>`

  - 현재 페이지 내, 또는 다른 페이지로의 링크를 보여주는 구획
  - 메뉴, 목차 색인 등에 주로 쓰임

- `<form></form>`

  - 정보를 제출하기 위한 구획, 폼

- `<input>`

  - 사용자의 데이터를 받을 수 있는 대화형 컨트롤 생성
  - `type`으로 button, checkbox, date, radio 등이 가능함
  - 속성이 매우 매우 많음

- `<output>`

  - `<input>`에 대한 결과값을 나타냄
