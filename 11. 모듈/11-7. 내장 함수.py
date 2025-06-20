# input : 사용자 입력을 받는 함수
language = input("무슨 언어를 좋아하세요?")
print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'language']
import random # 외장 함수
print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'language', 'random']
import pickle
print(dir()) # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'language', 'pickle', 'random']

print(dir(random)) # 랜덤 모듈에서 쓸 수 있는 변수, 함수들 표시

lst = [1, 2, 3]
print(dir(lst)) # 리스트에서 쓸 수 있는 것들 표시

name = "Jim"
print(dir(name)) # name 변수에서 쓸 수 있는 것들 표시