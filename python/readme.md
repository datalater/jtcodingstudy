© 2017 SHAKEADE

**Storingtelling Rules**
첫째, 2가 아니라 1+1까지만 보여줘라.
둘째, 결과보다 과정을 중시해라.
셋째, 테마를 초장부터 잡기는 어렵다. 쓰다 보면 잡힐 것이다.
넷째, 질문을 던지고 답변을 구하는 과정으로 진행해라.


---

# 4강 블록문, 들여쓰기, 주석

## 블록문 (Block Statement)

+ 블록문 : 연속된 코드의 묶음
+ 블록 구분 : 들여쓰기 (indent)

```
if student.age > 19:
    print("성인입니다.")

for item in bag:
    if item == '담배':
        print("흡연자 적발 완료")
```

## 들여쓰기 (Indentation)

+ Python: space 4칸 권장

```
for item in bag:
    if item == '담배':
        if student.age > 19:
            print("미성년자 흡연자 적발 완료")
```

+ HTML : space 2칸 권장

## 주석 (Comment)

+ Python: "1줄 주석" 문법만 지원

```
# naver 사이트 주소를 url로 할당하고, GET 방식으로 requests를 보낸다.

url = "http://naver.com"
requests.get(url)
```

+ "여러 줄 주석"으로 사용하는 임시 방법

```
'''이 함수는 학생의 나이를 return하기 위해서 만들었으며
미성년자 판단에 활용된다'''

# 사실 주석이 아니라 그냥 문자열이다.
# 위 코드를 실행하면 문자열로 인식하지만 변수에 저장하지는 않으므로 프로그램에 영향을 끼치지는 않는다.
```

+ "여러 줄 주석"은 실제 주석이 아니다. 문자열이다.

```
names = {
 'Tom': 10,
 'Steve': 12,
 '''
 'John': 9,
 'Anderson': 14,
 'Bell': 8,
 '''
}

# 위 코드는 SyntaxError를 발생시킨다.
```

**끝.**

---

# 3강 기본 자료구조

## 기본 자료구조

+ list, tuple, set, dict

## Container

+ 여러 원소들을 가지고 있는 자료구조
    + **list**, deque
    + **set**, frozensets
    + **dict**, defaultdict, OrderedDict, Counter
    + **tuple**, namedtuple
    + str

    > 이번 시간에는 진하게 표시된 list, set, dict, tuple만 살펴본다. 나머지도 Container 자료구조에 속한다.

+ in 연산자로 멤버십 테스트를 지원

```
>>> 'hello' in 'hello world'
True
```

## list

+ 생성문법: [], list(), list(iterable)
+ 여러 값을 순차적으로 저장, 순서를 보장
+ 리스트를 한 줄로 쓸 때에는 대개 끝에 쉼표를 쓰지 않는다.
+ 여러 줄로 나눠서 쓸 때는 끝에 쉼표를 쓴다. 항목 추가/삭제가 용이하기 때문이다.

```
numbers = [1, 3, 5, 6, 9]
names = [
    'Tom',
    'Steve',
    'Min',
]
```
+ 색인(index) 지원: 0부터 시작하여 1씩 증가

    + 음수 색인 지원: 끝에서부터 역으로 -1부터 1씩 감소

    > offset의 개념으로 접근하면 더 쉽게 알 수 있다.

+ 다른 타입의 값들로도 구성 가능
+ 한 list에 서로 다른 데이터 타입의 값을 넣을 수도 있지만, 가급적 같은 타입으로 맞춰주는 것이 보다 알기 쉬운 코드가 된다.

```
numbers = [1,3,5,7]               # 리스트 선언
print(7 in numbers)               # 멤버십 체크
print(numbers[0], numbers[-3])    # 색인 0과 -3의 값 출력
print(len(numbers))               # 리스트의 길이 출력
for i in numbers:                 # for 루프를 통해 list 내 모든 값 순회
    print(i)                      # in 뒤에는 모든 container가 올 수 있다.

bad_values = [10, 'Tom', (1,2,3)] # BAD
```

+ 범위 밖의 색인을 참조하면 IndexError 예외가 발생한다.

```
IndexError: list index out of range
```

+ 데이터 변경

