# https://www.hackerrank.com/challenges/reverse-shuffle-merge/problem?isFullScreen=true

##### 해설

# 1. reverse 와 shuffle에 필요한 알파벳의 수를 각각 저장
# 2. 주어진 문자열을 뒤에서부터 한 개씩 차례대로 탐색
# 3. 만약 해당 알파벳이 reverse에 모두 가득 차있다면 무조건 shuffle에 포함시킴
# 4. 해당 알파벳이 reverse에 들어갈 자리가 있다면
#     - 이전 reverse에 들어간 알파벳이 현재 알파벳보다 크고 shuffle에 넣을 자리가 있다면 계속 reverse에서 빼 shuffle에 넣기
#     - 그 후, reverse에 넣기

# 예시: aaacbacaba -> 답: aaabc (aaa'cba'c'a'b'a')
# reverse: a:3, b:1, c:1 ()
# shuffle: a:3, b:1, c:1 ()

# 1. reverse에 a를 넣음
#    reverse: a:2, b:1, c:1 (a)
#    shuffle: a:3, b:1, c:1 ()

# 2. reverse에 b를 넣음
#    reverse: a:2, b:0, c:1 (ab)
#    shuffle: a:3, b:1, c:1 ()

# 3. a를 reverse에 넣기 전 b는 a보다 크고 shuffle에 들어갈 자리가 있으므로 b의 위치 변경
#    reverse: a:2, b:1, c:1 (a)
#    shuffle: a:3, b:0, c:1 (b)

# 4. reverse에 a를 넣음
#    reverse: a:1, b:1, c:1 (aa)
#    shuffle: a:3, b:0, c:1 (b)

# 5. reverse에 c를 넣음
#    reverse: a:1, b:1, c:0 (aac)
#    shuffle: a:3, b:0, c:1 (b)

# 6. a를 reverse에 넣기 전 c는 a보다 크고 shuffle에 들어갈 자리가 있으므로 c의 위치 변경
#    reverse: a:1, b:1, c:1 (aa)
#    shuffle: a:3, b:0, c:0 (bc)

# 7. reverse에 a를 넣음
#    reverse: a:0, b:1, c:1 (aaa)
#    shuffle: a:3, b:0, c:0 (bc)

# 8. reverse에 b를 넣음
#    reverse: a:0, b:0, c:1 (aaab)
#    shuffle: a:3, b:0, c:0 (bc)

# 9. reverse에 c를 넣음
#    reverse: a:0, b:0, c:0 (aaabc)
#    shuffle: a:3, b:0, c:0 (bc)

# 10. reverse에 a를 위한 자리가 없으므로 3개의 a를 모두 shuffle에 넣음
#    reverse: a:0, b:0, c:0 (aaabc)
#    shuffle: a:0, b:0, c:0 (bcaaa)