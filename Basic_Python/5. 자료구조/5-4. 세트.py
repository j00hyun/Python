# 집합 (set)

# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3}

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}

# 합집합 (java 도 할 수 있거나 python 도 할 수 있는 개발자)
print(java | python) # {'박명수', '김태호', '유재석', '양세형'}
print(java.union(python)) # {'박명수', '김태호', '유재석', '양세형'}

# 차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python) # {'양세형', '김태호'}
print(java.difference(python)) # {'양세형', '김태호'}

# python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python) # {'김태호', '박명수', '유재석'}

# java를 잊었어요
java.remove("김태호")
print(java) # {'유재석', '양세형'}
