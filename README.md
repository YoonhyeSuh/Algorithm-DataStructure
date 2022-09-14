# :sunglasses:알고리즘과 자료구조를 부수고싶은 DC&amp;M 
<br>

<B> 일정 : 2022.09.05 ~ 2022.12.23 </B><br>

<B>[알고리즘 스터디] Git Branch Protection Rule 적용 안내</B><br>
Branch Protection 이란? Branch를 보호하기 위한, 깃에서 제공하는 보호 장치입니다. 여러 사람들이 동시에 같은 코드 베이스에서 작업을 하다 보면 여러 가지 문제가 생길 수 있습니다. 허락받지 않은 사람이 무질서하게 코드를 작성하고 머지 하는 경우도 발생하고, 설령 허락을 받은 멤버가 코드를 작성하고 머지 하더라도 그 코드가 테스팅을 거치지 않은 문제가 많은? 코드 일 수도 있습니다.
실례로 제가 프로젝트를 진행하였을 때도, 자기 짠 코드는 틀릴 일이 없다고 자신만만하게 말씀하시던 분 코드를 머지 한 이후에 크게 문제가 발생한 경우도 있었습니다. 추후에 테스팅에 대한 중요성을 설명드리겠지만, 머지 한 이후 문제가 발생한 경우 여러분들이 작업하는 프로젝트 혹은 서비스가 크게 망가질 수도 있습니다. 그렇기에 깃허브에서는 Pull Request(Pr)라는 작업으로 코드를 머지 할 때, 리뷰를 받을 수 있는 장치를 제공하고 있습니다.

동아리에서 진행하는 알고리즘 스터디 방식은 이러한 리뷰 시스템을 이용한 것입니다.

