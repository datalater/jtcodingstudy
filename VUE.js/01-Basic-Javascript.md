ⓒ JMC 2018

**Source**: 모던 웹을 위한 JavaScript, jQuery 입문, 윤인성 (3판)

---

### 04주차 함수의 매개변수와 리턴

Q1. alert() 함수에서 매개변수를 더 많이 사용할 경우

```html
<script>
    alert('원래 매개변수입니다', '추가 매개변수입니다.');
</script>
```

+ 원래 alert() 함수는 매개변수 하나만 사용할 수 있다. 원래 선언할 수 있는 매개변수보다 많은 수를 선언하면 일반적으로 추가된 매개변수는 무시한다.

Q2. 매개변수의 개수에 따라 달라지는 함수

```html
<script>
    var array1 = Array();
    var array2 = Array(10);
    var array3 = Array(273, 103, 57, 32);

    alert(array1 + '\n' + array2 + '\n' + array3);
</script>
```

+ Array(): 빈 배열을 만든다.
+ Array(number) : 매개변수 값만큼의 길이를 가지는 배열을 만든다.
+ Array(any, ..., any): 매개변수를 요소로 하는 배열을 만든다.
+ 이렇게 매개변수의 개수가 변할 수 있는 함수를 '**가변 인자 함수**'라고 부른다.

Q3. 가변 인자 함수 만드는 방법



---

### 04주차 함수

Q1. 함수란 무엇인가

+ 재사용할 수 있는 코드 묶음이다.

Q2. 함수 기본 용어

번호  | 설명 | 개념
--|---|--
 1 | 함수 내부의 코드를 실행하는 행동 | 호출  
 2 | 함수를 호출할 때 괄호 안에 적는 것 | 매개변수  
 3 | 함수를 실행한 결과로 나오는 것 | 리턴
 4 | 함수의 매개변수로 함수를 전달할 때 매개변수 함수를 지칭하는 말 | 콜백 함수  

Q3. 기본 함수 만들기

+ 변수를 함수로 만들어보자.

```html
<script>
    // 함수를 만든다.
    var askNumber = function () {
        var output = prompt('숫자를 입력하세요.');
        alert(output + "을 입력하셨습니다.");
    }
    // 함수를 호출한다.
    askNumber()
</script>
```

+ 일반적으로 함수를 선언하는 방식은 다음과 같다.

```html
<script>
    // 함수를 만든다.
    function askNumber() {
        var output = prompt('숫자를 입력하세요.');
        alert(output + "을 입력하셨습니다.");
    }
    // 함수를 호출한다.
    askNumber()
</script>
```

Q4. 익명 함수

+ function () {} 형태는 함수지만 이름이 없으므로 '익명 함수'라고 부른다. 이름이 없으므로 변수에 넣어 사용해야 한다.

```html
<script>
    // 함수를 만든다.
    var askNumber = function () {
        var output = prompt('숫자를 입력하세요.');
        alert(output + "을 입력하셨습니다.");
    }
    // 함수를 호출한다.
    askNumber()
</script>
```

Q5. 선언적 함수

+ 함수의 이름이 function 뒤에, 소괄호 앞에 있다. 이게 일반적인 방식이다.

```html
<script>
    // 함수를 만든다.
    function askNumber() {
        var output = prompt('숫자를 입력하세요.');
        alert(output + "을 입력하셨습니다.");
    }
    // 함수를 호출한다.
    askNumber()
</script>
```

Q6. 익명 함수와 선언적 함수의 실행 우선 순위

+ **웹 브라우저는 선언적 함수부터 읽는다**.

```html
<script>
    함수();
    var 함수 = function () { alert('함수 A'); };
    var 함수 = function () { alert('함수 B'); };
</script>
```

+ 위 코드는 변수를 선언하기 이전에 변수를 사용했기 때문에 오류가 발생해 실행되지 않는다.

