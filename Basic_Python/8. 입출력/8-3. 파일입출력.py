# 덮어쓰기 목적으로 파일 열기
score_file = open("score.txt", "w", encoding="utf8") 
print("수학: 0", file=score_file) # 자동 줄바꿈
print("영어: 50", file=score_file)
score_file.close()

# 뒤에서 이어쓰기 목적으로 파일 열기
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학: 80") # 줄바꿈 없음
score_file.write("\n코딩: 100")
score_file.close()

# 파일 모든 내용 읽어옴
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

# 파일 줄별로 읽기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print()
score_file.close()

# 파일이 몇줄인지 모르는 상태에서 읽기
score_file = open("score.txt", "r", encoding="utf8")

while True:
  line = score_file.readline()
  if not line:
    break
  print(line, end="")

print()
score_file.close()

# 리스트에 값을 넣어 처리
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장

for line in lines:
  print(line, end="")

score_file.close()
