# travel 패키지 안에 thailand 모듈 불러오기
import travel.thailand 
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# travel 패키지 안 thailand 모듈에서 ThailandPackage 함수만 불러오기
from travel.thailand import ThailandPackage 
trip_to = ThailandPackage()
trip_to.detail()

# travel 패키지 안 vietname 모듈 불러오기
from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# travel 패키지 안 모든 모듈 불러오기
from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()
trip_to2 = thailand.ThailandPackage()
trip_to2.detail()