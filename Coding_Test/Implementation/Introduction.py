##### 2차원 공간 행렬(Matrix)
for i in range(5):
  for j in range(5):
    print('(', i, ',', j, ')', end=' ')
  print()

##### 방향 벡터 (시뮬레이션 및 완전 탐색 문제)
# 오, 위, 왼, 아
dx = [0, -1, 0, 1] # 위아래 이동
dy = [1, 0, -1, 0] # 좌우 이동

# 현재 위치
x, y = 2, 2

for i in range(4):
  # 다음 위치
  nx = x + dx[i]
  ny = y + dy[i]
  print(nx, ny) 