현재 Branch Protection에서는 **2명**에게 Approve를 받지 못하면 Merge가 되지 못하도록 막아 놓았습니다.
<br><br>
## :zap:목차
* [링크](#iphone링크)
* [멤버](#four_leaf_clover멤버)
* [스케쥴](#alarm_clock스케쥴)
* [자료구조 및 알고리즘 목차](#book자료구조-및-알고리즘-목차)
* [규칙 및 주의사항](#muscle규칙-및-주의사항)
* [사용법](#question사용법)

## :iphone:링크
* <B>다운로드</B>
  + <a href = "https://git-scm.com/download/win">Git(필수)</a>
    - 설치법: [for Windows](https://github.com/HSU-DCnM-Study/Algorithm-DataStructure/blob/main/resource/git설치법/git설치법%20for%20Windows.pdf) / [for Mac](https://github.com/HSU-DCnM-Study/Algorithm-DataStructure/blob/main/resource/git설치법/git설치법%20for%20Mac.pdf)
  + <a href = "https://desktop.github.com">GitHubDeskTop(필수)</a>
* <b>코딩테스트 사이트</b>
  + <a href = "https://www.acmicpc.net">백준알고리즘(필수)</a><br>
  + <a href = "https://school.programmers.co.kr/learn/challenges">프로그래머스</a><br>
  + <a href = "https://swexpertacademy.com/main/main.do">삼성SwExpertAcademy</a><br>
* <b>참고자료</b>
  + <a href = "https://wikidocs.net/book/1">파이썬</a><br>
  + <a href = "https://github.com/ndb796/python-for-coding-test">이것이 코딩테스트다.gitCode</a><br>
  + <a href = "https://www.youtube.com/watch?v=m-9pAwq1o3w&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC">이것이 코딩테스트다 무료강의</a><br>
  + <a href = "https://github.com/onlybooks/algorithm-interview">파이썬 알고리즘 인터뷰 문제풀이</a><br>

_[목차로 이동](#zap목차)_

## :four_leaf_clover:멤버
**19기**
| <a href="https://github.com/jeinie"><img src="https://avatars.githubusercontent.com/u/68533847?v=4" width="90" height="90"></a> | X | <a href="https://github.com/jueun0725"><img src="https://avatars.githubusercontent.com/u/82727761?v=4" width="90" height="90"></a> | <a href="https://github.com/newJunsung"><img src="https://avatars.githubusercontent.com/u/107932188?v=4" width="90" height="90"></a> |
| ----- | ----- | ----- | ----- |
| [장정윤](https://github.com/jeinie) | X | [김주은](https://github.com/jueun0725) | [김준성](https://github.com/newJunsung) |

**20기**
| <a href="https://github.com/ois0886"><img src="https://avatars.githubusercontent.com/u/58154638?v=4" width="90" height="90"></a> | <a href="https://github.com/YJMINT"><img src="https://avatars.githubusercontent.com/u/105741144?v=4" width="90" height="90"></a> | <a href="https://github.com/S-DPR"><img src="https://avatars.githubusercontent.com/u/108619579?v=4" width="90" height="90"></a> | <a href="https://github.com/YoonhyeSuh"><img src="https://avatars.githubusercontent.com/u/106311524?v=4" width="90" height="90"></a> | <a href="https://github.com/juniii99"><img src="https://avatars.githubusercontent.com/u/112378363?v=4" width="90" height="90"></a> | <a href="https://github.com/ubin0318"><img src="https://avatars.githubusercontent.com/u/109210958?v=4" width="90" height="90"></a> |
| ----- | ----- | ----- | ----- | ----- | ----- |
| [오인성](https://github.com/ois0886) | [정윤주](https://github.com/YJMINT) | [추영광](https://github.com/S-DPR) | [서윤혜](https://github.com/YoonhyeSuh) | [박준이](https://github.com/juniii99) | [신유빈](https://github.com/ubin0318) |

**21기**
| <a href="https://github.com/isnonyou"><img src="https://avatars.githubusercontent.com/u/109057475?v=4" width="90" height="90"></a> | <a href="https://github.com/krevlin"><img src="https://avatars.githubusercontent.com/u/109061978?v=4" width="90" height="90"></a> |
| ----- | ----- |
| [이서원](https://github.com/isnonyou) | [권영현](https://github.com/krevlin) |

_[목차로 이동](#zap목차)_

## :alarm_clock:스케쥴
<B>TODO : 논의 필요</B>

_[목차로 이동](#zap목차)_

## :book:자료구조 및 알고리즘 목차
feat. 참고 자료 : C언어로 쉽게 풀어쓴 자료구조, 이것이 코딩테스트다, 파이썬 알고리즘 인터뷰
1. <a href= "https://velog.io/@cha-suyeon/Algorithm-%EC%8B%9C%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84-%EA%B3%B5%EA%B0%84-%EB%B3%B5%EC%9E%A1%EB%8F%84">시간복잡도, 공간복잡도</a><br>
2. 문자열, 수학, 구현
3. <a href = "https://www.secmem.org/blog/2021/07/09/recursion/">재귀</a><br>
4. <a href = "https://yjg-lab.tistory.com/118">단순 연결리스트</a> ,<a href = "https://yjg-lab.tistory.com/120?category=932096">원형 연결리스트</a> ,<a href = "https://yjg-lab.tistory.com/122?category=932096">양방향 연결리스트</a><br>
5. <a href = "https://velog.io/@falling_star3/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9DStack%ED%81%90Queue%EB%8D%B1Deque"> 스택, 큐, 덱 </a><br>
6. <a href = "https://gmlwjd9405.github.io/2018/08/12/data-structure-tree.html">트리</a><br>
7. <a href = "https://suyeon96.tistory.com/31">우선순위 큐, 힙</a><br>
8. <a href = "https://gmlwjd9405.github.io/2018/08/13/data-structure-graph.html">그래프(DFS,BFS)</a><br>
9. 해시테이블
10. 정렬
11. 다이나믹(동적 계획법)
12. 그리디
13. 이진탐색
14. 최단 경로

_[목차로 이동](#zap목차)_

## :muscle:규칙 및 주의사항
1. 오른쪽 상단에 현 Repository를 Fork하여 자신의 깃 저장소로 가져간다.
2. 자신의 깃 Repogitory에 가져온 것을 확인한 후 git 주소를 복사하여, git Bash 혹은 Cmd를 이용하여 자신이 원하는 파일에 git clone!!
3. 백준알고리즘사이트 혹은 그와 비슷한 알고리즘 사이트에서 일주일에 1~3 문제를 푼다. <br>
4. Commit Message는 최대한 구체적으로 ex) 백준알고리즘 1715번 카드 정렬하기, 프로그래머스 Lv5 방의갯수 <br>
자신이 공부한 자료는 ex) 자료구조 연결리스트
5. 문제에 대한 자유로운 질문과 회고는 스터디 시간에 공유한다.
6. 언어는 Python, Java, C, C++, Kotlin, JavaScript, Swift 자유롭게 사용가능 단, Ruby같은 건 관리자들이 못 봄. TODO: 논의필요
7. 열심히 풀고 Commit -> Push -> PR -> Comment작성 -> ReviewRequest -> 3명이상에게 Approve 받기 -> Merge
자세한 설명은 아래 참고
8. Review 및 Comment에는 경어체, 평어체 아무거나 사용해도 되나, 욕설과 비속어는 금지<br>
왜? Repository가 Private가 아니라 Public임 일반 사람들도 볼 수 있음.
9. 다른이의 폴더를 참고하여 볼 수 있으나 허락없이 수정하지 말 것
10. Branch Protection을 사용하여, Reviewer 3명 이상에게 Approve를 받지 못하면 Merge가 안됨

_[목차로 이동](#zap목차)_

## :question:사용법
![1](https://user-images.githubusercontent.com/58154638/184289798-73195cb5-3d9d-4fdb-a5f2-dc6e87120063.jpg)
<B>1. HSU-DCnM-Study/Algorithm-DataStructure에 들어와서 오른쪽 상단에 Fork 클릭 </B><br>
<br>
![2](https://user-images.githubusercontent.com/58154638/184289805-4a2c034b-f3da-4643-98b2-21a478d9db5f.jpg)
<B>2. Repository 이름을 확인 후에 Create 클릭 </B><br>
<br>
![3](https://user-images.githubusercontent.com/58154638/184289810-943047c5-8446-4a54-8270-7cb45920c2a9.jpg)
<B>3. 내 프로필로 돌아와서 맨위에 내 Repository 확인 </B><br>
<br>
![4](https://user-images.githubusercontent.com/58154638/184289815-c0f488bf-c57d-438b-a2e4-7952d180bada.jpg)
<B>4. Fork 해 온 Repository 확인 후에 클릭해서 들어가기 </B><br>
<br>
![5](https://user-images.githubusercontent.com/58154638/184289824-dd7a1971-ebc7-4e7d-b3f6-b4e5cf0588c6.jpg)
<B>5. 왼쪽 상단에 내 아이디/Algorithm-DataStructure이 되어있다면 잘 된 것, 이후에 Git Clone을 위해 주소 복붙!</B><br>
<br>
![6](https://user-images.githubusercontent.com/58154638/184289830-31edab43-a931-4585-84ee-7465e53799af.jpg)
<B>6. HTTPS에 있는 주소 복붙!! </B><br>
<br>
![7](https://user-images.githubusercontent.com/58154638/184289835-6b2c2068-2549-4f29-a618-d9987ff4e712.jpg)
<B>7. Git Bash를 이용하여 내가 원하는 파일 경로로 이동하여 명렁어" Git clone 주소 " 입력하기 </B><br>
<B> ※주의사항 : 이동 경로중에 파일명이 한글로 되어있다면, 나중에 문제가 될 수 있음 ex) C:\공부\~~~ (x) // C:\Education\~~~(o)</B><br>
<br>
![8](https://user-images.githubusercontent.com/58154638/184289840-95af4127-815f-40d0-bcfb-d35a5c62d58b.jpg)
<B>8. 이제 GitDesktop에 내 아이디로 접속하여, 내가 받은 Repogitory 셋팅하기 경로명, 파일 이름 확인하기 </B><br>
<br>
![9](https://user-images.githubusercontent.com/58154638/184289845-abf7a689-6837-4db8-84bf-b3875c349388.jpg) <br>
<B>9. 학번-이름으로 된 자기 파일로 경로를 잡는 것이 아님!! </B><br>
<br>
![10](https://user-images.githubusercontent.com/58154638/184289847-05f05c68-e33b-4c5c-ae03-e0dd8a248ba1.jpg)
<B>10. add로 추가하였다면 저렇게 자연스럽게 GitDesktop에 Repository가 추가 된 것을 볼 수 있음</B><br>
<B> -- 여기까지가 기본 셋팅 -- </B><br>
<br>
![11](https://user-images.githubusercontent.com/58154638/184289849-a1c8d940-418f-4803-8390-fd60dac97ca0.jpg)
<B>11. (visualStudio 기준 예시) 열심히 작업을 하고 항상 Ctrl + S로 저장하기, 저장안하면 GitDeskTop에서 변경사항이 안 뜸 </B><br>
<br>
![12](https://user-images.githubusercontent.com/58154638/184289854-a786a8f5-10d3-4037-b324-ebc3c4141593.jpg)
<B>12. 열심히 문제를 풀고 GitDesktop으로 돌아와서 변경사항 다시 확인하고 Commit Message 작성하기(최대한 구체적으로) 이후 Commit하고 Push하기 </B><br>
<br>
![13](https://user-images.githubusercontent.com/58154638/184289859-d30c3c63-b3dc-4546-9251-22b7acd10ec8.jpg)
<B>13. Push이후 변경 사항 확인하기 </B><br>
<br>
![14](https://user-images.githubusercontent.com/58154638/184289863-16d75eb3-21a4-4f63-b31a-3e55caf63218.jpg)
<B>14. Pull Resquests 클릭 -> New Pull Request 클릭하기 </B><br>
<br>
![15](https://user-images.githubusercontent.com/58154638/184289869-beb2baac-5ad5-40a0-9aef-0de6bdd4a36d.jpg)
<B>15. Create Pull Request 클릭 </B><br>
<br>
![16](https://user-images.githubusercontent.com/58154638/184289875-6c4b6c79-4bca-4933-8b38-9dfd0478a798.jpg)
<B>16. Comment는 문제에 대한 것 혹은 무엇을 공부했는지에 대해서 자세하게 작성하기 이후 Create Pull Request 클릭 </B><br>
<br>
![17](https://user-images.githubusercontent.com/58154638/184289878-73dfa293-0f52-49e1-afd6-af2d50c70bfc.jpg)
<B>17. 오른쪽 상단에 Review Request 클릭 이후 동아리 누구에게나 요청하기(최소2명이상) </B><br>
<br>
![18](https://user-images.githubusercontent.com/58154638/184289882-d36a07c3-288c-4cb0-bef2-9140c5fac55a.jpg)
<B>18. Review 요청을 받은이들은 열심히 물어보고, 질문하기 궁금증이 해결되었거나 피드백이 반영되었다면 Approve 체크 후, LGTM(Looks Good To Me 약자) 남기기 </B><br>
<br>
<B> 예시 </B><br>
![KakaoTalk_20220812_122844584](https://user-images.githubusercontent.com/58154638/184292627-3a8dc649-61ef-438e-81b8-90bbcba27ad1.jpg) <br>
![KakaoTalk_20220812_122845312](https://user-images.githubusercontent.com/58154638/184292635-396704b7-f742-4470-91d8-3edff46bfbe4.jpg) <br>

_[목차로 이동](#zap목차)_
