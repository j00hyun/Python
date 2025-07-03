####################### 종료 조건이 있는 재귀 함수 ############################

def recursive_function(i):
  # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
  if i == 100: return
  print(i, '번째 재귀함수에서', i + 1, '번째 재귀함수를 호출합니다.')
  recursive_function(i + 1)
  print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)

############################## 팩토리얼 구현 ###############################

# 반복적으로 구현한 n!
def factorial_iterative(n):
  result = 1
  # 1부터 n까지의 수를 차례대로 곱하기
  for i in range(1, n + 1): result *= i
  return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
  if n <= 1: return 1 # 0! = n! = 1
  # n! = n * (n - 1)!를 그대로 코드로 작성하기
  return n * factorial_recursive(n - 1)
  
######################## 최대공약수 계산 (유클리드 호제법) ######################

# 유클리드 호제법
#   두 자연수 A, B에 대하여 (A > B) A를 B로 나눈 나머지를 R이라고 합시다.
#   이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같습니다.

#   예시: GCD(192, 162)
#        GCD(162, 30)
#        GCD(30,  12) 
#        GCD(12,  6)   = 6

def gcd(a, b):
  if a % b == 0: return b
  else: return gcd(b, a % b)

print(gcd(192, 162))