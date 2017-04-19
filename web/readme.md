## 03 멋사 2주차 1번 강의

#### jQuery 강의

Q1. HTML 요소에 마우스를 갖다 대면 손가락 cursor로 보여주기
- `<id="clickme" style="cursor:pointer;">`

Q2. javascript에 대한 설명
- `<script>`와 `</script>` 사이에 있는 코드는 순서를 아무렇게나 둬도 된다.
- 왜냐하면 javascript는 event 기반이기 때문이다.
- 가령 fadeOut과 fadeIn은 click event 기반이다.

Q3. java vs. javscript  
- 아무런 관계가 없다.
- 인도와 인도네시아 같은 관계

Q4. 웹 개발 추천 사이트
- div.or.kr

Q5. jQuery 추천
- 흔히 웹에서 자주 쓰이는 jQuery를 모아둔 것
- 사용법: `view source` 클릭 전체 복사 후 붙여넣기
- 일단 실행해보고 무엇을 수정하면 좋을지 생각해본다.
- accordion의 경우 실제 javscript 코드는 3줄밖에 안 됨.
- `$("#accordion").accordion();` accordion이라는 id를 가진 태그를 accordion화 시켜라, accordion 함수에 적용되도록 해라.
- `//$("#accordion").accordion();` 주석처리 해보기

Q6. javscript 예시
- google:javscript showcase
- javscript는 실제로 짜기는 어렵고 라이브러리를 갖다 쓰는 경우가 많음
- ex. canvas sphere
- 개발자도구를 통해 코드를 보면
- `style.css`과 `sphere.js`가 필요하다는 것을 알 수 있다. 두 개를 include하고 있기 때문이다.
- 개발자도구 소스보기에서 각각을 클릭 후 복사해서 같은 방식으로 폴더와 파일을 만들어서 붙여 넣어주면 된다. (public/js/sphere.js, css/style.css)


Q7. copy&paste 주의사항
- LICENSE를 반드시 확인한다.
- Source가 공개적으로 노출되어 있는 오픈 소스는 얼마든지 사용해도 좋다. 특히 학습 위주로 사용하면 안전하다.
- 실제로 상용 LICENSE가 걸려있는 것을 사용하면 큰일난다.

---


## 02 멋사 1주차 8~9번 강의

#### grid 시스템 만들어보기

Q1. c9 - html - bootstrap CDN
- c9 workspace 만든다.
- /public - new file - index.html
- html 뼈대 태그 작성하기
- google:bootstrap https://getbootstrap.com - getting started - CDN 복사 후 붙여넣기
- 주석 삭제
- body에 한글로 아무 말 쓰고 Run Project
- bootstrap 쓸 때는 jQuery를 앞에 include 해야 한다.

Q2. jQuery CDN
- google:jQuery - download - Using jQuery with CDN - https://code.jquery.com - 최신 버전 선택 - CDN 복사 후 붙여넣기

Q3. // vs. https:// vs. http://
- CDN에 있는 src 직접 접속해보기 ex. https://code.jquery.com/jquery-3.2.1.js
- //만 쳐도 정상 작동
- //만 쳐도 자동으로 접속함
- http에서 보안을 더 강화한 것이 https (s stands for security)

Q4. grid 시스템을 배워보자
- bootstrap - css - grid system
- document를 그대로 따라서 해보면 된다.
- Mobile First 코드 붙여넣기
    - 코드 해석 : 화면 너비를 device 너비로 고정한다.
    - scalable : 확대 가능 여부
- Grid System example 코드 복붙
- bootsrap의 grid system을 사용하는 모든 코드는 container로 시작해서 container로 끝난다. 마치 html 태그의 body 태그 같은 느낌.

Q5. HTML/CSS 코드
+ style = margin-top=20px;

#### responsive grid

Q1. PC와 모바일 환경에서 다르게 배치하기
- medium : PC
- small : Tablet / Mobile
- col-md-7 col-xs-6

#### CSS 적용해보기

Q1. css 폴더 생성 후 stylesheet.css 연결하기
- /public - new folder - css - new file - stylesheet.css
- [link href="css/stylesheet.css" rel="stylesheet"]

#### grid 시스템 offset

