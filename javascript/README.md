모던 웹을 위한 JavaScript/jQuery 입문, 윤인성

---

## 2강 기본 문법

Q1. 표현식 + 세미콜론 = 문장

```JavaScript
10 + 20 + 30 * 2;
var rintiantta = 'Rint' + 'Ian' + 'Tta';
alert('Hello JavaScript..!');
273;
```

+ 자바스크립트는 문장 끝에 세미콜론을 일벽하지 않아도 프로그램 실행하는 데 문제가 없다.
+ 하지만 대부분의 프로그래밍 언어가 문장 끝에 세미콜론을 입력하므로 관례상 입력한다.

Q2. 키워드와 식별자

+ 키워드 : 예약어 ex. break, if, else, true, false, new, null, return, with, do
+ 식별자: 변수명과 함수명
    + 특수문자는 underscore( _ )와 dollar sign($)만 허용
    + 생성자 함수의 이름은 항상 대문자로 시작한다.
    + 변수, 인스턴스, 함수, 메서드의 이름은 항상 소문자로 시작한다.
    + 여러 단어로 이루어진 식별자는 각 단어의 첫글자를 대 문자로 한다.

```JavaScript
will out => willout
i am a boy => iAmABoy
```

+ 식별자의 종류 : 괄호 여부로 구분한다. 괄호 있으면 함수/메서드, 없으면 변수/속성.

```JavaScript
alert("Hello World")    => 함수
input                   => 변수
Math.abs(-273)          => 메서드
Math.PI                 => 속성
```

Q3. 주석

+ HTML 주석

```JavaScript
<!--주석-->
```

+ javascript 주석

```javascript
// 주석문
```

```javascript
/*
주석문
주석문
*/
```

Q4. 자바스크립트의 가장 기본적인 출력 방법

+ alert() 함수를 사용하면 웹 브라우저에 경고창을 띄울 수 있다.

```html
<script>
    alert("Hello JavaScript..!");
</script>
```

> **Note**: 이제부터 다른 태그를 별도로 건드리지 않는 이상 HTML 파일에서 script 태그 부분만 표시한다.

Q5. 함수의 매개변수

+ 함수의 괄호 안에 들어가는 것을 매개변수라고 부른다.
+ 함수마다 괄호 안에 입력될 것으로 예상하는 매개변수가 있다.

Q6. 문자열

+ alert() 함수의 매겨변수로 'Hello JavaScript..!'를 입력했다.
+ "Hello JavaScript..!" 같은 자료를 문자열이라고 부른다.
+ 문자열은 큰따옴표 or 작은따옴표로 표시한다.
+ 큰따옴표 안에 큰따옴표를 쓰려면 이스케이프 문자를 사용한다.

```html
<script>
    alert("This is \"string\"");
    alert('This is \'string\'');
</script>
```

Q7. 이스케이프 줄바꿈

```html
<script>
    alert("동해물과 백두산이\n마르고 닳도록")
</script>
```

+ 실행하면 '동해물과 백두산이'와 '마르고 닳도록' 사이가 줄바꿈된 것을 확인할 수 있다.

`@@@resume: p.68 코드 2-26 할 차례`

**끝.**

---

## 1강 (=챕터 1)

Q1. 자바스크립트의 활용

+ 초기의 웹은 하이퍼링크라는 매개체로 웹 문서가 연결된 하나의 거대한 책에 불과했다.
+ 자바스크립트가 나오고부터 웹 문서의 내용을 동적으로 바꾸거나 사용자가 마우스를 클릭하는 것 같은 이벤트를 처리할 수 있게 됐다.
+ 웹은 일반적인 웹 문서의 개념을 초월해 웹 애플리케이션으로 진화했다.
+ 대표적인 예가 웹 문서 작성 도구이다.
+ 별도의 설치 없이 웹 브라우저만으로도 워드, 엑셀, 파워포인트와 같은 애플리케이션을 사용할 수 있다.

Q2. HTML 파일 만들기

+ 코드 1-3 기본 구성

```HTML
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <script>

    </script>
</head>
<body>

</body>
</html>
```

+ HTML 페이지의 각 태그는 웹 브라우저에 의해 순차적으로 실행된다.
+ script 태그를 head 태그 안에 넣어야 코드를 살펴보기 편하므로 대부분 script 태그를 head 태그 안에 위치시킨다.

Q3. Hello World 예제

+ 코드 1-4

```html
<!DOCTYPE html>
<html>
<head>
    <script>
        alert("Hello World..!");
    </script>
</head>
<body>

</body>
</html>
```

+ 아톰 에디터에서 atom-html-preview 패키지 설치 후 ctrl+shift+h 단축키 실행

Q4. 콘솔 실행

+ 위에서 작성한 HTML파일을 크롬으로 실행
+ F12 단축키 실행
+ 코드에 오류가 있따면 우측 하단에 경고가 뜬다.

**끝.**

---
