def menu(func, arch, cur):
    if func == 0:
        #삭제
        if cur in arch:
            arch.remove(cur)
    else:
        #설치
        arch.append(cur)
        
def check_gi(gi, bo):
    for x, y in gi:
        if y == 0:
            continue
        if [x, y - 1] in gi:
            continue
        if [x - 1, y] in bo or [x, y] in bo:
            continue
        return False
    return True

def check_bo(gi, bo):
    for x, y in bo:
        if [x, y - 1] in gi or [x + 1, y - 1] in gi:
            continue
        if [x - 1, y] in bo and [x + 1, y] in bo:
            continue
        return False
    return True

def solution(n, build_frame):
    answer = []
    gi = []
    bo = []
    
    # 형식에 맞춰 저장
    for frame in build_frame:
        x, y, a, b = frame
        cur_frame = [x, y]
        
        if b == 1: #설치
            if a == 0: #기둥
                gi.append(cur_frame)
                if not check_gi(gi, bo):
                    gi.remove(cur_frame)
            else: #보
                bo.append(cur_frame)
                if not check_bo(gi, bo):
                    bo.remove(cur_frame)
        else: #삭제
            tmp = cur_frame
            if a == 0:
                gi.remove(tmp)
            else:
                bo.remove(tmp)

            # 삭제 후에도 구조가 유지되는지 확인
            if not check_gi(gi, bo) or not check_bo(gi, bo):
                # 구조가 깨지면 다시 추가
                if a == 0:
                    gi.append(tmp)
                else:
                    bo.append(tmp)
                    
        answer = [[x, y, 0] for x, y in gi] + [[x, y, 1] for x, y in bo]
        
    return sorted(answer)

# answer 낼 때 + 를 사용해서 각각이 기둥과 보 각각이 아니라 한 번에 고려
# answer sort하는 거 잊지 말기
# 기둥이나 보를 삭제한 이후에 구조가 유지되는지 확인 중요 !!
# for문 인덱스 두 개 사용하여 순회하면서 [x, y] 이런 식으로 순회하는 방법이 있다
# 체크할 때는 삭제 때문에 해당 기둥이나 보 말고 전체를 확인해야 함