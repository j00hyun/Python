######################### Big O Notation ########################

# Better O(1) - O(logN) - O(N) - O(NlogN) - O(N^2) - O(N^3) - O(2^N) Worse

# 수행 시간 측정 소스코드
import time
start_time = time.time() # 측정 시작
# 프로그램 소스 코드
end_time = time.time() # 측정 종료
print("time", end_time - start_time) # 수행 시간 출력 

########################### 수 자료형 ##########################

# 실수형
a = 5. # 5.0
a = -.7 # -0.7

# 지수 표현 방식 -> 실수형 데이터로 저장됨
a = 1e9 # 1,000,000,000.0
a = 75.25e1 # 752.5
a = 3954e-3 # 3.954

# int 함수를 사용해 정수형으로 변환 가능
a = int(1e9) # 1,000,000,000

# round 함수를 이용해 실수 값의 오차를 줄임
round(123.456, 2) # 123.46
round(0.3 + 0.6, 4) # 0.8999999999 -> 0.9

# 나누기 연산자(/) : 실수형으로 반환
a = 7 / 3 # 2.333333333335

# 나머지 연산자(%) : 홀수인지 짝수인지 체크 가능
a = 7 % 3 # 1

# 몫 연산자(//)
a = 7 // 3 # 2

# 거듭 제곱 연산자(**)
a = 5 ** 3 # 125
a = 5 ** 0.5 # 2.23606797749979 (제곱근)

###################### 리스트 자료형 ########################

# 크기가 N이고, 모든 값이 0인 1차원 리스트 초기화
a = [0] * 10 # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 슬라이싱 : 끝 인덱스는 실제 인덱스보다 1을 더 크게 설정
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[1 : 4] # [2, 3, 4]

# 리스트 컴프리헨션 : 리스트 초기화 방법
array = [i for i in range(10)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
array = [i for i in range(10) if i % 2 == 1] # [1, 3, 5, 7, 9]
array = [i * i for i in range(1, 5)] # [1, 4, 9, 16]
# 2 X 3 크기의 2차원 리스트 초기화
array = [[0] * 3 for _ in range(2)] # [[0, 0, 0], [0, 0, 0]]

a = [1, 4, 3]

# 리스트에 원소 삽입
a.append(2) # [1, 4, 3, 2]

# 오름차순 정렬
a.sort() # [1, 2, 3, 4]

# 내림차순 정렬
a.sort(reverse = True) # [4, 3, 2, 1]

# 리스트 원소 뒤집기
a.reverse() # [1, 2, 3, 4]

# 특정 인덱스에 데이터 추가
a.insert(2, 3) # 인덱스 2에 3 추가: [1, 2, 3, 3, 4]

# 특정 값인 데이터 개수 세기
a.count(3) # 2

# 특정 값 데이터 삭제 (해당 값을 가진 원소가 여러 개면 하나만 제거)
a.remove(1) # [2, 3, 3, 4]

# 리스트에서 특정 값을 가지는 원소를 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set] # [1, 2, 4]

# 리스트를 문자열로 변환하기
lst = ['a', 'b', 'c'] # 리스트가 문자열 요소일 경우
result = ''.join(lst)

lst = [1, 2, 3, 4] # 리스트가 숫자 요소일 경우
result = ''.join(str(x) for x in lst)

###################### 문자열 자료형 ########################

# 문자열은 특정 인덱스의 값을 변경할 수 없음 (Immutable)

data = "Don't you know \"Python\"?" # Don't you know "Python"?

# 덧셈(+)을 이용해 문자열을 연결(Concatenate)
a = "Hello" + " " + "World" # Hello World

# 문자열을 특정한 양의 정수와 곱하는 경우, 문자열이 그 값만큼 여러번 더해짐
a = "String" * 3 # StringStringString

# 슬라이싱 이용 가능
a = "ABCDEF"
a[2 : 4] # CD

###################### 튜플 자료형 ########################

# 리스트와 차이점
#   1. 튜플은 한 번 선언된 값을 변경할 수 없음
#   2. 튜플은 리스트에 비해 상대적으로 공간 효율적 (더 적은 양의 메모리 사용)

a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

a[1 : 4] # (2, 3, 4)

# 튜플을 사용하면 좋은 경우
#   1. 서로 다른 성질의 데이터를 묶어서 관리할 때 (ex. 최단 경로 알고리즘에서 (비용, 노드 번호)의 형태로 튜플 사용)
#   2. 데이터의 나열을 해싱의 키 값으로 사용할 때 (튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용 가능)
#   3. 리스트보다 메모리를 효율적으로 사용해야 할 때

###################### 사전 자료형 ########################

# 변경 불가능한(Immutable) 자료형을 키로 사용
# 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'

print(data) # {'사과': 'Apple', '바나나': 'Banana'}

# 키 데이터만 담은 리스트
key_list = data.keys() # dict_keys(['사과', '바나나'])

# 값 데이터만 담은 리스트
value_list = data.values() # dict_values(['Apple', 'Banana']) 

###################### 집합 자료형 ########################

# 중복을 허용하지 않고, 순서가 없음
# 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리

# 집합 자료형 초기화
data = set([1, 1, 2, 3, 4, 4, 5]) # {1, 2, 3, 4, 5}
data = {1, 1, 2, 3, 4, 4, 5} # {1, 2, 3, 4, 5}

# 합집합
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])
a | b # {1, 2, 3, 4, 5, 6, 7}

