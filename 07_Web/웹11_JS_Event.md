# Event

> 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
>
> **~ 하면 ~ 한다** => 클릭하면, 경고창을 띄운다. => 특정 이벤트가 발생하면, 함수를 등록한다.



##  addEventListener()

> 지정한 이벤트가 대상에 전달될 때마다 호출할 함수를 설정함
>
> 이벤트를 지원하는 모든 객체 (Element, Document, Window 등)을 대상으로 지정 가능



대상에 특정 이벤트가 발생하면, 할 일을 등록한다.

=> target.**addEventListener**(type, listener[, options])

- **`type`**
  - 반응할 이벤트 유형 (대소문자 구분 문자열)
- **`listener`**
  - 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체
  - EventListener 인터페이스 혹은 JS function 객체(콜백 함수)여야 함



```html
<body>
    <button type="button">버튼</button>
    
    <script>
    	const btm = document.querySelector('button');
        btn.addEventListener('click', function (event){
            alert('버튼이 클릭되었습니다.');
            console.log(event)
        })
    </script>
</body>
```



```html
<body>
    <button onclick="alertMessage()">나를 눌러봐!</button>
    <button id="my-button">나를 눌러봐!!</button>
    </button>
    <script>
    	const alertMessage = function () {
            alert('메롱!!!')
        }
        const myButton = document.querySelector('#my-botton')
        myButton.addEventListener('click', alertMessage)
    </script>
</body>
```



