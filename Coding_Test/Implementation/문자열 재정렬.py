##### 문제
#   알파벳 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다.
#   이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

#   예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다. 

#   입력 조건: 첫째 줄에 하나의 문자열 S가 주어집니다. (1 <= S의 길이 <= 10,000)
#   출력 조건: 첫째 줄에 문제에서 요구하는 정답을 출력합니다.
#   입력 예시 1: K1KA5CB7
#   출력 예시 1: ABCKK13
#   입력 예시 2: AJKDLSI412K4JSJ9D
#   출력 예시 2: ADDIJJJKKLSS20

##### 내 풀이
string = input()
numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'} # 숫자 요소 리스트
sum = 0
answer = []

# 입력 문자열을 하나씩 탐색하며 숫자 요소일 경우에는 합을 구하고 문자 요소일 경우에는 리스트에 추가
for c in string:
  if c in numbers: sum += int(c)
  else: answer.append(c)

answer.sort() # 문자 요소들만 있는 리스트를 오름차순 정렬
answer = ''.join(answer) # 리스트를 문자열로 변환
answer += str(sum) # 문자열 뒤에 숫자 요소의 총합을 붙여넣기

print(answer)

##### 모범 답안
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
      result.append(x)
    # 숫자는 따로 더하기
    else:
      value += int(x)
  
# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
  result.append(str(value))

# 최종 결과 출력 (리스트를 문자열로 변환하여 출력)
print(''.join(result))