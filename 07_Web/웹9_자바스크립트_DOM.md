# ✔자바스크립트

> 브라우저 화면을 **동적**으로 만들기 위하여 사용함
>
> 동적으로 콘텐츠를 바꾸고, 멀티미디어를 제어하고, 애니메이션을 추가하는 등을 동작할 수 있음
>
> 브라우저를 조작할 수 있는 유일한 언어



## Vanilla JavaScript

> 프레임워크나 라이브러리가 적용되지 않은 순수한 자바스크립트

- 크로스 브라우징, 간편한 활용 등을 위해 많은 라이브러리가 등장함 (jQuery 등)
- ES6 이후, 다양한 도구의 등장으로 순수 자바스크립트 활용이 증대됨



## 브라우저에서 할 수 있는 일

- DOM 조작
  - 문서(HTML) 조작
- BOM 조작
  - navigator, scree, location, frames, history, XHR
- JavaScript Core (ECMAScript)
  - Data Structure(Object, Array), Conditional Expression, Iteration



# ✔브라우저 API

> 웹 브라우저에 내장된 API로, 현재 컴퓨터 환경에 관한 데이터를 제공하거나 여러가지 유용하고 복잡한 일을 수행함

- BOM (window)
  - console
  - navigator
  - screen
  - location
  - frames
  - history
  - etc...
    - DOM (document)
      - head
      - body
      - title
      - forms
      - links
      - etc...
- Geolocation API
- Canvas API and WebGL API
- Audio and Video API
- etc..

## BOM (Browser Object Model)

> 자바스크립트가 브라우저와 소통하기 위한 모델
>
> 브라우저의 창이나 프레임을 `추상화`해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단 (버튼, URL 입력창, 타이틀 바 등)
>
> `window`객체는 모든 브라우저로부터 지원받음



## DOM (Document Object Model)

> HTML, XML과 같은 문서를 다루기 위한 `문서 프로그래밍 인터페이스`
>
> `문서를 구조화`하고 구조화된 `구성 요소를 하나의 객체로 취급`하여 다루는 논리적 트리 모델
>
> 프로그래밍 언어적 특성을 활용한 조작 가능



## 주요 객체

- `window`: DOM을 표현하는 창 가장 최상위 객체 *(작성시 생략 가능)*
- `document`: 페이지 컨텐츠의 Entry Point 역할을 하며, `<body>` 등과 같은 수많은 다른 요소들을 포함
- `navicator`, `location`, `history`, `screen`



## 파싱 (Parsing)

> 브라우저가 `구문을 분석, 해석`하여 `DOM Tree`로 만드는 과정



# ✔DOM 조작

> Document는 문서 한 장(HTML)에 해당함 이를 조작함



## DOM 객체의 상속 구조

> `EventTarget` => `Node` => `Element`/`Document` => `HTMLElement`

- **EventTarget**
  - `Event Listener`를 가질 수 있는 객체가 구현하는 DOM 인터페이스
- **Node**
  - 여러가지 DOM 타입들이 상속하는 인터페이스
- **Element**
  - Document 안의 모든 객체가 상속하는 가장 범용적인 인터페이스
  - 부모인 `Node`와 그 부모인 `EventTarget`의 속성을 상속
- **Document**
  - 브라우저가 불러온 웹 페이지를 나타냄
  - DOM 트리의 진입점 (entry point) 역할을 수행함
- **HTMLElement**
  - 모든 종류의 HTML 요소
  - 부모 element의 속성 상속



## DOM 조작 순서

1. 선택 (Select)
2. 변경 (Manipulation)



## 1. DOM 선택

### 🤍 선택 관련 메소드

- ✨**`document.querySelector(selector)`**
  - 제공한 CSS selector(선택자)와 일치하는 첫 번째 `element ` 객체 하나를 반환함 (없다면 null 반환)
- ✨**`document.querySelectorAll(selector)`**
  - 제공한 선택자와 일치하는 모든 `element`를 선택함
  - 인자(문자열)로 매칭 할 하나 이상의 selector를 포함하는 유효한 CSS selector를 받음
  - 지정된 셀렉터에 일치하는 **NodeList를 반환**함
- `getElementById(id)`
- `getElementByTagName(name)`
- `getElementByClassName(names)`



#### 📌 querySelector(), querySelectorAll()을 사용하는 이유

> id, class, tag 선택자 등을 모두 사용 가능하므로, 더 구체적이고 유연하게 선택 가능
>
> ex) document.querySelector('#id'), document.querySelectAll('.class')