# 교집합
a & b # {3, 4, 5}

# 차집합
a - b # {1, 2}

# 새로운 원소 추가
data = set([1, 2, 3])
data.add(4) # {1, 2, 3, 4}

# 새로운 원소 여러 개 추가
data.update([5, 6]) # {1, 2, 3, 4, 5, 6}

# 특정한 값을 갖는 원소 삭제
data.remove(3) # {1, 2, 4, 5, 6}

# 사전 자료형과 집합 자료형의 특징
#   1. 리스트나 튜플은 순서가 있기 때문에 인덱싱을 통해 자료형의 값을 얻을 수 있음
#   2. 사전과 집합은 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없고 키(Key)와 원소(Element)를 이용해 O(1)의 시간 복잡도로 조회

###################### 기본 입출력 ########################

# input() : 한 줄의 문자열을 입력 받는 함수
# map() : 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용

# 공백을 기준으로 구분된 숫자 데이터를 입력 받을 때 (65 90 75 34 99)
data = list(map(int, input().split())) # [65, 90, 75, 34, 99]

# 공백을 기준으로 구분된 숫자 데이터의 수가 정해져 있고 많지 않을 때
a, b, c = map(int, input().split())

# 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우에는 sys 라이브러리 사용
# 단, 입력 후 엔터가 줄 바꿈 기호로 입력되므로 rstrip() 메서드 함께 사용
import sys
sys.stdin.readline().rstrip()

# 각 변수를 콤마(,)를 이용해 띄어쓰기로 구분하여 출력
print(1, 2) # 1 2

# 줄 바꿈을 원치 않는 경우 'end' 속성 이용
print(7, end=" ")
print(8, end=" ")
print("정답은 " + str(7) + "입니다.") # 7 8 정답은 7입니다.

# f-string: 문자열과 정수를 함께 넣을 수 있음
print(f"정답은 {answer}입니다.") # 정답은 7입니다.

######################### 조건문 ##########################

# if elif else 문
if a >= 0:
  print("a >= 0")
elif a >= -10:
  print("-10 <= a < 0")
else:
  print("a < -10")

# 논리 연산자
if True or False: # or
  print("Yes")

if True and True: # and
  print("Yes")

if not False: # not
  print("Yes")

# pass: 디버깅 과정에서 일단 조건문의 형태만 만들어 놓고 조건문을 처리하는 부분은 비워놓고 싶은 경우
if score >= 80:
  pass # 나중에 작성할 소스코드
else: 
  print("성적이 80점 미만입니다.")

# 조건문에서 소스코드가 한 줄인 경우, 줄바꿈하지 않아도 됨
if score >= 80: result = "Success"
else: result = "Fail"

# 조건문 표현식(Conditional Expression) : if else문을 한줄에 작성
result = "Success" if score >= 80 else "Fail"

# 수학의 부등식 그대로 사용 가능
if 0 < x < 20:
  print("x는 0 이상 20 미만의 수입니다.")

######################### 반복문 ##########################

# while 문
i = 1
while i <= 9:
  i += 1

# for 문
array = [9, 8, 7, 6, 5]
for x in array:
  print(x)

# range(시작값, 끝값 + 1)
for i in range(1, 10):
  print(i)

# continue : 남은 코드의 실행을 건너뛰고, 다음 반복을 진행
for i in range(1, 10):
  if i % 2 == 0:
    continue
  result += 1 # 1부터 9까지의 홀수의 합

# break : 반복문을 즉시 탈출
while True:
  i += 1
  if i == 5:
    break

##################### 함수와 람다 표현식 ######################

# 함수
def add(a, b):
  return a + b

# 파라미터의 변수를 직접 지정 가능
add(b = 3, a = 7)

# global 키워드 : 해당 함수에서 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조
a = 0

