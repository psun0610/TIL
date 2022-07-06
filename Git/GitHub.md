# GitHub

## [GitHub](https://github.com/)란?

![github](GitHub.assets/github.png)

Git이 분산 버전 관리 시스템이라면 GitHub는 이러한 Git을 사용하는 프로젝트를 지원하는 웹호스팅 서비스(**원격 저장소**)다.

GitHub를 사용하여 버전관리와 협업을 더 효율적으로 할 수 있다.



## 원격저장소 (Remote Repository) 기본 흐름

- `$ git push` 명령을 통해 로컬 저장소의 commit(버전)을 원격 저장소로 보낸다.
- `$ git pull`명령을 통해 원격 저장소의 commit(버전)을 로컬 저장소로 가져온다.



## GitHub 기본 명령어

- `$ git remote add <원격저장소> <URL>`

  깃아 원격저장소 추가해줘 오리진이라는 이름으로 URL을

- `$ git push <원격저장소> <브랜치>`

  origin이라는 원격저장소의 master 브랜치에 commit(버전)을 올림

- `$ git pull <원격저장소> <브랜치>`

  origin 원격저장소의 master 브랜치에서 변경된 내역을 로컬저장소로 받아옴

- `$git clone <url>`

  로컬저장소가 없는데 원격저장소의 버전들을 가져오고 싶을 때

  원격저장소 복제

- `$ git remote -v`

  원격저장소 정보 확인

- `$ git remote rm <원격저장소>`

  원격저장소 삭제

  

## 로컬 저장소의 버전을 원격 저장소에 보내고 받기

1. GitHub에서 New repository를 생성한다.

   - 생성된 레포지토리의 주소: https://github.com/GitHub_Username/저장소이름.git

   

2. git bash에 `$ git remote add <원격저장소> URL.git`을 입력한다.

   - `$ git remote add origin URL.git`
   - => 깃아 원격 저장소 추가해줘 오리진이라는 이름으로 URL을!

   

3. `$ git push <원격저장소> <브랜치>`을 입력하여 origin의 master 브랜치에 변경 사항을 올린다.

   - 만약 원격저장소에 처음 commit을 올린다면 로그인 창에 로그인 하면 된다.

   - 로컬 폴더의 파일, 폴더가 아니라 저장소에 commit 했던 버전들이 올라감!

   - 만약 `$ git push -u <원격저장소> <브랜치>`로 `-u 옵션`을 줘서 명령하면 다음에 `$ git push`||`$ git pull`만 입력하여도 자동으로 master 브랜치와 origin 원격 저장소에 연결하여 줘서 간단하게 사용가능하다.

     

4. `$ git pull <원격저장소> <브랜치>`을 입력하여 변경 사항을 받아온다.
