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

n, req_sum = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

def func():
  start, end = 0, n - 1
  prev_mid, prev_sum = 0, 0

  while True:
    curr_mid = (start + end) // 2
    curr_sum = 0

    for val in data[curr_mid + 1:]: curr_sum += val - data[curr_mid]

    if curr_sum == req_sum:
      return data[curr_mid]
    
    if prev_sum < curr_sum and prev_sum < req_sum < curr_sum: 
      left, right = data[curr_mid] + 1, data[prev_mid]
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

    if curr_sum > req_sum:
      prev_mid, prev_sum = curr_mid, curr_sum
      start = curr_mid + 1
    elif curr_mid == 0: return data[0] - 1
    else:
      prev_mid, prev_sum = curr_mid, curr_sum
      end = curr_mid - 1

print(func())