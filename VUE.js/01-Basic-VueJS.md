ⓒ JMC 2018

---

### 2주차 VueJS 템플릿에서 directive 사용하기

"HTML attribute에는 curly braces를 쓸 수 없다"

Q1. 구글로 이동하는 링크 (anchor 태그)를 만들어보자.

```html
<script src="https://unpkg.com/vue/dist/vue.js"></script>

<div id="app">
  <p> {{ title }} </p>
  <p> {{ sayHello() }} - <a href="{{ link }}">Google</a></p>
</div>
```

```javascript
new Vue({
    el: "#app",
    data: {
        title: 'Hello JMC',
        link: 'http://www.google.com'
    },
    methods: {
  	     sayHello: function() {
    	   return this.title
        }
    }
})
```

+ 실행하면 잘 안 될 것이다. (새 탭으로 열기 실행)
+ 명심하자 HTML attribute (="attribute")에는 절대 curly braces를 넣으면 안 된다.
+ curly braces를 쓸 수 있는 곳은 HTML에서 text를 쓸 수 있는 곳에 한정된다.
+ HTML elemet에는 curly braces를 쓸 수 없다.
+ 이럴 때는 directive를 쓰면 된다.

Q2. VueJS directive 사용하기

+ directive란 VueJS로 바로 연결시키는 도구를 뜻한다.
+ directive에는 여러 종류가 있는데 여기서는 `v-bind`를 쓴다.

```html
<script src="https://unpkg.com/vue/dist/vue.js"></script>

<div id="app">
  <p> {{ title }} </p>
  <p> {{ sayHello() }} - <a v-bind:href="link">Google</a></p>
</div>
```

```javascript
new Vue({
    el: "#app",
    data: {
        title: 'Hello JMC',
        link: 'http://www.google.com'
    },
    methods: {
  	     sayHello: function() {
    	   return this.title
        }
    }
})
```

+ `v-bind:argument`: 해당 argument를 HTML 일반 방식으로 실행하지 않고 binding 해서  VueJS로 연결시킨다.
+ `v-bind:href="link"`: href는 VueJS 인스턴스로 가서 link를 찾는다. 그러므로 따옴표 안에는 VueJS의 인스턴스의 property를 넣어야 한다.

Q3. 2주차 학습 목표

+ Q. directive에 대한 이해 및 활용



---

### 2주차 VueJS 템플릿 이해하기 및 VueJS 인스턴스 접근하기

Q1. html에서 쓰는 VueJS 문법

+ `{{ title }}`
+ double curly braces: interpolation 또는 string interpolation이라 부른다.

Q2. html과 VueJS 템플릿의 소통 방식

+ HTML → VueJS → VueJS Template → final rendered HTML
    + html과 vue 인스턴스가 연결된다.
    + html에 vue 템플릿을 rendering 한다.
    + 클라이언트는 vue 템플릿이 rendering된 HTML 코드를 보게 된다.
    + 따라서 해당 렌더링된 페이지에서 크롬 f12 개발자도구를 열어 봐도 curly brace은 보이지 않는다.

Q3. VueJS template에 data의 오브젝트 출력하는 방법

```html
<!-- html -->

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<div id="app">
    <p>{{ title }}</p>
</div>
```

```javascript
// javascript

new Vue({
    el: '#app',
    data: {
        title: 'Hello World!'
    }
})
```

+ html에서 `{{ this.title }}`이나 `{{ data.title }}`로 적지 않고, `{{ title }}`이라고 적어준다. data의 오브젝트는 모두 이런 식으로 접근 가능하다. 오토 파싱.

Q4. VueJS template에 methods의 오브젝트 출력하는 방법

```html
<!-- html -->

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<div id="app">
    <p>{{ title }}</p>
    <p>{{ sayhello() }}</p>
</div>
```

```javascript
// javascript

new Vue({
    el: '#app',
    data: {
        title: 'Hello World!'
    },
    methods: {
        sayHello: function() {
            return "Hello JMC"
        }
    }
})
```

+ 마찬가지로 methods의 오브젝트도 그대로 적어주면 된다. 단 함수이므로 괄호를 빼먹지 않도록 한다.

Q5. VueJS instance에서 오브젝트 출력하는 방법

```html
<!-- html -->

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<div id="app">
    <p>{{ title }}</p>
    <p>{{ sayhello() }}</p>
</div>
```

```javascript
// javascript

new Vue({
    el: '#app',
    data: {
        title: 'Hello World!'
    },
    methods: {
        sayHello: function() {
            return title
        }
    }
})
```

+ 위처럼 하면 안 된다.

```javascript
// javascript

new Vue({
    el: '#app',
    data: {
        title: 'Hello World!'
    },
    methods: {
        sayHello: function() {
            return this.title
        }
    }
})
```

+ 템플릿과 달리 vuejs 코드 안에서는 해당 인스턴스(this)를 명시해줘야 한다.
+ this.data.title이라고 적을 필요가 없는 이유는 this만으로도 title에 알아서 접근 가능하기 때문이다.

**END**

---

### 1주차 로컬로 작업하기

