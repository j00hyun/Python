##### 문제
#   오늘 동빈이는 부모님을 대신해서 떡집 일을 하기로 했습니다. 오늘은 떡볶이 떡을 만드는 날입니다.
#   동빈이네 떡볶이 떡은 재밌게도 떡볶이 떡의 길이가 일정하지 않습니다.
#   대신에 한봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춰줍니다.
#   절단기에 높이(H)을 지정하면 줄지어진 떡을 한 번에 절단합니다.
#   높이가 H보다 긴 떡은 H 위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않습니다.
#   예를 들어 높이가 19, 14, 10, 17cm인 떡이 나란히 있고 절단기 높이를 15cm로 지정하면 자른 뒤의 떡 높이는 15, 14, 10, 15cm가 될 것입니다.
#   잘린 떡의 길이는 차례대로 4, 0, 0, 2cm입니다. 손님은 6cm만큼의 길이를 가져갑니다.
#   손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하세요.

#   입력 조건: 첫째 줄에 떡의 개수 N과 요청한 떡의 길이 M이 주어집니다. (1 <= N <= 1,000,000, 1 <= M <= 2,000,000,000)
#            둘째 줄에는 떡의 개별 높이가 주어집니다. 떡 높이의 총합은 항상 M 이상이므로, 손님은 필요한 양만큼 떡을 사갈 수 있습니다.
#            높이는 10억보다 작거나 같은 양의 정수 또는 0입니다.
#   출력 조건: 적어도 M만큼의 떡을 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값을 출력합니다.
#   입력 예시: 4 6
#            19 15 10 17
#   출력 예시: 15

##### 내 풀이
n, req_sum = map(int, input().split()) # 떡의 개수, 요청한 떡의 길이
data = list(map(int, input().split())) # 떡의 개별 높이

data.sort() # 떡의 높이를 오름차순으로 정렬

def func():
  start, end = 0, n - 1 # 이진 탐색 시작 인덱스와 끝 인덱스
  prev_mid, prev_sum = 0, 0 # 이전 이진 탐색 데이터 (중간 인덱스, 떡 길이)

  # 반복하여 이진 탐색 수행
  while True:
    curr_mid = (start + end) // 2 # 중간 인덱스
    curr_sum = 0

    # 중간 인덱스의 떡 높이를 기준으로 자른 오른쪽 떡들의 길이 합 계산
    for val in data[curr_mid + 1:]: curr_sum += val - data[curr_mid]

    # 오른쪽 떡들의 길이 합이 요청한 떡의 길이와 같다면 수행 종료
    if curr_sum == req_sum:
      return data[curr_mid]
    
    # 요청한 떡의 길이가 이전 탐색의 합과 현재 탐색의 합의 사잇값인 경우
    if prev_sum < curr_sum and prev_sum < req_sum < curr_sum: 
      left, right = data[curr_mid] + 1, data[prev_mid]
      # H 값을 보정하며 요청한 떡의 길이와 합이 같아질 때 수행 종료
      for h in range(left, right):
        curr_sum -= len(data[curr_mid + 1:])
        if curr_sum == req_sum:
          return h

    elif prev_sum > curr_sum and curr_sum < req_sum < prev_sum: 
      left, right = data[prev_mid] + 1, data[curr_mid]
      for h in range(left, right):
        curr_sum -= len(data[curr_mid + 1:])
        if curr_sum == req_sum:
          return h

    # 위의 조건에 맞지 않고, 현재 길이가 요청 길이보다 크다면 오른쪽 떡 값들을 높이로 탐색
    if curr_sum > req_sum:
      prev_mid, prev_sum = curr_mid, curr_sum
      start = curr_mid + 1
    # 현재 길이가 요청 길이보다 작고 더이상 왼쪽 떡값들이 없다면 가장 작은 떡의 길이보다 1 작은 값 반환
    elif curr_mid == 0: return data[0] - 1
    # 현재 길이가 요청 길이보다 작다면 왼쪽 떡 값들을 높이로 탐색
    else:
      prev_mid, prev_sum = curr_mid, curr_sum
      end = curr_mid - 1

print(func())

##### 모범 답안
# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력
n, m = list(map(int, input().split(' ')))
# 각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while(start <= end):
  total = 0
  mid = (start + end) // 2
  for x in array:
    # 잘랐을 때 떡의 양 계산
    if x > mid:
      total += x - mid
  # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
  if total < m:
    end = mid - 1
  # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
  else:
    result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
    start = mid + 1

# 정답 출력
print(result)