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