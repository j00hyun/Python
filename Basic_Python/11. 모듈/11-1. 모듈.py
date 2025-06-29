# theater_module 불러오기
import theater_module
theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때

import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning # 필요한 함수만 가져옴
price(5)
price_morning(6)
# price_soldier(7) # 에러

from theater_module import price_soldier as price
price(5) # price_soldier 호출됨