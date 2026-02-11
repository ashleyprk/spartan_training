# 양 세기 문제: 양을 누가 이렇게 세
# 이전에 셌던 번호들의 각 자릿수에서 0에서 9까지의 모든 숫자를 보는것은
# ㅍ최소 몇 번 양을 센 시점일까
T = int(input())
for x in range(1, T+1):
    N = int(input())

    # 0~ 9까지 숫자를 봤는지 체크하는 배열 
    # 값이 1 => 봄
    # 값이 0 -> 못봄
    seen = [0] * 10

    # N, 2N, 3N, ... 중 K번째 양 세기
    k = 0

    while True:
        k += 1
        num = N * k

        # 각 자리 숫자 확인
        for i in str(num):
            seen[int(i)] = 1 # 봤으면 1로 표시

            # all_seen = 1 
            # 0~9 다 봤는지 검사
            for j in range(10):
                # 아직 한 번도 못 본 숫자라면
                if seen[j] == 0:
                    all_seen = 0
                    break
            if all_seen == 1:
                break 

    print(f'#{x} {k}') 
            