```
numbers = [1, 3, 5, 7, 9]
numbers[0] = 10                    # 지정 색인의 값을 변경
numbers.append(11)                 # 끝에 값을 추가
numbers.pop(3)                     # 특정 색인의 값을 출력하고 동시에 제거
numbers.remove(5)                  # 특정 값을 1회 제거
numbers.insert(1, 11)              # 특정 위치에 값을 추가
```

+ 값을 잘라내기 (slice)
    + 콜론(:)을 붙여주면 슬라이싱한다.
    + 리스트[시작인덱스:끝인덱스:인덱스증가량]
    + 시작인덱스 이상, 끝 인덱스 미만

```
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers[1:]                        # 1번 인덱스부터 끝까지
numbers[1:8]                       # 1번 인덱스 이상 8번 인덱스 미만
numbers[:8]                        # 처음부터 8번 인덱스까지
numbers[1:8:2]                     # 2칸씩 step(간격)을 넣는다. [Out] 2, 4, 6, 8
numbers[::-1]                      # 역순으로 정렬한다.
```

+ 리스트 합치기
    + 리스트끼리 더할 수 있다.

```
>>> numbers1 = [1,3,5,7]
>>> numbers2 = [2,4,6,8]
>>> print(numbers1 + numbers2)
[1,3,5,7,2,4,6,8]
```

+ List Comprehension

```
>>> numbers1 = [1,3,5,7]
>>> numbers2 = [2,4,6,8]
>>> print([i+j for (i,j) in zip(numbers1, numbers2)])
[3,7,11,15]
```

## tuple

+ 생성문법: (), tuple(), tuple(iterable)

+ list와 유사하지만 변경 불가능(immutable)한 특성 : 추가, 삭제, 변경이 없음


+ 소괄호는 때에 따라, 우선순위 연산자 혹은 튜플로 쓰인다.
    + 설정값으로 튜플을 쓸 때는 헷갈리면 리스트를 쓰는 게 낫다. 튜플을 쓰면 성능 상의 약간의 이득은 있으나 차이 거의 없다. 코드 오류가 나지 않는 것이 중요하다.

```
>>> tuple1 = (1 + 3)        # 우선순위(갯수가 1개일 때, 콤마를 생각하면 NOT 튜플)
>>> tuple2 = (1 + 3,)       # 튜플
>>> tuple3 = (3)            # 우선순위
>>> tuple3 = (3,)           # 튜플

>>> tuple4 = 1, 2           # 튜플. 괄호 없이도 튜플로 인식한다.
```

+ packing/unpacking : list/tuple에서 동일하게 적용된다.

+ unpacking 시에 개수가 맞지 않으면 ValueError가 발생한다.

```
>>> numbers = (1,2,3,4,5,)          # packing - 다수 값을 하나의 변수에 넣는다.
>>> v1, v2, v3, v4, v5 = numbers    # unpacking - 하나의 값을 다수의 변수에 나눠 담는다.

>>> v1, v2, v3, v4 = numbers[:4]
>>> v1, v2, v3, *others = numbers   # 처음 3개를 제외한 나머지는 others라는 list에 넣겠다.
>>> *others, v3, v4, v5 = numbers
>>> v1, v2, *others, v5 = numbers

>>> v1, v2, v3, v4, v4, v5, v6, v7, v8 = (*numbers, 6, 7, 8)
```

+ **swap**: list/tuple에 동일하게 적용

```
>>> x, y = 1, 2                     # x에는 1 대입, y에는 2 대입
>>> x, y = y, x                     # x에는 y값을, y에는 x값을 동시에 대입
```

## set(집합형)

+ 중복을 허용하지 않는 데이터의 집합
    + list/tuple에서 중복을 제거하고자 할 때, set을 활용하면 유용

+ list/tuple과 다르게 추가된 순서를 유지하지 않는다.

```
>>> set_numbers = {1,3,4,5,4,1,3,3,4}
>>> set_numbers
{1,3,4,5}

>>> list_numbers = [1,1,2,2,3,2,2,1,1,1]
>>> list_numbers = list(set(list_numbers))
>>> list_numbers
[1, 2, 3]
```

+ 합집합, 교집합, 차집합, 여집합 연산 지원

```
>>> set_numbers1 - set_numbers2      # 차집합
>>> set_numbers1 | set_numbers2      # 합집합
>>> set_numbers1 & set_numbers2      # 교집합
>>> set_numbers1 ^ set_numbers2      # 여집합
```

