# [입력]
T = int(input())
# 학점 목록
score_lst = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for tc in range(1, T+1):
    # N: 학생 수, K번째 학생
    N, K = map(int, input().split())

    # 모든 학생의 총점을 저장할 리스트 
    scores = []
    # k번째 학생 총점 k
    k = 0

    for i in range(1, N+1):
        mid, final, hw = map(int, input().split())

        # 총점 계산
        total = mid * 0.35 + final * 0.45 + hw * 0.2
        # 전체 총점 리스트에 추가
        scores.append(total)
        
        # k번째 학생이라면
        if i == K:
            # k번째 학생의 총점을 따로 저장 
            k = total 

    # k번째 학생의 등수 계산
    rank_i = 0
    for s in scores:
        # 다른 학생의 점수가 k번째 학생의 총점보다 높다면
        if s > k:
            # 등수를 1 올린다
            rank_i += 1

    # 한 학점 당 몇 명인지 계산
    group = N // 10
    # 학점 인덱스 rank_i//group
    grade = score_lst[rank_i // group]


    # [출력]
    print(f'#{tc} {grade}')