Q1. [div class = row]를 하나 더 만든다.
- 총 (1, 1), (1, 2), (2, 1), (2, 2)의 well을 만든다.
- 한 줄에 있는 두 칼럼의 비율은 7:5로 맞춘다.
- [div class="col-md-5 col-md-offset-7"]

#### jQuery 적용하기

Q1. jQuery가 편리한 이유
- 원래는 javascript를 맨땅에서부터 다 배워야 구현할 수 있다.
- 그런데 javascript에서 자주 쓰는 코드를 라이브러리로 만든 게 jQuery이다.
- jQeury를 이용하면 당연히 맨땅에서 할 필요 없이 편하게 사용할 수 있다.

Q2. jQuery 사용해보기
- 이미 jQuery를 include 했다는 것을 알고 있어야 한다.
- jQuery.com - API documentation - Effect - .fadeOut()
- $로 시작하는 예제코드 복사
- javascript 코드를 쓸 때는 반드시 [script] [/script] 태그를 써야 한다.
- javscript 코드는 head 태그 사이에 넣어도 되고 body 태그 사이에 넣어도 된다. 요즘 추세는 body 태그 마지막에 넣는다.

Q3. .fadeOut() 코드 해석
- id=clickme 를 클릭하면
- id=book 을 slow 천천히 fadeOut 시킨다.

Q4. .fadeIn() 만들어서 없어진 놈 다시 나타나게 만들기 [실습]

---
---


## 01 멋사 1주차 1~7번 강의

Q1. 웹 개발로 배우는 이유
- 바로 바로 구현하면서 써먹을 수 있다.
- 지루하지 않다.

Q2. 웹 개발이란?
- 프론트엔드
- 백엔드

Q3. 프론트엔드란?
- HTML/CSS/javscript [jquery]
- Angular(Google), React(Facebook)

Q4. 백엔드란?
- Ruby on Rails
- Python / Django
- Java
- JSP, ASP, PHP

---

Q5. 커리큘럼
- HTML
- CSS (Bootstrap)
- jQuery
- Ruby (simple web page)
- Database
- 게시판
- 오픈소스

Q6. 오픈소스는 무조건 활용한다
- 보통 서비스를 만들 때 바닥부터 만드는 경우는 없다
- 대부분 있는 도구들을 조립해서 만듦
- ex. 페이스북, 카카오톡

---

Q7. 2가지 약속
- 1) 브라우저 = chrome
- 2) 검색엔진 = Google

Q8. HTML과 CSS를 가장 효율적으로 배울 수 있는 곳
- https://www.codecademy.com/en/tracks/korean-web (7h)
- http://ko.learnlayout.com/
- (추가) http://learn.shayhowe.com/html-css/

---

Q9. 윈도우에서 rails 설치 어렵다. 따라서 2가지 사이트 가입한다.
- https://github.com 깃헙
- https://c9.io c9 (깃헙 계정으로 가입)

Q10. 깃헙 계정으로 c9 로그인 후 workspace 생성
- template Ruby on Rails로 설정

Q11. HTML 페이지 만들기 1 | C9 Run Project
- Run Project 후 주소 접속해보기
- \public - index.html
- [h1]] 아무거나 작성 [/h1]
- 주소 새로고침

---

Q12. HTML 페이지 만들기 2 | Bootstrap
- html utf8
- google:Bootstrap (트위터에서 만든 html 템플릿, 자주 쓰이는 요소들을 이쁘게 꾸며 놓은 것)
- Getting Started - Bootstrap CDN 복사 - [head][/head] 사이에 붙여넣기

Q13. HTML 페이지 만들기 3 | jQuery
- google:jQuery
- jquery.com/download - jQuery CDN 복사 - [head][/head] 사이에 붙여넣기

---

Q14. HTML 페이지 만들기 4 | Bootstrap 그리드 활용하기
- grid를 만들어 본다.
- 아 그냥 어디서 베끼고 싶다는 생각이 든다면 통과!

Q15. HTML 페이지 만들기 5 | 부트스트랩 테마를 적용하기
- google:bootstrap theme
- free 버전만 다운로드
- 압축 해제
- index.html 이름을 index2.html 변경
- c9의 public 폴더에 압축 파일 업로드 (css, img, js, index2.html)
- Run Project
- html 코드를 수정한다

---