## dict(사전형)

+ Key와 Value의 쌍으로 구성된 집합
+ Key 중복을 허용하지 않음
+ 중괄호 내에 콜론(:)으로 Key/Value를 구분

```
dict_values = {'blue': 10, 'yellow': 3, 'red': 42}
```

+ in 연산자로 멤버십 체크 지원 (Key의 등록 여부)

    > key의 여부를 확인하는 것이지, value의 여부를 확인하는 것이 아니다!  
    > value의 여부를 확인하려면 10 in dict_values.values()와 같이 멤버함수를 써야 한다.

+ 순회할 때도 Key 목록만 지원
+ 멤버함수
    + .keys() : key 목록
    + .values() : value 목록
    + .items() : (key, value) 목록

```
>>> dict_values = {'blue': 10, 'yellow': 3, 'red': 42}
>>> print(dict_values['blue'])
10

>>> dict_values['black'] = 30          # 새로운 Key:Value 등록
>>> del dict_values['blue']            # 지정 Key:Value 제거
```

+ for 루프 순회

```
>>> dict_values = {'blue': 10, 'yellow': 3, 'red': 42}
>>> for key in dict_values:
        print(key)
red
yellow
blue
>>> for (key, value) in dict_values.items():
        print(key, value)
red 42
yellow 3
blue 10
```

**끝.**

---

# 2강 데이터 타입

## 기본 데이터 타입

+ int, float, str = 정수, 실수, 문자

## 변수 (Variables)

+ 프로그램이 실행되면서 필요한 데이터를 임시로 저장하는 공간
    > 이러한 공간을 하드웨어에서는 '메모리'라고 한다.


+ 효율성을 높이기 위해 적절한 크기/용도의 변수에 값을 담아서 처리


+ 하나의 소프트웨어가 동작하면서, 로직에 따라 수많은 새로운 변수가 생겨나고 변경되며 제거

```
name = "Hello, Python." # 우항의 값을 좌항의 변수에 할당한다.
birth = 1990
age = 2017 - birth
print(name, age)

# 위 코드를 jupyter notebook에서 실행해 본다.
```

## 데이터 타입 (Data Types)

+ 변수는 하나의 데이터를 담아두는 공간. 그릇 개념.

+ **효율성** 을 위해, 그릇도 목적(크기/용도)에 따라 다양한 그릇이 필요.
    + 물을 담아두는 다양한 용기 : 물컵, 양동이, 물탱크, 소방차 등
+ 자원은 **유한** 하다.
    + 자원이 귀한 줄 알고, 아껴써야 한다. (CPU, **메모리**, 디스크 등)

## Numeric Type (숫자)

+ 정수형 : int
+ 실수형 : float
+ 사칙연산 (`+`, `-`, `*`, `/`), 몫(`//`), 나머지(`%`), 지수 (`**`)

```
# 실행된 jupyter notebook에서 사칙연산을 해본다.
# 여유가 된다면 마크다운 모드로 작성해본다.
# ex. ## 사칙연산
```

## Boolean Type (참/거짓)

+ 참, 거짓 = True, False (Java에서는 true/false)
+ 비교 연산자의 결과는 Boolean Type이다.
    + 값 비교: <, <=, >, >=, ==, !=
    + 참조 비교: is, is not
        > 참조하는 변수가 같은지를 따지는 것  
        > (심화: 자료구조) 메모리의 주소가 같으냐(ex. 0x1000)를 따지는 것

```
>>> a = []
>>> b = []
>>> id(a), id(b)
(3023598353864, 3023598350472)
>>> a = b
True            # 값을 비교하는데 둘 다 빈 리스트이므로 True
>>> a is b
False           # 참조를 비교하는데 서로 다른 변수이므로 False
```

+ 논리 연산자
    + or, and, not

```
>>> True and False
False
>>> True or False
True
>>> not True
False
```

## 다른 타입에서의 Boolean 판단

+ 숫자 0은 False, 그 이외에는 True
+ 빈 문자열은 False, 그 이외에는 True
+ 빈 list/tuple/set/dict는 False, 그 이외에는 True