```html
<script>
    함수();
    function 함수() { alert('함수 A'); };
    function 함수() { alert('함수 B'); };
</script>
```

+ 위 코드에서는 함수 B를 출력하게 된다. 따라서 위 코드는 첫 줄부터 실행하는 것이 아니라 2번째 줄, 3번째 줄, 1번째 줄의 순서로 실행됩니다.


Q7. 매개변수와 리턴 값을 갖는 함수를 만들어 보자.

```html
<script>
    function f(x) {return x * x; }

    alert(f(3));
</script>
```

Q8. 짝수와 홀수를 알려주는 함수를 만들어 보자.

```html
<script>
    function f(x) {
        if (x % 2 == 0) {
            result = "짝수입니다."
        } else {
            result = "홀수입니다."
        }
    }

    var x = Number(prompt("숫자를 입력하세요."));
    var result = "";

    f(x)
    alert(result);
</script>
```

**END**

---

### 03주차 반복문과 배열

Q1. 반복문의 힘

+ 컴퓨터가 인간에 비해 월등히 뛰어난 능력이 '반복'이다.
+ `alert('출력');`을 100번 실행해보자.

```html
<script>
    for (var i = 0; i < 100; i++) {     // 100 = 반복횟수
        alert(i + '번째 출력');          // alert 문장을 실행한 이후에 i+=1이 된다.
    }
</script>
```

+ `alert('버그 아님');`을 29번 실행해보자.

Q2. 여러 개의 변수를 한꺼번에 다룰 수 있는 자료형인 배열을 알아보자.

+ 배열은 객체 자료형에 속한다.
+ 배열은 대괄호로 생성한다.

```html
<script>
    var array = ["Jay", "0123", "Will", "0202"]
</script>
```

+ 배열을 출력해보자.

```html
<script>
    var array = ["Jay", "0123", "Will", "0202"]

    alert(array)
</script>
```

+ 배열의 요소에 접근해보자.

```html
<script>
    var array = ["Jay", "0123", "Will", "0202"]

    alert(array[0]);
    alert(array[1]);
    alert(array[2] + "의 생일은 " + array[3] + "입니다.")
</script>
```

Q3. 배열이라는 객체의 속성과 메서드는

+ 속성: 특정 객체가 갖고 있는 변수
+ 메서드: 특정 객체가 갖고 있는 함수

+ 배열의 길이를 알려주는 length 속성을 출력해보자.

```html
<script>
    var arrayA = [0, 1, 2, 3];
    var arrayB = [0, 1, 2, 3, 4, 5, 6];

    alert("length of A: " + arrayA.length);
    alert("length of B: " + arrayB.length);
</script>
```

+ 배열의 요소를 추가하는 push() 메서드를 실행해보자.

```html
<script>
    var array = [0, 1];

    array.push(2);
    array.push(3);

    alert(array);
</script>
```

Q4. while 반복문 활용하기

+ 자바스크립트의 가장 간단한 반복문이다. if 조건문과 형태가 비슷하다.
+ 불 표현식이 참인 동안 지속적으로 문장을 실행한다.

```html
<script>
    var value = 0;

    while (value < 5) {
        alert(value+ '번째 반복');
        value++
    }
</script>
```

+ 경고창(alert)을 다섯 번 출력한다.
+ 시간으로 조건을 변화시켜 반복문을 설정할 수도 있다.

```html
<script>
    var value = 0;
    var startTime = new Date().getTime();

    while (new Date().getTime() < startTime + 1000) { value++; }

    alert(value);
</script>
```

+ 1000밀리 초 (1초) 동안 `value++;`을 실행한다.

Q5. do while 반복문 활용하기

+ while 반복문은 조건을 먼저 검사하고 코드 블록을 반복한다.
+ do while 반복문은 내부의 문장을 최소한 한 번을 실행하고 코드 블록을 반복한다.

