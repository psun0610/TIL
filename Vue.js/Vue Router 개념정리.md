# Vue Router

> vue.js에서 페이지 이동을 위한 라이브러리
>
> url 변경시 DOM을 새로 갱신하지 않고 변경된 영역에 컴포넌트를 갱신함



## 설치방법

vue-router 4 버전 설치

npm: `npm install vue-router@4`

yarn: `yarn add vue-router@4`



## Router 기초

### `<router-link to="경로">`

- 컴파일 시 `<a>` 태그로 변환됨
- `router-link-exact-active` 등 class를 통해 스타일 줄 수 있음



### to 속성

- to 속성의 value 경로로 이동함 (a태그의 href와 비슷함)
- `to="test/path"`: 앞에 슬래시가 없다면 **현재 url에 path가 붙음**
- `to="/test/path"`: 앞에 슬래시를 붙이면 **default url에 붙음**



### `<router-view>`

- vue 파일 내 template에서 사용하는 페이지 표시 태그
- url에 따라 컴포넌트가 화면에 그려짐



## Dynamic Routing

> url path를 동적으로 요청을 받아서 데이터를 넘길 수 있는 라우팅 방식
>
> 파라미터를 전달함
>
> 반대로 해당 파라미터 정보를 가져올 때(역참조?)는 `$route` 객체를 참조

- 동적 segment는 앞에 `:`를 붙임
  - `path='/user_detail/:username/post/:post_id'`
  - path='/user_detail/sunyoung/post/610' 라면 라우팅된 컴포넌트에서
  - `this.route.params.username=='선영'`/ `this.route.params.post_id==77`
- 컴포넌트의 lifecycle hook이 호출되지 않기 때문에 params 변경사항에 반응하기 위해서는 `watch` 옵션으로 `$route`객체의 수정을 감지해야함

```javascript
// router.js
// 만약, url이 '/post/123'라면 :id=123 데이터와 함께 PostItem 컴포넌트로 이동
const router = new VueRouter({
	routes: [{
		path : '/post/:id'
        component : () => import('../views/PostView.vue')
	}]
});
```

```vue
// PostView.vue
// this.$route.params.id로 값을 전달 받을 수 있음
created() {
  getPost('requestPost', this.$route.params.id);
}
```



## Nested Routers

> 라우터 컴포넌트 안에 하위 라우터 컴포넌트를 중첩하여 구성
>
> 라우터 설정에서 **children** 옵션 사용 (Parent-Child)

```javascript
const User = {
  template: `
    <div class="user">
	  <h2>User {{ $route.params.id }}</h2>
	  // id값에 맞는 User의 하위 컴포넌트가 들어옴 
      <router-view></router-view>
    </div>
  `,
}

const routes = [
  {
    path: '/user/:id',
    component: User,
    children: [
      {
        // UserProfile will be rendered inside User's <router-view>
        // when /user/:id/profile is matched
        path: 'profile',
        component: UserProfile,
      },
      {
        // UserPosts will be rendered inside User's <router-view>
        // when /user/:id/posts is matched
        path: 'posts',
        component: UserPosts,
      },
    ],
  },
]
```



## Named Views

> **특정 URL에 여러 컴포넌트들**을 영역별로 지정하여 렌더링
>
> 같은 레벨의 여러 컴포넌트를 동시에 표시하는 방식
>
> 라우터 설정에서 **components** 옵션 사용

```vue
// App.vue
<div id="app">
  <router-view name="appHeader"></router-view>
  <router-view></router-view>
  <router-view name="appFooter"></router-view>
</div>
```

```javascript
// router.js
{
  path: '/home',
  // Named Router
  components: {
    appHeader: AppHeader,
    default: Body,
    appFooter: AppFooter
  }
},
```



## Named Routes

> 특정 URL에 지정된 **1개의 컴포넌트가 여러 개의 하위 컴포넌트**를 갖는 것
>
> router-link의 to 속성에 path 대신 name 지정

```vue
<template>
    <router-link :to="{ name: 'user', params: { username: 'erina' }}">
        User
	</router-link>
</template>
<javascript>
const routes = [
  {
    path: '/user/:username',
    name: 'user',
    component: User
  }
]
</javascript>
```



## Router Transition

> Vue Router에서 기본 제공하는 transition
>
> 다른 페이지로 전환될 때 페이지에 애니메이션이 들어감
>
> **`<transition>` 태그에 name 속성 값**을 기반으로 클래스가 적용됨

- `.[name]-enter`
- `.[name]-enter-active`
- `.[name]-leave-to`
- 등 여러 클래스 있음

``` vue
<template>
  <transition name="fade">
    <router-view class="main"></router-view>
  </transition>
</template>
<style scoped>
/* CSS : Router Transition */
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}

.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>
```



## redirect 옵션

```javascript
// '/a'에서 '/b'로 리디렉션
routes: [{path : '/a', redirect: '/b'}]
// 이름이 있는 라우터의 경우
routes: [{path : '/a', redirect: {name: 'sunyoung'}}]
// 함수를 사용하여 동적 리디렉션 가능 
routes: [{path : '/a', redirect: to => {return '/with-params:id'}}]
```



## props 옵션

> 라우트 컴포넌트에 속성값 전달

컴포넌트에서 `$route`를 사용하게 되면 컴포넌트가 URL에 의존적이게 되어 재사용성이 떨어진다.

이를 해결하기 위하여 `props` 옵션을 사용한다.

```javascript
// $route를 사용하여 의존적인 경우
template: '<div>User {{ $route.params.id }}</div>'

// 의존성 해제하기 위하여 props 옵션 사용
// 1. Boolean mode (props: true / false)
const User = {
 props: ['id'],
 template: '<div>User {{ id }}</div>'
}
{ path: '/user/:id', component: User, props: true }

// 2. Object mode
{ path: '/promotion/from-newsletter', component: Promotion, props: { newsletterPopup: false } }

// 3. Function mode
// props를 반환하는 함수도 만들 수 있습니다.
{ path: '/search', component: SearchUser, props: (route) => ({ query: route.query.q }) }

// named view + Boolean mode
{ path: '/user/:id', components: { default: User, sidebar: Sidebar }, props: { default: true, sidebar: false } }
```

