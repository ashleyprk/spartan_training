# [입력]
# 테스트 케이스의 개수
T = int(input())
for tc in range(1, T+1):
    N = int(input())
 
    lst = [0, 0, 0, 0, 0]
 
    while N % 2 == 0:
        # N이 2로 나눠지면
        lst[0] += 1
        # lst의 첫번째 원소에 1을 더하고
        N //= 2
        # 그 N을 실제로 2로 나눠라 
     
    while N % 3 == 0:
        lst[1] += 1
        N //= 3
 
    while N % 5 == 0:
        lst[2] += 1
        N //= 5
     
    while N % 7 == 0:
        lst[3] += 1
        N //= 7
 
    while N % 11 == 0:
        lst[4] += 1
        N //= 11
 
    # answer = ' '.join(lst) join()은 문자열만 이어붙일 수 있다
    # 정수를 문자열로 바꾸고 그것을 join 시킨다
    answer = ' '.join(map(str, lst))
         
    print(f'#{tc} {answer}')