```html
<script>
    var value = 0;

    do {
        alert(value + '번째 반복문');
        value++;
    } while (value < 5)
</script>
```

+ 예를 들어 '사용자에게 전화번호를 물어보고, 전화번호 형식이 아니라면 전화번호 형식을 입력할 때까지 반복'하는 경우가 있다. 적어도 한 번은 일단 물어보고 시작해야 하므로 do while 반복문을 사용할 수 있다.

Q6. for 반복문 활용하기

+ while 반복문이 조건에 비중을 둔다면 for 반복문은 횟수에 비중을 둔다.

```html
<script>
    for (초기식; 조건식; 종결식;) {
        문장
    }
</script>
```

+ (1) 초기식을 실행한다.
+ (2) 조건식을 비교한다. 조건이 거짓이면 반복문을 종료한다.
+ (3) 문장을 실행한다.
+ (4) 종결식을 실행한다.
+ (5) 2단계로 간다.

```html
<script>
    for (var i = 0; i < 5; i++) {
        alert(i + '번째 반복');
    }
</script>
```

+ 배열의 요소를 반복문으로 모두 출력하기

```html
<script>
    var array = ['원숭이 엉덩이', '빨개', '사과', '맛있어', '바나나', '길어', '기차']

    for (var i = 0; i < array.length; i++) {
        alert(array[i])
    }
</script>
```

+ 배열의 요소를 역으로 출력할 수도 있다.

```html
<script>
    var array = ['원숭이 엉덩이', '빨개', '사과', '맛있어', '바나나', '길어', '기차']

    for (var i = array.length - 1; i >= 0; i--) {
        alert(array[i])
    }
</script>
```

+ 배열의 인덱스는 0부터 시작하므로 마지막 요소를 출력하려면 array.length에서 1을 빼줘야 한다.

Q6-1. for in 반복문 (인덱스)

+ 하지만 배열을 반복문에서 다룰 때는 for in 반복문을 사용하는 것이 효율적이다.

```html
<script>
    var array = ['원숭이 엉덩이', '빨개', '사과', '맛있어', '바나나', '길어', '기차']

    for (var i in array) {
        alert(array[i])
    }
</script>
```

+ for in 반복문에 배열을 넣으면, 반복변수 i에 '요소'가 아니라 '인덱스'가 들어간다.

Q6-2. for of 반복문 (요소)

+ 반복변수 i에 '요소'가 들어간다.

```html
<script>
    for (var i of [1, 2, 3, 4]) {
        alert(i)
    }
</script>
```

Q7. 브라우저의 성능을 측정하는 프로그램 만들기

+ 아래 코드에서 추가로 for 반복문을 사용해서 1초 동안 반복문이 몇 회 반복되는지 표시해 브라우저의 성능을 측정해보자.

```html
<script>
    var startTime = new Date().getTime(); // 현재 시간 구하기
</script>
```

+ 정답

```html
<script>
    var startTime = new Date().getTime();

    for (var speed = 0; new Date().getTime() < startTime + 1000; speed++) {}
    alert('초 당 연산 횟수: ' + speed);
</script>
```

Q8. 중첩 반복문 (1)

+ 10층 짜리 별 트리를 만들어라. 1층에 별 1개, 2층에 별 2개, ...
+ 책 저자도 처음 프로그래밍을 배울 때는 이 예제를 직접 완성하지 못하고 결국 답지를 보았다고 한다. 또 일을 5년 정도 하다가 동료들과 이야기가 나와서 만들어봤는데 또 못 만들겠다고 하더라. 원래 어려운 것이니 만들지 못해도 크게 낙심하지 말자.
+ 정답

```html
<script>
    var output = '';

    for (var i = 0; i < 10; i++) {
    	for (var j = 0; j < i; j++) {
      	output += "*";
      }
      output += "\n";
    }

    alert(output);
</script>
```

Q9. 중첩 반복문 (2)

