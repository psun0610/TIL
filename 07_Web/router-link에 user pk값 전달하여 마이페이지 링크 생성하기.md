## router-link에 user pk값 전달하여 마이페이지 링크 생성하기

> nav바에 마이페이지로 가는 router-link 달기



`:pk`를 path에 포함시킨다.

```javascript
// router/index.js
  {
    path: '/userprofile/:pk',
    name: 'UserDetailView',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "UserDetailView" */ '../views/UserDetailView.vue')
  },
```



user의 pk값은 로컬스토리지의 vuex에 담겨있다. 아래 사진의 값에 있는 pk를 빼내려면 JSON으로 파싱이 필요하다.

`localStorage.getItem('키')` 를 사용하여 vuex를 읽어줄 것인데 이를 JSON으로 파싱 후 안에 있는 pk 값을 꺼내면 된다.

![image](https://user-images.githubusercontent.com/97274144/206118598-991d9ae3-e987-4204-bf52-a4beaae74a8b.png)

```javascript
  data () {
    return {
      logincheck: '',
      pk: '',
      userInfo: JSON.parse(localStorage.getItem("vuex")).loginStore.userInfo.pk,
    }
  },
```



data에서 넘겨주는 `userinfo`를 `router-link`의 `params`에 넣어준다.

```html
<!-- component/Navbar.vue -->
<router-link
    :to="{ name: 'UserDetailView', params: { pk: this.userInfo } }"
>
마이페이지
</router-link>
```

