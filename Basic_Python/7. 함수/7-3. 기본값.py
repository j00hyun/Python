def profile(name, age, main_lang):
  print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업
def profile1(name, age=17, main_lang="파이썬"):
  print("이름: {0}\t나이: {1}\t주 사용 언어: {2}".format(name, age, main_lang))

profile1("유재석")
profile1("김태호")