+ 별 트리가 가운데 정렬되도록 만들어라.
+ 정답

```html
<script>
    var output = '';

    for (var i = 0; i < 15; i++) {
        for (var j = 15; j > i; j--) {
            output += " ";
        }
        for (var k = 0; k < 2 * i - 1; k++) {
            output += "*";
        }
        output += "\n";
    }

    alert(output);

</script>
```

Q10. break 키워드

+ 반복문을 벗어난다.

```html
<script>
    for (var i = 0; true; i++) {
        alert(i + '번째 반복문입니다.');

        if (!confirm('계속하시겠습니까?')) {
            break;
        }
    }
    alert('프로그램 종료');
</script>
```

Q11. continue 키워드

+ 현재 반복을 멈추고 다음 반복을 진행시킨다.

```html
<script>
    for (var i = 0; i < 5; i++) {
        continue;
        alert(i)
    }
</script>
```
+ 0~10까지 중에서 홀수이면 다음 반복문으로 넘어가고 짝수이면 누적시켜서 합을 구하는 프로그램을 만들어보자.

```html
<script>
    var output = 0;

    for (var i = 0; i <= 10; i++) {
        if (i % 2 == 1) {
            continue
        }
        output += i;
    }
    alert (output);
</script>
```

Q12. 연습문제

+ (1) 1부터 100까지 더하는 프로그램을 만들어보자.

```html
<script>
    var output = 0;

    for (var i = 1; i <= 100; i++) {
        output +=i
    }
    alert(output);
</script>
```

+ (2) 사용자에게 입력을 받아 특정한 숫자부터 특정한 숫자까지 더하는 프로그램을 만들어보자.

```html
<script>
    var output = 0;
    var startNum = Number(prompt("시작 숫자를 입력하세요."))
    var endNum = Number(prompt("마지막 숫자를 입력하세요."))

    for (var i = startNum; i <= endNum; i++) {
        output += i
    }

    alert(output)
</script>
```

+ (3) [52, 273, 103, 32, 57, 103, 31, 2]와 같은 숫자 배열에서 최대값과 최소값을 찾는 코드를 작성해보자.

```html
<script>
    var arrayA = [52, 273, 103, 32, 57, 103, 31, 2]

    var maxValue = arrayA[1];
    var minValue = arrayA[1];

    for (var element of arrayA) {
        if (element > maxValue) {
            maxValue = element;
        }
        if (element < minValue) {
            minValue = element;
        }
    }
    alert(maxValue + ", " + minValue);

</script>
```

**END**

---

### 02주차 조건문

Q1. JMC가 28세 인데 19세 이상일 경우 주류를 판매할 수 있다는 메시지를 alert() 함수로 출력해보자. (단, 템플릿 문자열을 사용해보자)

```javascript
<script>
    var jmc = 28;
    if (jmc > 19) {
        alert(`jmc는 ${jmc}세이므로 주류를 구매할 수 있습니다.`)
    }
</script>
```

+ 이번에는 사용자의 나이를 직접 입력 받아서 Q1과 같은 메시지를 출력해보자.

```javascript
<script>
    var userAge = Number(prompt('나이를 입력하세요', 'ex. 19'));

    if (userAge > 19) {
        alert(`고객님은 ${userAge}세이므로 주류를 구매할 수 있습니다.`)
    }
</script>
```

Q2. 현재 시각에 따라 오전과 오후를 구분하는 프로그램을 만들어보자.

+ 현재 시각을 구하는 코드는 다음과 같다.

```javascript
var date = new Date();
var hour = date.getHours();
```

+ 정답

```javascript
<script>
    var date = new Date();
    var hour = date.getHours();

    if (hour >= 12) {
    	alert(`현재 시간은 ${hour}시이므로 오후입니다.`)
    }
    else {
    	alert(`현재 시간은 ${hour}시이므로 오전입니다.`)
    }
</script>
```

