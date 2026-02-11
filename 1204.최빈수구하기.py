# 최빈수: 특정 자료에서 가장 여러 번 나타나는 값을 의미함
# 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력
T = int(input())
for _ in range(1, T+1):
    tc = int(input())
    nums = list(map(int, input().split()))

    # 최대 빈도수
    max_cnt = 0
    # 최빈값 중 최댓값 
    max_num = 0

    # i 인덱스가 T번 돌아갈때
    for i in range(len(nums)):
        cnt = 0
        # 값이 동일한게 나오면 
        for again in nums: 
            if nums[i] == again:
                # 빈도수를 1증가
                cnt += 1
        
        # 최대빈도수가 빈도수의 누적합보다 작으면
        if max_cnt < cnt:
            # 최대빈도수 갱신
            max_cnt = cnt
            # 해당 값은 최빈수임
            max_num = nums[i]
        
        # 최빈값 중 최댓값 출력하기 - ai 썼습니다.
        elif cnt == max_cnt:
            # 등장 횟수가 동일한 상황에서 더 큰 값을 선택 
            # 지금 저장된 최빈값(max_num)보다 현재 숫자가 더 크면
            if max_num < nums[i]:
                # 더 큰 값으로 갱신
                max_num = nums[i]
    
    print(f'#{tc} {max_num}')
        
