def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    idx = 0
    
    while (k > 0):
        if food_times[idx] > 0:
            food_times[idx] -= 1
            k -= 1
        idx = (idx + 1) % len(food_times)

    while food_times[idx] == 0:
        idx = (idx + 1) % len(food_times)
    
    answer = idx + 1
        
    return answer

print(solution([3,1,2], 5))

# 어떻게 하면 O(N^2) -> O(NlogN)으로 줄일 수 있을지 고민해보기
# 조건이 까다로울 수록 단순하게 만들기 위해 노력할 것
# -1 출력 -> 최대한 빨리 처리될 방법은 없을지 생각할 것
# NlogN? -> quick sort, heap sort, priority queue, ... 등을 떠올리기