Q1. 로컬 컴퓨터에서 Vue.js 작업하는 방법

+ [Vue.js](vuejs.org) 접속
+ Get started 버튼 클릭
+ 좌측 사이드에서 installation 클릭
+ Standalone - development version - 클릭 및 다운로드
+ 다운로드 한 위치에서 에디터 실행
+ html 파일 작성 후 index.html로 파일 저장 (https://jsfiddle.net/smax/c4mcxu7s/)

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>VueJS</title>
    <link rel="stylesheet" href="">
    <script src="vue.js"></script>
</head>
<body>
    <div id="app">
        <input type="text" v-on:input="changeTitle">
        <p>{{ title }}</p>
    </div>

    <script>
        new Vue({
            el: '#app',
            data: {
                title: "Hello JMC"
            },
            methods: {
                changeTitle: function(event) {
                    this.title = event.target.value;
                }
            }
        });
    </script>
</body>
</html>
```

+ vue.js 파일과 index.html 파일이 한 디렉토리에 있는 것을 확인한 후 index.html 브라우저로 실행

**END**

---

### 1주차 VueJS 애플리케이션 만들기

Q1. Vue.js 오피셜 홈페이지에 접속한다.

+ [Vue.js](vuejs.org) 접속
+ Get started 버튼 클릭
+ 좌측 사이드에서 installation 클릭
+ #CDN 복사

    `<script src="https://cdn.jsdelivr.net/npm/vue@2.5.16/dist/vue.js"></script>`

> **Note**: 최신 버전 자동 매칭 : `<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>`

Q2. jsfiddle.net에 접속한다.

+ [jsfiddle](https://jsfiddle.net) 접속
+ HTML 섹션을 클릭한다.
+ 타이핑으로 script 치고 tab 누른다. 태그가 자동완성 된다.
+ source attribute를 적어준다.

```html
<!-- html -->

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<div id="app">
    <p></p>
</div>
```

Q3. new 키워드로 Vue 인스턴스를 만들어준다.

+ new 키워드로 Vue 인스턴스를 만든다.

```javascript
// javascript

new Vue()
```

+ Vue 인스턴스의 argument는 javascript의 object를 넣어준다.

```javascript
// javascript

new Vue({

})
```

+ 첫 번째 property(속성)로 el을 넣어준다.
+ el은 HTML의 어떤 element(템플릿)를 컨트롤 할 것인지 그 대상을 string으로 설정한다.

```javascript
// javascript

new Vue({
    el: ''
})
```

+ el의 대상은 CSS selector로 지정할 수 있다.

```javascript
// javascript

new Vue({
    el: '#app'
})
```

+ 화면(template)에 출력할 데이터에 대한 property가 필요하다.
+ data는 그 대상을 object로 설정한다.

```javascript
// javascript

new Vue({
    el: '#app',
    data: {

    }
})
```

+ 현재 Vue 인스턴스에 title이라는 data를 저장한다고 해보자.

```javascript
// javascript

new Vue({
    el: '#app',
    data: {
        title: 'Hello World!'

    }
})
```

+ title을 템플릿(화면)에 출력해보자.

```html
<!-- html -->

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<div id="app">
    <p>{{ title }}</p>
</div>
```

+ jsfiddle에서 ctrl + enter를 눌러본다.
+ 작동 원리: html에 있는 `{{ title }}`이 Vue 인스턴스에서 해당하는 title property를 찾아서 출력한 것이다.

Q4. input field 추가하기

+ html 섹션에서 p 태그 윗줄에 타이핑으로 input을 치고 tab을 눌러 자동완성시킨다.

```html
<!-- html -->

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<div id="app">
    <input type='text'>
    <p>{{ title }}</p>
</div>
```

Q5. input field에 사용자가 입력하는 내용을 title의 내용으로 출력해보자.

+ v-on: Vue.js야 해당 태그의 event를 listening 해라! event이름은 콜론 오른쪽에 있는 input이야. 그리고 실행할 method는 changeTitle이야.

```html
<!-- html -->

<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

<div id="app">
    <input type='text' v-on:input="changeTitle">
    <p>{{ title }}</p>
</div>
```

+ Vue 인스턴스에 methods property를 object로 만들어준다.

```javascript
// javascript

new Vue({
    el: '#app',
    data: {
        title: 'Hello World!'
    },
    methods: {

    }
})
```

+ 인스턴스에 속한 property는 `this.`으로 가져올 수 있다.
+ event.target : input field
+ event.target.value : input field content

```javascript
// javascript

new Vue({
    el: '#app',
    data: {
        title: 'Hello World!'
    },
    methods: {
        changeTitle: function(event) {
            this.title = event.target.value;
        }
    }
})
```

+ jsfiddle에서 ctrl + enter 눌러서 실행해본다.

Q6. 1주차 학습 목표

+ Q. HTML 코드와 VueJS가 어떻게 interact하는가?
    + (1) **패키지 로드**: head tag에 vuejs 스크립트 코드를 삽입한다.
    + (2) **el 연결**: html 코드의 특정 CSS selector와 Vue 인스턴스의 el이 연결된다.

**END**

---
