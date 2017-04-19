© 2017 SHAKEADE

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
+ 사칙연산 (+ - * /), 몫(//), 나머지(%), 지수 (\**), 연산자

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
이 노랠 부르면
네가 내 옆으로 와주니까
어깨에 기대어
목소리 좋다고 말해주니까
또 난 좋아서 이 노래 번호를 눌러
노래를 불러 너를 불러
여기까지만 할래요
나 혼자 하는 노랜
아무리 불러도 계속 불러도
넌 들을 수가 없잖아
이 노랠 부르면
네가 내 옆으로 와주니까
어깨에 기대어
목소리 좋다고 말해주니까
또 난 좋아서 이 노래 번호를 눌러
노래를 불러 너를 불러
노래가 끝나고
이 노래가 불러준
너도 떠나고 나면
모든 게 돌아와 제자리로
난 어떡해야 할지를 몰라
이 노랠 들으면
너도 내 생각이 나긴 할까
많이 좋아하던 목소리
잊어버린 건 아닐까
또 난 오늘도 이 노래 번호를 눌러
노래를 불러 너를 불러'''

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

+ 정의되지 않은 변수에 접근 시에 발생

```
>>> print(a)
NameError: name 'a' is not defined
```

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
