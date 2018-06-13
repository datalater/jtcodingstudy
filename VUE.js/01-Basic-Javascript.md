ⓒ JMC 2018

---

### 01주차 기본 문법

Q1. 기본 문법에서 알아야 할 용어

번호  | 설명 | 개념
--|---|--
 1 | 값을 만들어내는 간단한 코드 | 표현식  
 2 | 프로그래밍 언어가 처음 만들어질 때 정해진 특별한 의미가 있는 단어 | 키워드(예약어)  
 3 | 이름을 붙일 때 사용하는 단어 또는 변수명이나 함수명 | 식별자(=이름)
 4 | 프로그램 코드를 설명하며, 프로그램 진행에 전혀 영향을 주지 않는 문장 | 주석  
 5 | 문자를 표현할 때 사용하는 자료형 | 문자열  
 6 | 숫자를 표현할 때 사용하는 자료형 | 숫자  
 7 | 참과 거짓을 표현할 때 사용하는 자료형 | 불(Bool)  
 8 | 값을 저장할 때 사용하는 식별자 | 변수  

Q2. 표현식과 문장

+ 표현식

```javascript
273
'JayMincheolCho'
```

+ 문장

```javascript
273;
var name = 'Jay' + 'Mincheol' + 'Cho'
alert('JayMincheolCho');
```

세미콜론을 입력하지 않아도 프로그램을 실행하는 데는 문제가 없지만 프로그래밍 언어 대부분이 문장 끝에 세미콜론을 입력하므로 자바스크립트에서도 관례상 입력한다.

Q3. 이름(변수명이나 함수명)을 정할 때 지키는 관례

+ 생성자 함수의 이름은 항상 대문자로 시작
+ 변수와 인스턴스, 함수, 메서드의 이름은 항상 소문자로 시작
+ 여러 단어로 구성될 경우 각 단어의 첫 글자를 대문자로 한다

```javascript
updateCoordinates
```

Q4. 이름 뒤에 괄호가 있는 경우, 없는 경우

```javascript
alert('Hello World')        // 함수
Array.length                // 속성
input                       // 변수
prompt('Message', 'Defstr') // 함수
Math.PI                     // 속성
Math.abs(-273)              // 메서드
```

Q5. 주석

```javascript
<script>
    // 한 줄 주석

    /*
    여러 줄
    주석
    */
</script>
```

---

Q6. alert() 함수를 이용한 출력 연습

+ 코드 에디터로 작성해도 되지만 온라인 에디터인 [JSFiddle](https://jsfiddle.net)을 이용해보자.

```javascript
<script>
    alert("출력 테스트");
</script>
```

```javascript
<script>
    alert("2 + 3 = " 2 + 3);
</script>
```

```javascript
<script>
    alert(52 < 51);
    alert(52 < 53);
    alert(52 != 50);
    alert('가방' > '하마');
    alert(true > false);
</script>
```

> **Note**: true = 1, false = 0

Q7. if 문을 이용한 alert 출력 연습

```javascript
<script>
    if (200 < 100) {
        alert("200은 100보다 작습니다.");
    }
    if (200 > 100) {
        alert("200은 100보다 큽니다.");
    }
</script>
```

Q8. 변수 생성 및 사용

+ `var` 키워드 뒤에 이름을 쓰면 해당 이름은 변수가 된다.

```javascript
<script>
    var pi = 3.14152965;

    alert(pi);
</script>
```

Q9. 자바스크립트의 여러 가지 자료형을 변수로 만들기

```javascript
<script>
    var stringVar = 'String';
    var numberVar = 273;
    var booleanVar = true;
    var functionVar = function () {};
    var objectVar = {};
</script>
```

Q10. 복합 대입 연산자

```javascript
<script>
    var value = 10;

    value += 10; // -=, *=, /=, %=

    alert(value);
</script>
```

Q11. 증감 연산자

```javascript
<script>
    var value = 10;

    value++; // 변수++, ++변수, 변수--, --변수

    alert(value);
</script>
```
```javascript
<script>
    var value = 10;

    alert(value++);
    alert(value++);
    alert(value++);
    alert(value);
</script>
```

> **Note**: 문장을 실행하기 전에 연산을 한다 또는 문장을 실행한 후 연산을 한다

```javascript
<script>
    var value = 10;

    alert(value++);
    alert(++value);
    alert(value--);
    alert(--value);
</script>
```

Q12. 자료형 검사

```javascript
<script>
    alert(typeof ('String'));
    alert(typeof (273));
    alert(typeof (true));
    alert(typeof (function () {}));
    alert(typeof ({}));
    alert(typeof (alpha));   // undefined 선언되지 않은 변수
</script>
```

---

Q13. prompt() 함수를 사용한 입력 연습

```javascript
<script>
    var input = prompt('Message', 'DefStr');

    alert(input);
</script>
```

Q14. confirm() 함수를 사용한 불 자료형 입력 연습

```javascript
<script>
    var input = confirm('수락하시겠습니까?');

    alert(input); // 사용자가 [확인]을 누르면 true를 리턴하고, [취소]를 누르면 false를 리턴한다.
</script>
```

---

Q15. 숫자 자료형을 문자열 자료형으로 자동 변환

```javascript
<script>
    alert('52 + 273');
    alert(52 + 273);
    alert('52' + 273);
    alert(52 + '273');
    alert('52' + '273');
</script>
```

Q16. 문자열 자료형을 숫자 자료형으로 자동 변환

```javascript
<script>
    alert('52 * 273');
    alert(52 * 273);
    alert('52' * 273);
    alert(52 * '273');
    alert('52' * '273');
</script>
```

**END**

---

### 01주차 자바스크립트 개요

Q1. 자바스크립트를 공부하면 할 수 있는 분야?

+ 웹 페이지 개발

2010년 이후

+ 웹 서버 개발
+ 게임 개발
+ 데스크톱 애플리케이션 개발
+ 모바일 애플리케이션 개발
+ 데이터베이스 관리
+ IoT 개발

> **Note**: 웹 페이지 = 웹 클라이언트 애플리케이션 or 웹 서버 애플리케이션

Q2. 자바스크립트의 역사

+ 원래 이름: 모카
+ 모카 → 라이브스크립트 → 자바스크립트

Q3. 웹 개발로서 자바스크립트의 의미

+ 웹 문서의 내용을 동적으로 바꾼다.
+ 사용자가 마우스를 클릭하는 것과 같은 이벤트를 처리한다.
+ 결국 정적인 [웹 문서]가 [웹 애플리케이션]으로 진화하는데 핵심 역할을 하고 있다.

> **Note**: 웹 애플리케이션의 대표적인 예시 : 구글 독스, 크롬 웹 스토어 앱

Q4. 자바스크립트로 개발한 대표적인 예시 (언어)

+ 웹 서버 개발: LinkedIn
+ 게임 개발: (Unity Script)
+ 데스크톱 애플리케이션 개발: Atom, Slack, Visual Studio Code, WordPress
+ 모바일 애플리케이션 개발: (React Native)
+ 데이터베이스 관리: (MongoDB)
+ IoT 개발: 아두이노

---

Q5. 자바스크립트 오류 확인하는 방법

+ 크롬에서 F12 또는 Ctrl + Shift + I 키를 누른다.
+ 코드에 오류가 있다면 경고 메시지가 나타난다.
+ 아래 코드에서 주석을 행동에 옮긴 후 index.html 파일을 만들어서 크롬으로 실행해본다.

```javascript
<head>
</head>
<body>
    <script>
        alert('Hello World..!') // 닫는 괄호를 삭제한다.
    </script>
</body>
```

**END**

---