def func():
  global a
  a += 1

func()
print(a) # 1

# 전역 변수 값을 출력하는 등 단순히 참조 할 때는 global 키워드 필요 없음
a = 10

def func():
  print(a)

func() # 10

# 전역 변수로 선언된 리스트 객체의 내부 메서드를 호출 할 때에도 global 키워드 필요 없음 
array = [1, 2, 3, 4, 5]

def func():
  array.append(6)
  print(array)

func() # [1, 2, 3, 4, 5, 6]

# 함수 안에 전역 변수와 동일한 이름을 가진 지역 변수가 선언된다면 지역 변수가 우선적으로 참조됨 
array = [1, 2, 3, 4, 5]

def func():
  array = [3, 4, 5]
  array.append(6)
  print(array)

func() # [3, 4, 5, 6]
print(array) # [1, 2, 3, 4, 5]

# 전역 변수를 사용하기 위해서 global 키워드 사용
array = [1, 2, 3, 4, 5]

def func():
  global array
  array = [3, 4, 5]
  array.append(6)
  print(array)

func() # [3, 4, 5, 6]
print(array) # [3, 4, 5, 6]

# 여러 개의 반환 값
def operator(a, b):
  return a + b, a - b, a * b

a, b, c = operator(7, 3)

# 람다 표현식 : 한 줄에 함수를 작성 가능 
def add(a, b):
  return a + b

add(3, 7) # 10
(lambda a, b: a + b)(3, 7) # 위와 동일한 람다 표현식

# 학생을 점수 순으로 오름차순 정리
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
  return x[1]

sorted(array, key=my_key) # [('이순신', 32), ('홍길동', 50), ('아무개', 74)]
sorted(array, key=lambda x: x[1]) # 위와 동일한 람다 표현식

# 2개의 리스트에 같은 인덱스를 가진 값들을 더하기
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)

list(result) # [7, 9, 11, 13, 15]

##################### 유용한 표준 라이브러리 ######################
##### 내장 함수: 기본적인 함수들 제공

# sum() : 리스트와 튜플의 원소들의 합 반환
result = sum([1, 2, 3, 4, 5]) # 15

# min(), max() : 가장 작은 값, 큰 값 반환
min_result = min(7, 3, 5, 2) # 2
max_result = max(7, 3, 5, 2) # 7

# eval() : 수식으로 표현된 식의 계산 값을 반환
result = eval("(3+5)*7") # 56

# sorted() : 반복 가능한 객체의 정렬 결과 반환
result = sorted([9, 1, 8, 5, 4]) # [1, 4, 5, 8, 9]
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True) # [9, 8, 5, 4, 1]

# sorted() with key : 키 속성으로 정렬 기준 명시 가능
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
result = sorted(array, key=lambda x: x[1], reverse=True) # [('아무개', 74), ('홍길동', 50), ('이순신', 32)]

# ord() : 아스키 코드
ord('a')

# 문자가 알파벳인지 확인
'a'.isalpha() # True

##### itertools : 반복되는 형태의 데이터를 처리 기능 제공 (순열과 조합 라이브러리 중요) 

# 순열 : {'A','B','C'}에서 3개를 선택하여 나열하는 경우
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3)) # [('A','B','C'), ('A','C','B'), ('B','A','C'), ('B','C','A'), ('C','A','B'), ('C','B','A')]

# 조합 : {'A','B','C'}에서 순서를 고려하지 않고 2개를 뽑는 경우
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2)) # [('A','B'), ('A','C'), ('B','C')]

# 중복 순열 : 2개를 뽑는 모든 순열 구하기 (중복 허용)
from itertools import product
data = ['A', 'B', 'C']
result = list(product(data, repeat=2))

# 중복 조합 : 2개를 뽑는 모든 조합 구하기 (중복 허용)
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))

##### collections: 덱(deque), 카운터(Counter) 등 자료구조 포함

# Counter: 반복 가능한 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지 알려줌
from collections import Counter
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

counter['blue'] # 3
counter['green'] # 1
dict(counter) # {'red': 2, 'blue': 3, 'green': 1}

##### math: 필수적인 수학 기능 제공 (팩토리얼, 제곱근, 최대공약수, 삼각함수, 파이 상수)

# gcd() : 최대 공약수
import math
math.gcd(21, 14) # 7

# 최소 공배수
def lcm(a, b):
  return a * b // math.gcd(a, b)

lcm(21, 14) # 42

##### heapq: 힙(Heap) 자료구조 제공 (우선순위 큐 기능 구현 시 사용)
##### bisect: 이진 탐색(Binary Search) 기능 제공 