# 일반 유닛
class Unit:
  def __init__(self):
    print("Unit 생성자")

class Flyable:
  def __init__(self):
    print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
  def __init__(self):
    super().__init__()

# 다중 상속의 경우 사용하면 안됨
# Unit 생성자만 호출됨 (맨 처음 상속받는 클래스에 대해서만 init 함수 호출)
dropship = FlyableUnit() 

# 건물
class BuildingUnit(Unit):
  def __init__(self, name, hp, location):
    super().__init__(name, hp, 0) # Unit.__init__(self, name, hp, 0) 과 동일
    self.location = location