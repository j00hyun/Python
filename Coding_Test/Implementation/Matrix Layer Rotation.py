# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem?isFullScreen=true

# 이 문제를 선형 배열로 푸는 방법은, 2D 매트릭스를 1D 배열로 변환하여 순차적으로 회전한 후, 다시 2D 매트릭스로 복원하는 방법입니다. 이 접근법을 사용하면 매트릭스의 회전 연산을 더 효율적으로 할 수 있습니다. 각 레벨을 선형 배열로 변환하여 다루면 회전 연산을 더 쉽게 처리할 수 있습니다.

# 방법 설명
#   1. 매트릭스 레벨 추출
#     - 매트릭스는 여러 개의 "레벨"로 나눌 수 있습니다. 각 레벨은 매트릭스의 외곽을 따라가는 원형 구조를 가집니다.
#     - 예를 들어, 4x4 매트릭스는 2개의 레벨로 나눠서 처리할 수 있습니다. 첫 번째 레벨은 외부 테두리이고, 두 번째 레벨은 내부의 테두리입니다.

#   2. 레벨을 선형 배열로 변환
#     - 각 레벨을 시계방향 또는 반시계방향으로 한 번에 순차적으로 배열로 변환합니다.

#   3. 배열 회전
#     - 배열에서 회전 연산을 진행합니다. 이때 회전 연산은 r번 만큼 회전시키면 됩니다.

#   4. 회전된 배열을 다시 매트릭스 형태로 복원
#     - 회전된 선형 배열을 원래 매트릭스의 위치에 맞게 다시 배치합니다.

# 단계별 구현:
#   1. 매트릭스에서 레벨 추출
#     각 레벨은 매트릭스의 외곽을 순차적으로 따라가며 선형 배열로 추출합니다. 예를 들어, 상단, 우측, 하단, 좌측을 차례대로 따라가며 배열로 만듭니다.

#   2. 배열 회전
#     회전하려는 배열에서 r % len(level) 만큼 회전하면 됩니다. (len(level)은 배열의 길이, r은 회전 횟수)

#   3. 매트릭스 복원
#     회전된 배열을 원래 매트릭스의 각 레벨에 다시 넣습니다.

def matrixRotation(matrix, r):
    m, n = len(matrix), len(matrix[0])
    
    # 1. 각 레벨 추출
    def extract_level(matrix, level):
        result = []
        top, left = level, level
        bottom, right = m - level - 1, n - level - 1

        # 상단
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        # 우측
        for i in range(top + 1, bottom + 1):
            result.append(matrix[i][right])
        # 하단
        if bottom > top:
            for i in range(right - 1, left - 1, -1):
                result.append(matrix[bottom][i])
        # 좌측
        if right > left:
            for i in range(bottom - 1, top, -1):
                result.append(matrix[i][left])
        
        return result
    
    # 2. 배열을 원형으로 회전
    def rotate_level(level, r):
        length = len(level)
        r = r % length  # r이 level의 길이보다 클 수 있으므로 모듈러 연산으로 회전 범위 설정
        return level[r:] + level[:r]
    
    # 3. 회전된 배열을 다시 매트릭스에 채우기
    def fill_level(matrix, level, level_num):
        result = []
        top, left = level_num, level_num
        bottom, right = m - level_num - 1, n - level_num - 1
        idx = 0

        # 상단
        for i in range(left, right + 1):
            matrix[top][i] = level[idx]
            idx += 1
        # 우측
        for i in range(top + 1, bottom + 1):
            matrix[i][right] = level[idx]
            idx += 1
        # 하단
        if bottom > top:
            for i in range(right - 1, left - 1, -1):
                matrix[bottom][i] = level[idx]
                idx += 1
        # 좌측
        if right > left:
            for i in range(bottom - 1, top, -1):
                matrix[i][left] = level[idx]
                idx += 1

    # 4. 모든 레벨에 대해 회전 적용
    num_levels = min(m, n) // 2
    for level in range(num_levels):
        level_elements = extract_level(matrix, level)
        rotated_level = rotate_level(level_elements, r)
        fill_level(matrix, rotated_level, level)

    # 결과 출력
    for row in matrix:
        print(" ".join(map(str, row)))

