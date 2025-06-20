# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = [1,2,3,4,5]
print(students) # [1, 2, 3, 4, 5]

students = [i+100 for i in students]
print(students) # [101, 102, 103, 104, 105]

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I an groot"]
students = [len(i) for i in students]
print(students) # [8, 4, 10]

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I an groot"]
students = [i.upper() for i in students]
print(students) # ['IRON MAN', 'THOR', 'I AN GROOT']