```
>>> bool(0), bool(1), bool(-1)
(False, True, True)
>>> bool(''), bool(' '), bool('a')    # ' ': 눈에 보이지 않지만 whitesapce 1칸 존재
(False, True, True)
>>> bool([]), bool(()), bool({}), bool(set()), bool([' '])
(False, False, False, False, True)
```

## String Type (문자열)

+ 문자열을 홑따옴표(')로 감싸거나 쌍따옴표(")로 감싸기

```
name1 = 'Python'
name2 = "Python"

name1 == name2

# 따옴표의 종류는 상관없다. 두 개는 같은 문자열이다.
```

+ 따옴표 1개로 감싼 문자열 안에 따옴표를 문자열 처리하고자 할 경우, 해당 따옴표를 ESCAPE 처리

```
name = 'I\'m tom'
```

+ 파이썬은 여러 줄 문자열 문법을 지원한다. 따옴표 3개로 감싸주는 문법.

```
lyrics = '''노래 한번 할게요
굉장히 좋은 노래
후렴이 듣기 좋아서
마음 아려지는 그런 노래
라라라라라
한 여자가 주인공인 노래
이제는 듣는 사람이 없는 노래
'''

# 개행 (\n)이 자동으로 처리된다.
```

## 문자열 format 지정자

+ 문자열 내에 "{}"와 같은 형태로 슬롯을 만들고, format 함수를 통해 슬롯에 필요한 데이터를 넘긴다.

+ format 함수에 **함수인자** 로서 슬롯을 지정하는 방법
    + 위치 (Positional), 키워드 (Keyword)

```
# 위치 인자

>>> '{0}, {1}, {2}'.format('a', 'b', 'c')
a, b, c
>>> '{}, {}, {}'.format('a', 'b', 'c')
a, b, c
>>> '{2}, {1}, {0}'.format('a', 'b', 'c')
c, b, a
>>> '{2}, {1}, {0}'.format(*'abc')    # sequence-unpacking (tuple)
c, b, a
>>> '{0}, {1}, {0}'.format('a', 'b')
a, b, a

# 출력시 감싸주는 따옴표를 없애려면 print문으로 출력해본다.
```

```
# 키워드 인자

>>> 'Coordinates: {lat}, {lng}'.format(lat='37.24N', lng='-115.81W')
>>>
>>> coord = {'lat': '37.24N', 'lng': '-115.81W'}
>>> 'Coordinates: {lat}, {lng}'.format(**coord)    # sequence-unpacking (dictionary)
```

## NameError

+ 정의되지 않은 변수에 접근하면 발생

```
>>> print(a)
NameError: name 'a' is not defined
```

**끝.**

---

# 1강 시작하기

## 시작하기에 앞서

+ Python3 설치
    + Anaconda Python 추천


+ 소스코드 편집기 설치
    + Visual Studio Code, Atom, Sublime Text 3


+ Ipython Notebook 설치
    + Anaconda Python에는 이미 설치되어 있다.
    + 기본 파이썬을 쓴다면 터미널에서 다음 명령어 실행한다.
        + `pip install "ipython[notebook]"`

## 파이썬의 선 (The Zen of Python)

+ 명시가 암시보다 좋다. (분명하게 표현해라)
+ 가독성은 중요하다. (네이밍, 들여쓰기, 주석, 라인브레이크)

+ `import this`

## 파이썬에서 코드 실행하는 3가지 방법

+ Interactive Shell에서 한땀 한땀 실행하기

```
$ python
>>> print(sum(range(101)))
>>> exit()

# 기본 python shell
```

```
$ ipython
>>> print(sum(range(101)))

# 기본 파이썬보다 기능이 훨씬 더 많은 ipython shell
# 명령어에 따른 컬러링 기능으로 훨씬 보기 편함
```

```
$ jupyter notebook

노트북 파일 생성 : `New` - `Python[default]`
노트북 이름 변경 : `Untitled` - `원하는 이름`

>>> sum(range(101))

코드 실행 : ctrl + enter

# jupyter notebook
# 단, 반드시 작업할 디렉토리에서 명령어를 실행해야 관리하기 편하다.
```

+ 파이썬 인터프리터 실행할 때 코드 넣기

```
$ python -c "print(sum(range(101)))"
```

+ 소스파일로부터 한 번에 실행하기

```
$ python filename.py

# 실제 개발시 가장 많이 사용하는 방법
# 소스코드 편집기를 통해 소스파일을 작성한다.
```
