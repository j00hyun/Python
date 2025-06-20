# 일반 유닛
class Unit:
  def __init__(self, name, hp, speed):
    self.name = name
    self.hp = hp
    self.speed = speed

  def move(self, location):
    print("[지상 유닛 이동]")
    print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# 건물
class BuildingUnit(Unit):
  def __init__(self, name, hp, location):
    pass # 코드를 완성하지 않아도 완성된 것 처럼 넘어감

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# -----------------------------------

def game_start():
  print("[알림] 새로운 게임을 시작합니다.")

def game_over():
  pass

game_start()
game_over()