### 🤍 선택 메소드별 반환 타입

- 단일 element
  - `getElementById()`
  - **`querySelector()`**
- HTMLCollection
  - `getElementsByTagName()`
  - `getElementsByClassName()`
- NodeList
  - **`querySelectorAll()`**



### 🤍 HTMLCollection & NodeList

> 둘 다 배열과 같이 각 항목에 접근하기 위한 index를 제공함 (유사 배열)

- **`HTMLCollection`**

  - name, id, index 속성으로 각 항목에 접근 가능

- **`NodeList`**

  - index로만 각 항목에 접근 가능
  - 단, HTMLCollection과 달리 배열에서 사용하는 `forEach` 메소드 및 다양한 메소드 사용 가능

- 둘 다 **Live Collection**으로 DOM의 변경사항을 실시간으로 반영하지만,

  **querySelectorAll()**에 의해 반환되는 NodeList는 **Static Collection**으로 실시간으로 반영되지 않음



### 🤍 Collection

- **`Live Collection`**
  - 문서가 바뀔 때 DOM의 변경사항을 실시간으로 collection에 반영함
  - ex) HTMLCollection, NodeList
- **`Static Collection (non-live)`**
  - DOM이 변경되어도 collection 내용에는 영향을 주지 않음
  - `querySelectorAll()`의 반환 NodeList만 static collection



## 2. DOM 변경

### 🤍 변경 관련 메소드

#### Creation

- **`document.createElement()`**
  - 작성한 태그 명의 HTML 요소를 생성하여 반환함

#### append DOM

- **`Element.append()`**
  - 특정 부모 `Node`의 자식 `NodeList` 중 마지막 자식 다음에 `Node 객체`나 `DOMString`을 삽입함
  - 여러 개의 `Node`객체, DOMString을 추가할 수 있음
  - 반환 값이 없음
- **`Node.appendChild()`**
  - 한 `Node`를 특정 부모 `Node`의 자식 `NodeList`중 마지막 자식으로 삽입 (`Node`만 추가 가능)
  - 한번에 오직 하나의 `Node`만 추가할 수 있음
  - 만약 주어진 `Node`가 이미 문서에 존재하는 다른 `Node`를 참조한다면 새로운 위치로 이동함



#### 📌 ParentNode.append() vs Node.appendChild()

> `append()`를 사용하면 **`DOMString` 객체**를 추가할 수도 있지만, `.appendChild()`는 **`Node`객체**만 허용함
>
> `append()`는 반환 값이 없지만, `appendChild()`는 **추가된 `Node`객체를 반환**함
>
> `append()`는 **여러 `Node`객체와 문자열**을 추가할 수 있지만, `.appendChild()`는 **하나의 `Node`객체**만 추가할 수 있음



### 🤍 변경 관련 속성 (property)

- **`Node.innerText`**
  - `Node`객체와 그 자손의 텍스트 컨텐츠(DOMString)을 표현함 (해당 요소 내부의 raw text, 사람이 읽을 수 있는 요소만 남김)
  - 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 *최종적으로 스타일링이 적용된 모습으로 표현*
- **`Element.innerHTML`**
  - 요소(element) 내에 포함된 HTML 마크업을 반환함
  - **XSS 공격에 취약**하므로 사용 시 주의할 것❗❗



#### 📌 XSS (Cross-site Scripting)

> 공격자가 입력 요소를 사용하여 웹 사이트 클라이언트 측 코드에 악성 스크립트를 삽입해 공격하는 방법
>
> 피해자(사용자)의 브라우저가 악성 스크립트를 실행하며 공격자가 엑세스 제어를 우회하고 사용자를 가장할 수 있도록 함



## 3. DOM 삭제

### 🤍 삭제 관련 메소드

- **`ChildNode.remove()`**
  - `Node`가 속한 트리에서 해당 `Node`를 제거
- **`Node.removeChild()`**
  - DOM에서 `자식 Node`를 제거하고 제거된 `Node를 반환`함
  - Node는 인자로 들어가는 자식 Node의 부모 Node



## 4. DOM 속성

### 🤍 속성 관련 메소드

- **`Element.setAttribute(name,value)`**
  - 지정된 요소의 값을 설정함
  - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성 추가
- **`Element.getAttribute(attributeName)`**
  - 해당 요소의 지정된 값(문자열)을 반환함
  - 인자(attributeName)는 값을 얻고자 하는 속성의 이름



### 5. 결론

> DOM조작은 **1. 선택**하고 **2. 변경(조작)**한다.
