import sys

# Python,Java?무엇이 더 재밌을까요?
print("Python", "Java", sep=",", end="?")
print("무엇이 더 재밌을까요?")

print("Python", "Java", file=sys.stdout) # 표준 출력
print("Python", "Java", file=sys.stderr) # 로깅시 표준 에러로 출력

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}

for subject, score in scores.items():
  # ljust(8): 8칸의 공간 확보 후 왼쪽으로 정렬
  # rjust(4): 4칸의 공간 확보 후 오른쪽으로 정렬
  print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
  print("대기번호 : " + str(num).zfill(3)) # 3칸의 공간 확보 후 값이 없는 공간은 0으로 채움

# 표준 입력
# 사용자 입력으로 값을 받으면 항상 string 값으로 저장됨
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")