Q3. 현재 날짜에 따라 3-5월이면 봄, 6-8월이면 여름, 9-11월이면 가을, 12-2월이면 겨울로 계절을 구분하는 프로그램을 만들어보자.

+ 현재 날짜(월)를 구하는 코드는 구글링을 직접 해본다.
+ 정답

```javascript
<script>
    var date = new Date();
    var month = date.getMonth()+1; // january = 0

    if (5>= month && month >=3) {
    	alert(`현재 날짜는 ${month}월이므로 봄입니다.`)
    }
    else if (8 >= month && month >= 6) {
    	alert(`현재 날짜는 ${month}월이므로 여름입니다.`)
    }
    else if (11 >= month && month >= 9) {
    	alert(`현재 날짜는 ${month}월이므로 가을입니다.`)
    }
    else {
    	alert(`현재 날짜는 ${month}월이므로 겨울입니다.`)
    }
</script>
```

+ `5>= month >=3` 이런 식으로 하면 안 되는 이유를 반드시 알고 넘어가자.

Q4. 삼항 연산자 조건문

+ 삼항 연산자의 기본 형태

```javascript
// 불 표현식 ? 참일 때 실행하는 문장 : 거짓일 때 실행하는 문장
(number > 0) ? alert('0보다 큽니다.') : alert('0보다 크지 않습니다');
```

Q5. 이항 연산자 조건문

+ 이항 연산자의 기본 형태

```javascript
// 불 표현식 || 거짓일 때 실행할 문장
// 불 표현식 && 참일 때 실행할 문장

true || false;
false || anything;

true || alert('실행될까요 A');
false || alert(' 실행될까요 B');
```

+ 논리합 연산자(||, or)는 좌변이 참이면 우변을 실행하지 않는다. (원리)
+ 논리합 연산자(||, or)는 좌변이 거짓이면 우변을 실행한다. (적용)

```javascript
// 불 표현식 || 거짓일 때 실행할 문장
// 불 표현식 && 참일 때 실행할 문장

true && alert('실행될까요 A');
false && alert(' 실행될까요 B');
```

+ 논리합 연산자(||, or)는 좌변이 거짓이면 우변을 실행하지 않는다. (원리)
+ 논리합 연산자(||, or)는 좌변이 참이면 우변을 실행한다. (적용)

```html
<script>
    var input = Number(prompt('숫자를 입력해주세요.'));

    input % 2 == 0 || alert('홀수입니다'); // 0으로 나눠지지 않으면 홀수입니다.
    input % 2 == 0 && alert('짝수입니다'); // 0으로 나눠지면 짝수입니다.
</script>
```

+ 다른 조건문 코드와 비교했을 때 이해하기 어려우므로 이항 연산자 조건문은 많이 사용하지는 않는다.

Q6. indexOf() 메서드

```html
<script>
    var output = "안녕하세요".indexOf("안녕");

    alert(output);
</script>
```

+ indexOf() 메서드는 앞에 있는 문자열 에 뒤에 있는 문자열이 포함되어 있을 경우 위치를 출력한다.
+ "안녕하세요"라는 문자열 안에 "안녕"이라는 문자열이 가장 앞에 포함되어 있다.
+ 자바스크립트는 숫자를 0부터 세기 때문에 "안녕"이라는 문자열의 위치는 0번째 위치이다.
+ 따라서 0을 출력한다.

```html
<script>
    var output = "안녕하세요".indexOf("잘자");

    alert(output);
</script>
```

+ 앞의 문자열에 뒤의 문자열이 포함되어 있지 않으면 무조건 음수(-1)로 출력한다.

Q7. indexOf() 메서드와 조건문을 활용하여 인사하는 프로그램 만들기

+ prompt() 함수로 문자열을 입력받아 "안녕"이 들어가 있으면 "안녕하세요", "잘자" 또는 "잘 자"를 입력하면 "안녕히 주무세요"를 출력하는 코드를 작성하세요. 만약, 둘 다 들어있지 않다면 "잘못 입력되었습니다"라고 출력하세요.
+ 정답

