ⓒ JMC 2017

**주요 소스**  
멋쟁이 사자처럼 강의

---

---

## 05 멋사 3주차

### MVC 런쓰루 복습

Q1. 새 워크스페이스 - controller 생성 - view 파일 생성 - route 파일 수정
- 워크 스페이스 제목: food
- 아래 명령어를 기계적으로 따라한다.
- `rails g controller tomato`

```ruby
# controller.rb

    def potato

    end
```

- 뷰 폴더에 함수에 대한 erb파일을 만든다. `views/tomato/potato.erb`

```html
<h1>원해?</h1>
```

- config폴더에서 route를 수정한다. `config/routes.rb`

```ruby
# routes.rb

    root "tomato#potato"

```

+ `Run Project` 후 웹 페이지 확인

### Ruby 문법

Q1. 리스트에서 랜덤 추출

```ruby
@food_list = ['짜장면', '피자', '탕수육', '순두부찌개', '쌀국수']
@today_food = @food_list.sample
```

### 오늘의 랜덤 푸드

Q1. 음식 이미지를 구글링으로 저장한 후 서버에 업로드한다.
- `/app/assets/images`에 `jjm.jpg`, `tangsu.jpg`를 업로드한다.

> **Note:** c9에서는 파일 제목을 한글로 쓰면 오류가 발생할 수 있다. 가령 `탕수육.jpg`로 올리면 에디터에서는 잘 보이지만, 막상 파일을 클릭하고 Rename 눌러보면 `ㅌㅏㅇㅅㅜㅇㅠㄱ.jpg` 이런 식으로 나오는 경우가 있다.


Q2. 이미지 파일 이름을 활용해서 컨트롤러 코드를 수정한다.

```ruby
@food_list = ['짜장면', '탕수육', '제육볶음', '옐로우피자']
@today_food = @food_list.sample
@today_food_image = @today_food + ".jpg"
```

Q3. 이미지 파일을 view로 출력해본다.
- rails에서 이미지 태그는 어떻게 쓸까? 구글링해보자.
- 구글링: `rails image tag`

```html
<h1>오늘의 음식 추천!</h1>
<!-- <img src="/images/jjm.jpg" /> -->

<h2><%= @today_food %></h2>
<%= image_tag "jjm.jpg" %>
```

Q4. javscript로 refresh 버튼 만들어보자.
- 구글링: javscript refresh button

```javascript
<h1>오늘의 음식 추천!</h1>
<a href="javascript:location.reload(true)">Refresh this page</a>
<!-- <img src="/images/jjm.jpg" /> -->

<h2><%= @today_food %></h2>
<%= image_tag @today_food_image %>
```

**끝.**

---

## 04 멋사 2주차 5,6 번 강의

### MVC

Q1. 서버는 어떻게 구성되는가
- Model
- Controller
- View

Q2. 컴퓨터를 구성하는 모든 어플리케이션은 MVC로 이루어져있다.
- 곤충은 머리/가슴/배로 이루어져있다

Q3. MVC 설명
- Model : 게시판 글이 다 담겨져 있는 곳
- Controller : 모델에 있는 모든 데이터를 적당히 뽑아서 View에게 던져준다.
- View : 던져받은 데이터를 예쁘게 꾸민다.

> **Note:** 클라이언트가 HttpRequest(요청)를 보내면 서버는 MVC를 거쳐서 HttpResponse(응답)를 내보낸다.

Q4. Ruby on Rails와 MVC
- ROR은 MVC를 쓰기에 가장 최적화된 웹 프레임워크
- 가장 쓰기 쉽다

### MVC c9 실습

Q1. MVC 중에서 C, 즉 controller를 배워보자.
- View는 이미 배웠다.

Q2. public 폴더는 영영 쓰지 않을 것이다.
- 연습용이었다.

Q3. 컨트롤러(controller) 생성
- `rails g controller banana`
- `g` stands for generate

Q4. 우리가 앞으로 엄청나게 많이 쓰게 될 폴더
- `/app/controllers`
- `/app/models`
- `/app/views`
- `/config/routes.rb`

Q5. `/app/controllers` 폴더를 열어보자
- `banana_controller.rb`를 확인 후 클릭해본다.
- 아래 소스코드 입력

```ruby
class BananaController < ApplicationController

    def apple
        "안녕하세요"
    end

end
```
+ 함수 apple을 action이라고 부른다.

Q6. 함수의 내용을 전달할 view를 만들어보자.
+ `/app/views/banana` - [New File] - `apple.erb`
+ 함수의 이름과 New File의 이름이 반드시 같아야 한다.

Q7. view에 코드를 써보자.
- `apple.erb`에 아래 소스코드를 입력한다.

```html
<h1>안녕하세요</h1>
```

Q8. routes에 코드를 써보자.
- `config/routes.rb`를 열고 아래 소스코드를 입력한다.

```ruby
Rails.application.routes.draw do
  root "banana#apple"

(...생략...)
```

- `Run Project` 해보자.
- 브라우저로 프로젝트 url을 열고 '안녕하세요'를 확인한다.

Q9. controller에 변수 만들고, view에 변수 넣기
+ 아래 소스코드를 입력한다.

```ruby
# controller

class BananaController < ApplicationController

    def apple
        @mango = "안녕!"
        @name = "Jay"
    end

end
```

```html
<!-- view -->

<h1><%= @mango %></h1>
<h1>내 이름은 <%= @name %>, 한국의 조커버그야.</h1>
```

+ `Run Project`해서 프로젝트를 확인한다.
+ 이것이 controller와 view의 전부이다.
+ controller에서 어떤 연산을 하고 그 연산의 결과를 `@변수`에 넣고 `@변수`를 view로 전달한다.
+ `@변수`는 비둘기 역할을 한다. 비둘기! 뀨뀨!

> **Notes:** Ruby 코드와 HTML 코드를 동시에 쓸 수 있다. 다만 Ruby 코드를 쓰려면 지금부터 Ruby 코드를 쓴다는 의미로 `<% @variable %>`를 표시해줘야 한다.

**끝.**

---

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

**끝.**

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

**끝.**

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
