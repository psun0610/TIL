# Axios, fetch, Ajax

기존 WEB에서 비동기를 요청할 때는 XHR(XML HTTP Request) 객체를 사용하여야 했음

XHR은 요청 상태나 변경을 submit 하려면 Event를 등록해서 변경사항을 받아야 했고 또한 요청 성공, 실패 여부, 상태에 따라 처리하는 로직이 들어가기 때문에 좋지 않았음

이를 보완하기 위해 HTTP 요청에 최적화 되어 있고 상태도 잘 추상화 되어 있는 Axios와 fetch 등의 api들이 생겨나기 시작

&nbsp;

## Axios

node.js와 브라우저를 위한 HTTP 통신 라이브러리

비동기로 HTTP 통신을 가능하게 해주고 promise 객체를 return 해주기 때문에 response 데이터를 다루기 쉬움

외부 라이브러리이므로 설치 및 import 해줘야함

**크로스 브라우징에 신경을 많이 쓴 라이브러리로 브라우저 호환성이 뛰어남**

&nbsp;

### axios 설치

```bash
$ npm install axios
```

&nbsp;

### axios 구현

#### 1번

```javascript
import axios from "axios";

axios ({
    method: 'post',
    url: '/user/1234'
    data: {
    firstName: 'SunYoung',
    lastName: 'Park'
}
});
```

#### 2번

```javascript
import axios from "axios";

let url = "http://localhost:8000/user/"; // 장고 서버 주소

axios.get(url)
.then(function(response){
  console.log(response);
})
.catch(function(response){
  console.log(response);
})
```

&nbsp;

## fetch

ES6부터 JavaScript 내장 라이브러리로 들어옴

axios와 마찬가지로 promise기반이므로 데이터를 다루는데 어렵지 않음

내장 라이브러리기 때문에 import하지 않아도 됨

**내장 라이브러리이므로 사용하는 프레임워크가 안정적이지 않을 때 사용하면 좋음**

&nbsp;

### fetch 구현

```javascript
const url ='http://localhost8000/test`
const option ={
   method:'POST',
   header:{
     'Accept':'application/json',
     'Content-Type':'application/json';charset=UTP-8'
  },
  body:JSON.stringify({
  	name:'sewon',
    	age:20
  })

  fetch(url,options)
  	.then(response => console.log(response))
```

