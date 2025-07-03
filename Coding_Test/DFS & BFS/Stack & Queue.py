################################ 스택 구현 #############################

stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5) # 시간 복잡도 O(1)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() # 시간 복잡도 O(1)
stack.append(1)
stack.append(4)
stack.pop()

# 최상단 원소부터 출력
print(stack[::-1]) # [1, 3, 2, 5]
# 최하단 원소부터 출력
print(stack) # [5, 2, 3, 1]

################################# 큐 구현 ##############################

from collections import deque

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5) # 시간 복잡도 O(1)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # 시간 복잡도 O(1)
queue.append(1)
queue.append(4)
queue.popleft()

# 먼저 들어온 순서대로 출력
print(queue) # deque([3, 7, 1, 4])
# 나중에 들어온 원소부터 출력
queue.reverse() # 역순으로 바꾸기 
print(queue) # deque([4, 1, 7, 3])