```html
<script>
    var input = prompt("인사를 해주세요.", "ex. 안녕 or 잘 자")
    if (input.indexOf("안녕") != -1) {
        alert("안녕하세요.")
    }
    else if (input.indexOf("잘 자") != 1 || input.indexOf("잘자") != 1) {
        alert("안녕히 주무세요.")
    }
    else {
        alert("잘못 입력되었습니다.")
    }
</script>
```

**END**

---

### 02주차 템플릿 문자열

Q1. 템플릿 문자열로 문자열 내부에 표현식 삽입하기

```javascript
<script>
    alert('표현식 273 + 52의 값은 ' + (273 + 52) +'입니다!!');
</script>
```

+ 표현식 결합을 많이 하면 코드가 복잡해진다.
+ ECMAScript 6부터는 '템플릿 문자열'이라는 기능을 추가해 표현식 결합을 간단하게 작성할 수 있게 되었다.

```javascript
<script>
    alert(`표현식 273 + 52의 값은 ${52 + 273}입니다!!`);
</script>
```

+ 템플릿 문자열은 "\`" 기호로 감싸 만들며, 문자열 내부에 "${}" 기호를 사용합니다.

> **Note**: ECMAScript는 유럽 컴퓨터 제조협회(European Computer Manufacturer's Association)가 정한 자바스크립트의 표준 명칭이다. 하지만 자바스크립트라는 용어를 더 오래 사용해왔으므로 일반적으로 자바스크립트라는 명칭을 쓰고, 자바스크립트의 표준 버전이 달라질 때는 ECMAScript 6 이런 식으로 표기한다.

```javascript
<script>
    var variable = 273;
    alert(`변수 variable의 값은 ${variable}`입니다.)
</script>
```

+ 굉장히 편리한 기능이지만 모든 버전의 인터넷 익스플로러에서 사용이 불가능하다. 따라서 모든 버전의 인터넷 익스플로러에 대응해야 하는 웹 페이지를 만들 때는 주의해서 사용해야 한다.

**END**

---

### 01주차 기본 문법 (2)

Q1. 이름(식별자)을 지을 때 알야아 하는 규칙

+ 키워드를 사용하면 안 된다. ex. if, return, typeof, var
+ 숫자로 시작하면 안 된다. ex. 10hakbun
+ 특수문자는 언더스코어( _ )와 달러( $ )만 허용한다.
+ 공백 문자를 포함하면 안 된다. ex. change title

```javascript
// 아래는 모두 이름으로 사용할 수 있다.
alpha
alpha10
_alpha
$alpha
Alpha
ALPHA
```

Q2. 자바스크립트에서 정해진 키워드(예약어)를 한 번 훑어보고 넘어가자.

```javascript
true    false       var             if          this        while       with
do      delete      in              throw       try         finally     catch
new     break       instanceof      typeof      return      delete      void
```

```javascript
abstract    debugger    goto            Native          super
await       double      implements      package         synchronized
boolean     enum        import          private         throws
byte        export      int             protected       transient
char        extends     interface       public          volatile
class       final       let             short           yield
const       float       long            static          
```

+ 절대 외울 필요없이 그냥 단기 기억으로 스쳐 지나가자.

Q3. 이름 vs 함수 구분하는 법

+ 이름 뒤에 괄호 있으면 함수    ex. alert()
+ 이름 뒤에 괄호 없으면 변수    ex. input

Q4. 이스케이프 문자

+ 따옴표는 원래 문자열을 만들 때 사용한다. 그런데 따옴표 자체를 문자열로 쓰고 싶을 때가 있다.

```javascript
alert("This is \"string\"");
```

+ 이스케이프 문자(\, 백슬래시)를 앞에 써주면 된다.

Q5. 이스케이프 문자의 특수 기능

```javascript
alert('동해물과 백두산이\n마르고 닳도록');
```

+ 이스케이프 문자 `\n`을 사용하면 문자열을 줄 바꿈 한다.
+ 이스케이프 문자: `\t`, `\n`, `\'`, `\"`, `\\`

> **Note**: 일부 웹 브라우저는 경고창에서 `'\t'`를 인식하지 않을 수 있다.

Q6. 비교 연산자

+ `>=`
+ `<=`
+ `==`
+ `!=`

Q7. 비교 연산자와 문자열 자료형

+ 비교 연산자로 문자열 자료형도 비교할 수 있다.
+ 문자열 자료형은 국어사전의 앞쪽에 있을수록 값이 작아진다.

Q8. 논리 연산자

+ `!` : not
+ `&&` : and
+ `||`: or

```javascript
alert(!true);
alert(true && true)
alert(true || false)
```

Q9. 3개 이상의 숫자 자료형의 크기를 비교할 때

+ 비교 연산자와 논리 연산자를 함께 사용해야 정확하게 확인할 수 있다.
+ 비교 연산자만 사용한다면 원하지 않는 결과가 발생할 수 있다.

```javascript
alert(30 > 20 > 10);
```

+ 비교 연산자가 여러 개 있을 경우 왼쪽부터 차례대로 연산하면서 참과 거짓을 판단한다.
+ alert((30 > 20) > 10);
+ alert(true > 10);
+ alert(1 > 10);
+ alert(false);

```javascript
alert(30 > 20 && 20 > 10);
```

+ alert(true && true);
+ alert(true);

Q10. undefined 자료형

```javascript
alert(typeof(variable));
```

+ 선언

```javascript
var variable;
alert(typeof(variable));
```

+ 선언 + 초기화

```javascript
var variable = "변수";
alert(typeof(variable));
```

**END**

---

### 01주차 기본 문법 (1)

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

+ 숫자와 문자열을 덧셈하면 숫자를 문자열로 자동 변환한다.

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

+ 덧셈을 제외한 사칙 연산자는 문자열을 숫자로 자동 변환한다.

Q17. 강제 변환

+ Number() : 다른 자료형을 숫자로 바꾼다.
+ String() : 다른 자료형을 문자열로 바꾼다.

```javascript
<script>
    var input = prompt('숫자를 입력해주세요.', '숫자');

    alert(typeof(input))
</script>
```

```javascript
<script>
    var input = prompt('숫자를 입력해주세요.', '숫자');
    var numberInput = Number(input);

    alert(typeof(numberInput) + ': ' + numberInput);
</script>
```

```javascript
<script>
    var numberInput = Number(prompt('숫자를 입력해주세요.', '숫자'));

    alert(typeof(numberInput) + ': ' + numberInput);
</script>
```

> **Note**: 숫자가 아닌 값을 입력한 경우 NaN(Not a Number)값을 출력한다. `alert(Math.sqrt(-3));`

+ Boolean() : 다른 자료형을 불 자료형으로 바꾼다.

```javascript
<script>
    alert(Boolean(0));
    alert(Boolean(NaN));
    alert(Boolean(''));
    alert(Boolean(null));
    alert(Boolean(undefined));
    alert(Boolean('false'));
</script>
```

Q18. 일치 연산자

```javascript
<script>
    alert('' == false);
    alert('' == 0);
    alert(0 == false);
    alert('273' == 273);
</script>
```

+ 비교 연산자를 사용하면 자동으로 자료형이 변환되어 네 가지 모두 true를 출력한다.
+ 자동으로 자료형이 변환되는 것을 막고 원하는 자료형을 확실하게 구분짓고 싶다면 일치 연산자를 사용한다.

```javascript
<script>
    alert('' === false);
    alert('' === 0);
    alert(0 === false);
    alert('273' === 273);
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
