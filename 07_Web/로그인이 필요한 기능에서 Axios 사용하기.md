# 로그인이 필요한 기능에서 Axios 사용하기

로그인이 필요한 url에서는 그냥 `axios`를 import 받으면 `500 Server Internal Error`이 발생한다.

처음에 axios header에 토큰이 담기는데 이 토큰이 만료되면 로그인이 필요한 곳인 경우 갱신이 되지 않아서 발생하는 오류다.

이를 해결하기 위해서는 다음과 같은 과정이 필요하다.

```javascript
// axios/index.js
import axios from 'axios'
import store from '../store'

const testaxios  = axios.create()

testaxios.interceptors.response.use(
  function (response) {
    // 200대 response를 받아 응답 데이터를 가공하는 작업
    return response
  },
  async (error) => {
    console.log('interceptors 시작')
    const {
      config,
      response: { status }
    } = error
    console.log(error)
    if (status === 403) {
      console.log('403에러')
      if (error.response.data.detail === '이 토큰은 모든 타입의 토큰에 대해 유효하지 않습니다') { // 응답이 영어면 영어로 수정해서 사용한다.
        const originalRequest = config
        const refresh = localStorage.getItem('refresh_token')
        console.log('토큰이 유효하지않음')
        await store.dispatch('refreshtt', { refresh: refresh })
        const newAccessToken = localStorage.getItem('access_token')
        console.log(newAccessToken)
        axios.defaults.headers.common.Authorization = `Bearer ${newAccessToken}`
        originalRequest.headers.Authorization = `Bearer ${newAccessToken}` // 새로운 토큰을 헤더에 담아줌
        // 401로 요청 실패했던 요청 새로운 accessToken으로 재요청
        return axios(originalRequest)
      }
    }
    return Promise.reject(error)
  }
)
export default testaxios

```

만약 header에 token이 있다면 그냥 axios 요청을 보내고, 만약 token이 만료되어 없다면 `refresh token`을 이용하여 새로운 `access token`을 발급한다. 새로 발급된 토큰을 헤더에 담아서 다시 axios 요청을 보낸다.

&nbsp;

```javascript
// views/CreateGameView.vue
// import axios from 'axios'
import axios from '../axios/index'
  methods: {
    insertArticle() {
      if(!this.title || !this.A || !this.B) {
        this.error = "선택지를 모두 채워주세요"
      } else {
        console.log(this.title, this.A, this.B)
        axios.post('http://localhost:8000/articles/', {title: this.title, A: this.A, B: this.B})
      .then(resp => {console.log(resp.data)})
      .then(() => {
        this.$router.push({
          name: 'all-list'
        })
      })
      .catch(error => console.log(error))
      }
    }
  }
}
```

처음에는 line 2처럼 그냥 default axios를 받아와서 post요청을 보냈는데 잘 작동하였다.

하지만 어느 순간부터 작동이 되지 않았는데 방금 위에서 작성한 `axios/index.js`의 `axios`를 import 받아서 사용하였더니 잘 작동하였다. 토큰이 만료되었는데 토큰을 재발급을 받았기 때문이다.

