gun = 10

def checkpoint(soldiers): # 경계근무
  global gun # 전역 공간에 있는 gun 사용 (global 안쓰면 에러 발생)
  gun = gun - soldiers
  print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))

# 전역변수를 많이 사용하면 코드가 복잡해질 수 있어 아래 방법 추천

def checkpoint_return(gun, soldiers): # 경계근무
  gun = gun - soldiers # gun은 파라미터로 입력되어 지역변수가 됨
  print("[함수 내] 남은 총 : {0}".format(gun))
  return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_return(gun, 2) # 2명이 경계 근무 나감
print("남은 총 : {0}".format(gun))