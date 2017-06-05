ⓒ JMC 2017

**주요 소스**  
멋쟁이 사자처럼 강의

---

## 11 멋사 4주차 10, 11번

### 삭제기능 구현하기

### 수정기능 구현하기

---

## 10 멋사 4주차 7,8,9번

### 보낸 메일 기록하기 (2)~(4) ::: DB

[실습 c9 링크](https://ide.c9.io/datalater/jt_secondboard)

#### 모델에 대한 이론 설명

Q1. M of MVC

+ M : 모델 (:= 데이터베이스)

Q2. 모델은 4가지 행동을 한다.

+ CRUD
    + C : Create : 데이터베이스를 쓰고
    + R : read : 데이터베이스를 읽고
    + U : Update : 데이터베이스를 수정하고
    + D : Delete 또는 Destroy : 데이터베이스를 삭제한다.

+ 모든 웹서비스가 이런 동작을 한다. ex. 인스타그램
    + 인스타그램에 사진 포스트를 쓰고
    + 인스타그램 포스트를 읽고
    + 인스타그램 포스트를 수정하고
    + 인스타그램 포스트를 삭제한다.

#### Submit 누르면 쓴 글을 자동으로 보여주는 리스트 페이지 구현하기

Q3. 함수 구현 및 뷰 파일 생성

+ 컨트롤러에 `list` 함수 만든다.

```ruby
class HomeController < ApplicationController
  def index
  end

  def write
    @post_title = params[:title]
    @post_content = params[:content]
  end

  def list

  end
end

```

+ 뷰에 `list.erb` 파일 생성한다.

```html
<h1>지난 글 목록입니다.</h1>
```

Q4. `write` 함수에 redirect 기능 넣기

```ruby
class HomeController < ApplicationController
  def index
  end

  def write
    @post_title = params[:title]
    @post_content = params[:content]
    redirect_to "/list"
  end

  def list

  end
end
```

+ `redirect_to`에 의해 write 함수는 더 이상 `write.erb` 뷰 파일을 출력하지 않고, 이제 `list.erb` 뷰 파일을 출력하게 된다.

Q5. `write` 함수에 대한 route 추가하기

```ruby
Rails.application.routes.draw do
  root 'home#index'
  get 'home/index'
  post '/write' => 'home#write'
  get 'list' => 'home#list'
```

+ 서버를 켜고 포스트 작성해서 submit 눌러본다.
+ `/list` 페이지가 나오는 것을 확인한다.

#### 모델 생성 및 마이그레이트

참조: [공식문서](http://edgeguides.rubyonrails.org/active_record_migrations.html)

Q6. 모델 생성하기

+ bash 창을 클릭한다.
+ `rails g model post`
+ post라는 이름의 모델을 생성한다.

Q7. 모델을 생성하면 2가지 파일이 자동 생성된다.

+ `/db/migrate` 폴더에 숫자로 시작하는 `create_posts.rb` 파일 생성
+ `/app/models` 폴더에 `post.rb` 파일 생성

> **Note:** 당분간 `post.rb` 파일은 수정하지 않는다. migrate 폴더에 있는 파일은 자주 사용할 것이다.

Q8. `create_posts.rb` 파일 코드 수정

+ 위와 같이 `migrate` 폴더에 있는 파일을 마이그레이션 파일이라고 한다.

```ruby
class CreatePosts < ActiveRecord::Migration
  def change
    create_table :posts do |t|

      t.string :title
      t.string :content

      t.timestamps null: false
    end
  end
end
```

+ 코드를 작성하는 일반형은 다음과 같다.
    + `t.데이터타입 "저장할 내용의 변수 이름"`
    + `t.datatype "column_name"`
+ 예시
    + t.string :title
    + t.integer "view_count" (조회수)
    + t.datetime "date"
    + t.float "eyesight"
+ DB 파일은 테이블로 구성되어 있는데, 위에 추가한 것들이 column을 구성하게 된다.
    + 가령, `t.string :title`과 `t.string :content`에 의해서
    + title 칼럼과 content 칼럼이 생성된다.
    + 칼럼 이름을 여기서 처음 짓는 것이다.
    + 컨트롤러의 변수(`post_title`) 또는 HTML 태그의 name(`title`)과 다르게 이름 지어도 상관없다.
    + `t.string "title_column"`이라고 해도 된다.

Q9. 마이그레이션 파일 작성 후 마이그레이트 하기

+ bash 창을 클릭한다.
+ `rake db:migrate`
+ 마이그레이트 명령어를 입력하면 데이터베이스 파일을 생성한다.
    + `development.sqlite3`

#### C of CRUD

Q10. 컨트롤러를 모델과 연동하도록 `write` 함수 코드를 수정한다.

```ruby
class HomeController < ApplicationController
  def index
  end

  def write
    @post_title = params[:title]
    @post_content = params[:content]

    new_post = Post.new
    new_post.title = @post_title
    new_post.content = @post_content
    new_post.save

    redirect_to "/list"
  end

  def list

  end
end
```

+ `new_post = Post.new`
    + `Post`라는 모델의 새로운 인스턴스를 만든다.
    + 그 인스턴스를 변수 `new_post`에 할당한다.
    + DB 파일은 테이블로 구성되어 있는데, `Post.new` 명령어를 입력하는 순간, 새로운 row가 생성된다.

+ 위 코드를 더 줄여서 써도 된다.

```ruby
class HomeController < ApplicationController
  def index
  end

  def write
    new_post = Post.new
    new_post.title = params[:title]
    new_post.content = params[:content]
    new_post.save

    redirect_to "/list"
  end

  def list

  end
end
```

#### R of CRUD

Q11. 모델의 모든 내용을 보여주도록 `list` 함수의 코드를 수정하기

```ruby
class HomeController < ApplicationController
  def index
  end

  def write
    @post_title = params[:title]
    @post_content = params[:content]

    new_post = Post.new
    new_post.title = params[:title]
    new_post.content = params[:content]
    new_post.save

    redirect_to "/list"
  end

  def list
    @every_post = Post.all

  end
end
```

+ 위에서 생성한 변수를 뷰에서 출력하도록 한다.

```html
<!-- list.erb -->

<h1>지난 글 목록입니다.</h1>
<h2><%= @every_post %></h2>
```

Q12. 서버를 켜고 테스트하기

+ 내가 쓴 글이 아니라 `<Post::ActiveRecord_Relation...>` 코드가 찍힐 것이다.
+ 모델 객체 전체가 찍힌 것이다.


Q13. 모델 객체 순회하기 (보낸 메일 기록하기 (4))

+ `write.erb` 파일을 수정한다.

```html
<h1>지난 글 목록입니다.</h1>
<% @every_post.each do |p| %>
제목: <%= p.title %> <br>
내용: <%= p.content %>
<hr>
<% end %>
<p><a href="/">메인으로 가기</a></p>
```

+ `@every_post`는 여러 글이 한꺼번에 담겨 있기 때문에 하나씩 빼줘야 한다.
+ 하나씩 순회할 때는 each 구문을 사용한다.
+ HTML 파일에서 ruby 신택스를 쓸 때, 출력해야 하면 `<%= %>`을 쓰고 출력할 필요가 없다면 `<% %>`를 쓴다고 생각해두자.

Q14. 서버를 켜고 테스트하기

+ 만약 DB 관련 오류가 뜨는 것 같다면 다음 명령어를 차례대로 실행한다.

```shell
rake db:drop,    
rake db:create,    
rake db:migrate
```

Q15. 최신 포스트가 위에 오도록 정렬하기

```ruby
    def list
      @every_post = Post.all.order("id desc")
    end
```

+ `order("id desc")` : id 내림차순 정렬
+ `order("id asc")` : id 오름차순 정렬

**끝.**

---

## 09 멋사 4주차 6번

### 보낸 메일 기록하기 (1)

Q1. 워크스페이스 생성

+ `rails g controller home index`

Q2. `application_controller` 보안 코드 주석 처리하기

+ `# protect_from_forgery ...`

Q3. `/views/layouts` 레이아웃 application.html.erb에 Bootstrap CDN 인클루드하기

+ `<%= javascript_include_tag ...%>` 밑에 붙여넣기
+ 윗 줄에 있는 `...-turbolinks-...` 모두 `false`로 바꾸기

> **Note:** turbolink 기능 때문에 버그 발생하는 경우가 더러 있기 때문에 false로 바꿔준다.

Q4. form tag 코드 Bootstrap에서 복붙하기

```html
<form>
  <div class="form-group">
    <label for="exampleInputEmail1">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Email">
  </div>
  <div class="form-group">
    <label for="exampleInputPassword1">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
  </div>
  <div class="form-group">
    <label for="exampleInputFile">File input</label>
    <input type="file" id="exampleInputFile">
    <p class="help-block">Example block-level help text here.</p>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox"> Check me out
    </label>
  </div>
  <button type="submit" class="btn btn-default">Submit</button>
</form>
```

Q5. form tag 수정하기

+ 전체 코드를 `<div class="container">...</div>`로 감싸주기
+ 위에 너무 붙기 때문에 margin 옵션 넣어주기
    + `<div class="container" style="margin-top:50px;">`
+ 필요 없는 태그를 지우고, "제목", "내용"에 대한 `<input>` 태그를 만들어둔다.
+ 내용 태그는 Bootstrap textarea 검색해서 가져오기
    + `<textarea class="form-control" rows="5" id="content"></textarea>`

+ "제목" 태그와 "내용" 태그에는 각각 `name="title"`, `name="content"`를 넣어준다.
+ `<form action="/write" method="POST">`

```html
<div class ="container">
    <h1>게시판입니다.</h1>
    <form action="/write" method="POST">
      <div class="form-group">
        <label for="title">글 제목</label>
        <input name="title" type="text" class="form-control" id="title" placeholder="제목을 입력하세요.">
      </div>
      <div class="form-group">
        <label for="content">글 내용</label>
        <textarea name="content" class="form-control" rows="5" id="content" placeholder="내용을 입력하세요."></textarea>
      </div>
      <button type="submit" class="btn btn-default">Submit</button>
    </form>
</div>
```

Q6. 라우트와 컨트롤러 파일 수정하기

+ `routes.rb` 파일에서 `post '/write' => 'home#write'` 추가하기

```ruby
Rails.application.routes.draw do
  root 'home#index'
  get 'home/index'
  post '/write' => 'home#write'
```

+ `home_controller.rb` 파일에서 write 함수 정의하기

```ruby
class HomeController < ApplicationController
  def index
  end

  def write
    @post_title = params[:title]
    @post_content = params[:content]
  end
end
```

Q7. 함수 `write`에 대한 view 파일 만들기

+ `/views/home` - [New File] - write.erb

```html
<!-- write.erb -->

<h1>글이 정상적으로 등록되었습니다.</h1>

<h2>제목: </h2>
<%= @post_title %>
<h2>내용: </h2>
<%= @post_content %>

<hr>

<a href="/">메인으로 가기</a>
```

**끝.**

---

## 08 멋사 3주차 10번

### 게시판 만들기 (3)

Q1. `write` 함수를 수정해서 실제로 쓴 내용을 변수에 담기

+ 변수를 활용한다.

```ruby
# controller.rb

class HomeController < ApplicationController
  def index
  end

  def write
    @post_title = params[:title]
    @post_content = params[:content]
  end
end
```

+ `@post_title` : post의 title을 전달할 변수 이름을 `@post_title`로 짓는다.
+ `params[:title]` : 변수에 할당할 값으로 form 태그의 하위 태그 중 태그의 name이 title인 태그의 내용으로 지정한다.
    + `<input name="title" type="text" class="form-control" id="exampleInputEmail1" placeholder="제목을 입력하세요.">`
+ 즉 form 태그의 값을 전달하는 변수는 다음과 같은 형태로 쓰면 된다.
    + `@variable_name = params[:tag_name]`

Q2. 컨트롤러의 변수를 view에서 출력하기

```html
 <!-- write.erb -->

 <h1>글이 정상적으로 등록되었습니다.</h1>

 <h2>여러분이 쓴 글의 제목은</h2>
 <%= @post_title %>
 <h2>여러분이 쓴 글의 내용은</h2>
 <%= @post_content %>
```

+ `<%= @variable_name %>` : 변수를 출력할 때
+ `<% @variable_name %>` : 변수를 불러내지만 출력하지는 않을 때

Q3. 직접 테스트하기

+ 컨트롤러를 새로 작성했으니 server를 reset해준다.
+ 제목과 내용을 적고 submit을 눌러본다.

Q4. 메인으로 가는 버튼을 만들기

```html
<!-- write.erb -->

<h1>글이 정상적으로 등록되었습니다.</h1>

<h2>여러분이 쓴 글의 제목은</h2>
<%= @post_title %>
<h2>여러분이 쓴 글의 내용은</h2>
<%= @post_content %>

<hr>

<a href="/">메인으로 가기</a>
```

+ 약 26줄의 코드를 작성했다.
+ 몇 줄 안되지만 오늘 배운 내용이 웹 개발의 핵심이다.
+ 여러 번 실습해보고 익혀보자.

Q5. 게시판 만들기 (1), (2), (3)을 그대로 따라서 복습해본다.

+ 시작!

**끝.**

---

## 07 멋사 3주차 8, 9번

### 게시판 만들기 (1), (2)

Q1. MVC 초기 세팅

+ `rails g controller home index`

Q2. root 페이지를 index로 연결하기 위해 routes.rb 파일 수정

```ruby
Rails.application.routes.draw do
  root 'home#index'
  get 'home/index'
```

Q3. Bootstrap CDN 복사

```
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
```

Q4. `views/layouts/application.html.erb` 파일 클릭

+ `<%= csrf_meta_tags %>` 아래 줄에 붙여넣기

Q5. Bootstrap form 태그 붙여넣기

+ [Bootstrap form](http://getbootstrap.com/css/#forms)에서 Basic Example 코드 복사
+ `index.html.erb` 파일에 붙여넣기
+ 서버 refresh
+ file input과 check me out 블락 삭제하기
+ 서버 refresh. 양쪽이 너무 가장자리에 붙었으므로 `<div class = "container"></div>` 태그로 감싸주기
+ 현재 input 태그의 내용이 이메일과 패스워드로 되어 있다.
+ 다음과 같이 바꿔주자.


Q6. form 태그 수정하기

+ Email >> 글 제목
    + 그런데 글 제목에 글자를 입력하면 오류 메시지가 뜨면서 이메일 형식에 대한 유효성 검사를 한다.
+ `<input type="email">` >> `<input type="text">`
+ Password >> 글 내용
    + 그런데 글 내용 칸에 글자를 입력하면 비밀번호 형식으로 나온다.
+ `<input type="password">` >> `<input type="text">`
+ 그리고 글 내용은 보통 한 줄짜리가 아니라 여러 줄로 쓰므로 태그를 바꿔준다.
+ 여러 줄을 쓰는 태그는 `<input>`이 아니라 `<textarea>` 태그를 쓴다.
+ [Google:Bootstrap textarea] 검색해보자.
+ 기존 `<input>` 라인을 삭제하고 `<textarea class="form-control" rows="5" id="comment" placeholder="내용을 입력하세요."></textarea>`를 붙여넣는다.
+ 각 칸에 글자를 입력하고 submit 눌러본다. 오류 메시지 뜨지 않는다.

Q6-1. form 태그 수정하기 2

+ 글 제목과 글 내용 태그 각각에 name 옵션을 넣어준다.
+ `<input name="title>"`
+ `<textarea name="content>"`

> **Note:** name은 원래 기본적으로 설정해야 할 뿐만 아니라, GET 방식으로 테스트할 때 URL의 변화를 보려면 name을 설정해야 한다.

---

Q7. HTTP 전송 방식 중 GET 에 대하여

+ 구글 검색해보자. [Google:구글]
+ url에서 `q=구글` >> `q=구글코리아`
+ 검색창이 자동으로 바뀌어 있다.
+ 주소만 바꿔도 자동으로 검색된다.
+ 이게 GET 방식이다.

Q8. GET vs. POST

+ 내가 검색할 쿼리 내용을 주소에 그대로 노출하는 방식 = GET
+ 사용자의 request 내용을 url에 그대로 노출하는 방식 = GET
+ 사용자의 request 내용을 url에 노출하지 않는 방식 = POST


Q9. GET vs. POST 가장 큰 차이점

+ GET은 URL에 이어붙이기 때문에 길이 제한이 있어서 많은 양의 데이터를 보내기 어렵다.
+ POST는 많은 양의 데이터를 보내기 적합한 전송 방식이다.

Q10. GET vs. POST 사례

+ GET : 검색
+ POST : 게시판 글쓰기, 이메일 보내기, 파일 첨부

> **Note:** 기본적으로 웹에서는 GET 방식이 대부분이다. 데이터를 전송할 때만 POST를 쓰고 그 외에는 모두 GET을 쓴다고 생각해도 OK.

Q11. GET vs. POST 의미 차이

+ GET : 데이터를 가져온다
+ POST : 데이터를 전송한다

---

Q12. c9에 만든 게시판 글쓰기에 POST를 적용해보자.

Q13. `routes.rb` 파일로 이동해서 post 방식으로 url과 함수를 맵핑한다.

```ruby
post '/write' => 'home#write'
```

Q14.` home_controller` 파일로 이동해서 post 방식을 사용할 함수를 만든다.

+ write 함수를 만든다.

```ruby
class HomeController < ApplicationController
  def index
  end

  def write

  end
end
```

Q15. 함수를 만들었으니 view를 만들어준다.

+ `views/home - [New File] - write.html.erb`

```html
<h1>글이 정상적으로 등록되었습니다.</h1>
```

Q16. `index.html.erb` 파일로 이동

+ `<form>` 태그에서 submit 버튼을 눌렀을 때 어느 페이지로 이동할지 옵션을 정해줘야 한다.
+ 그 옵션을 `action`이라고 한다.
+ `action`에 대한 전송방식도 정해줘야 하는데 그 옵션을 `method`라고 한다.

```html
<form action="/write" method="POST">
```

+ 위 코드의 뜻은, submit 버튼을 눌렀을 때 form 태그에서 입력받은 내용을 url `/write`에게 전달하되 주소에 내용을 노출시키지 않도록 POST 방식을 사용한다는 뜻이다.


Q17. 서버 테스트

+ 글 제목과 글 내용을 입력하고 submit 버튼을 누른다.
+ 아마 아래와 같은 오류가 뜰 것이다.

```
ActionController::InvalidAuthenticityToken in HomeController#write
```

+ `contorllers/application_controller` 파일로 이동
+ `protect_from_forgery with: :exception` >> `# protect_from_forgery with: :exception` 주석처리하기
+ 다시 글을 작성하고 submit 해보자.

> **Note:** `protect_from_forgery with: :exception`는 해킹을 막아주는 보안 기능을 한다. 개발 테스트 단계에서는 주석처리 해두자.

Q18. POST 방식을 GET으로 바꿔보자.

+ form 태그의 method를 get으로 바꾼다.
+ routes.rb 파일에서 POST를 get으로 바꾼다.
+ 서버에서 테스트해본다.

Q19. 다시 POST로 되돌려준다.

+ URL을 확인해본다.
+ `/write`만 나올것이다.

**끝.**

---

## 06 멋사 3주차 6번

### 페이지간 점프하기

Q1. MVC 런쓰루 복습하기

+ 새 워크스페이스
+ `rails g controller home index`
    + controller와 action과 view와 routes를 한번에!
        + `controllers/home_controller.rb`
        + `def index`
        + `views/home/index.html.erb`
        + `config/routes.rb` - `get 'home/index'`

Q2. routes.rb 파일 수정
+ view 파일 수정

```html
<h1>home/index.html.erb!!!!</h1>
```

+ route 파일 수정


```ruby
get 'home/index'                
# 'home/index'로 request url이 들어오면 home 컨트롤러의 index 함수로 처리한다.

get 'name' => 'home#index'      
# '/name'으로 request url이 들어오면 home 컨트롤러의 index 함수로 처리한다.

get '/' => 'home#index'         
# '/'으로 request url이 들어오면 home 컨트롤러의 index 함수로 처리한다.
# root 'home#index'와 같은 뜻이다.
```

+ `get '내가 연결하고 싶은 url' => '내가 연결하고 싶은 controller#function'`
+ url(`controller/function`)의 형태가 컨트롤러/함수(`controller#function`)와 정확히 일치하면 url만 써줘도 된다.

Q3. 페이저 점프해보기

+ index.html.erb 파일을 수정한다.

```html
<!-- index.html.erb -->

<h1>home/index.html.erb!!!!</h1>

<hr>
<a href="/hornet">말벌로 점프</a>
```

+ 브라우저에서 실행해본다. routes 관련 오류가 뜬다.

Q4. 새로운 url에 대한 action을 만들고, view파일을 만든다.

+ routes.rb 파일을 수정한다.

```ruby
get 'name' => 'home#index'
get '/' => 'home#index'
get 'hornet' => 'home#hornet'
```


+ 새로운 action(`#hornet`)을 만들기 위해 home_controller.rb 파일을 수정한다.
```ruby
def index
end

def hornet
end
```

+ 새로운 action(`#hornet`)에 대한 view 파일(`hornet.erb`)을 만들고 수정한다.

```html
<h1>5cm 말벌의 습격!!</h1>
<hr>
<a href="/">메인으로 가기</a>
```

**끝.**

---

## 05 멋사 3주차 1,2,3,4번

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
