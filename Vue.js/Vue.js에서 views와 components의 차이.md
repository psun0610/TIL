# Vue.js에서 views와 components의 차이

vue 프로젝트 구성에는 `views` 폴더와 `components` 폴더가 있다.

두 폴더 아래에는 모두 `vue` 파일이 위치한다.

`rounter/index.js` 를 보면 다음과 같이 path별로 component를 명시해준다.

```javascript
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

```

이때 router의 component에 명시된 vue 파일은 `views`폴더 아래에 위치하고, `views` 폴더 속 vue 파일 내부에서 component로 호출하는 vue 파일은 `component` 폴더 아래에 위치시키면 된다.

사실 폴더 구조는 어떻게 하든 상관없지만 위는 `vue-cli`가 제시하는 통상적인 사용법이라고 한다.