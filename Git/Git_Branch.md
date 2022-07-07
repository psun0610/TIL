# Git Branch

## Git Flow

> Git을 활용하여 협업하는 흐름 (Branch를 활용하는 전략)
>
> 정해진 답이 있는 것은 아니고 각 프로젝트, 회사에 맞는 흐름으로 변형되어 활용한다

### 대표적인 Git Flow 전략

|            Branch             |                          주요 특징                           |               예시               |
| :---------------------------: | :----------------------------------------------------------: | :------------------------------: |
|         master (main)         |                   배포 가능한 상태의 코드                    |    LOL 클라이언트 라이브 버전    |
|        develop (main)         | feature branch로 나뉘어지거나 발생된 버그 수정 등 개발/ 개발 이후 release branch로 갈라짐 |      다음 패치를 위한 개발       |
| feature branches (supporting) | 기능별 개발 브랜치(topic branch)/ 기능이 반영되거나 드랍되는 경우 삭제 | 신규챔피언 닐라, 드래곤 업데이트 |
| release branches (supporting) | 개발 완료 이후 QA, Test 등을 통해 얻어진 다음 배포 전 이루어져야할 bug fix 반영 (다음 버전을 위함) |         9.24a, 9.24b ...         |
|     hotfixes (supporting)     |      긴급하게 반영 해야하는 bug fix (현재 버전을 위함)       |      긴급 패치를 위한 작업       |

![gitflow-woowahan](Git_Branch.assets/gitflow-woowahan.PNG)

이미지 출처: https://techblog.woowahan.com/2553/



## Branch 기본 명령어

- `(master) $ git branch <branch name>`
  - 브랜치를 생성한다
- `(master) $ git checkout <branch name>`
  - 해당 브랜치로 이동한다
- `(master) $ git checkout -b <branch name>`
  - `-b`옵션을 사용하여 브랜치 생성과 이동을 동시에 한다

- `(master) $ git branch -d <branch name>`
  - 브랜치를 삭제한다
- `(master) $ git branch`
  - 브랜치 목록을 조회한다



## Branch Merge

각 브랜치에서 작업한 이력을 합치려면 merge 명령어를 사용한다.

- ### -fast-forward

  - 기존 master 브랜치에 변경사항이 없어서 단순히 앞으로 이동만 한다.


- ### merge commit

  - 기존 master 브랜치와 병합하길 원하는 브랜치 모두에 변경사항이 있기 때문에 병합 커밋이 발생한다.

- ### *Conflict 발생

  - 기존 master 브랜치와 병합하길 원하는 브랜치에 같은 파일에 대한 수정사항이 있어서 conflict가 발생하며, 이는 수작업으로 해결해야한다.
  - @@@@@@@@@@사람들은 어떻게 해결하는지 구글링해보고 내용추가하기@@@@@@@@@@@@

@@@@@@@@@@@@@@@@@@@@@@@@@@그림 그려보고 삽입하기!!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



## GitHub Flow 기본 원칙

1. master branch는 반드시 배포 가능한 상태여야 한다.
2. feature branch는 각 기능의 의도를 알 수 있도록 작성한다.
3. Commit message는 매우 중요하며, 명확하게 작성한다.
4. Pull Request를 통해 협업을 진행한다.
5. 변경사항을 반영하고 싶다면, master branch에 병합한다.



@@@@@workflow랑 pullrequest 정리하기@@@@@@@@@@@@





## 참고하면 좋은 자료들

- [우아한 형제들 기술블로그 - 우린 GitFlow를 사용하고 있어요](https://techblog.woowahan.com/2553/)

