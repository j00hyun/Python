##### Breath-First Search

#       (1)——(2)
#      /   \    \
#    (3)   (8)——(7)
#    / \         |
#  (4)-(5)      (6)

# 방문 기준 : 번호가 낮은 인접한 노드부터
# 탐색 순서 : 1 -> 2 -> 3 -> 8 -> 7 -> 4 -> 5 -> 6

# 탐색 과정 (큐: 왼쪽 출구, 오른쪽 입구)
#   1                  1 입력 및 방문처리
#   2 3 8       1 출력, 2 3 8 입력 및 방문처리
#   3 8 7       2 출력, 7 입력 및 방문처리
#   8 7 4 5     3 출력, 4 5 입력 및 방문처리
#   7 4 5       8 출력
#   4 5 6       7 출력, 6 입력 및 방문처리
#   5 6         4 출력
#   6           5 출력
#               6 출력

from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
  # 큐(Queue) 구현을 위해 deque 라이브러리 사용
  queue = deque([start])
  # 현재 노드를 방문 처리
  visited[start] = True
  # 큐가 빌 때까지 반복
  while queue:
    # 큐에서 하나의 원소를 뽑아 출력하기
    v = queue.popleft()
    print(v, end=' ')
    # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7], 
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8], 
  [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)
