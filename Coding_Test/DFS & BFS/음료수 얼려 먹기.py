##### 문제
#   N x M 크기의 얼음 틀이 있습니다.
#   구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시됩니다.
#   구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주합니다.
#   이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림 개수를 구하는 프로그램을 작성하세요.
#   다음의 4 x 5 얼음 틀 예시에서는 아이스크림이 총 3개 생성됩니다.
#     00110
#     00011
#     11111
#     00000

#   입력 조건: 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어집니다. (1 <= N, M <= 1,000)
#            두 번째 줄부터 N + 1번째 줄까지 얼음 틀의 형태가 주어집니다.
#            이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1입니다.
#   출력 조건: 한 번에 만들 수 있는 아이스크림의 개수를 출력합니다.
#   입력 예시: 4 5
#            00110
#            00011
#            11111
#            00000
#   출력 예시: 3

##### 내 풀이
# BFS
from collections import deque

row, col = map(int, input().split()) # 얼음 틀의 세로 길이와 가로 길이
data = [[True] * col for _ in range(row)] # 얼음 틀 내부 0, 1 데이터 
answer = 0 # 한 번에 만들 수 있는 아이스크림 개수
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 얼음틀에서 뚫린 부분은 Fasle, 막혀있는 부분은 True로 세팅
for row_idx in range(row):
  for col_idx, col_data in enumerate(input()):
    if col_data == '0': data[row_idx][col_idx] = False

queue = deque()

for r in range(row):
  for c in range(col):
    # 얼음 칸을 탐색하며 뚫려 있는 부분을 큐에 집어 넣음
    if data[r][c] is False:
      queue.append((r, c))
      data[r][c] = True
      answer += 1

      while(queue):
        v = queue.popleft()
        # 현재 위치에서 상하좌우 부분이 뚫려있는 부분인지 확인
        for dr, dc in moves:
          cr,cc = v[0] + dr, v[1] + dc
          if 0 <= cr < row and 0 <= cc < col and data[cr][cc] is False:
            queue.append((cr, cc))
            data[cr][cc] = True

print(answer)

##### 모범 답안
# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
  # 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  # 현재 노드를 아직 방문하지 않았다먼
  if graph[x][y] == 0:
    # 해당 노드 방문 처리
    graph[x][y] = 1
    # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    # 현재 위치에서 DFS 수행
    if dfs(i, j) == True:
      result += 1

print(result) # 정답 출력 