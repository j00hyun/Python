def profile(name, age, lang1, lang2, lang3, lang4, lang5):
  print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # 프린트가 끝날 때 줄바꿈을 하지 않고 " "만 추가됨
  print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")

def profile1(name, age, *language):
  print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # 프린트가 끝날 때 줄바꿈을 하지 않고 " "만 추가됨
  for lang in language:
    print(lang, end= " ")
  print()

profile1("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile1("김태호", 25, "Kotlin", "Swift")