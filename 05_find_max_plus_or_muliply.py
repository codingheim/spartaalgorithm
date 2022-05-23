# Q. 다음과 같이 0 혹은 양의 정수로만 이루어진 배열이 있을 때,
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에
# '✕' 혹은 '+' 연산자를 넣어 결과적으로 가장 큰 수를 구하는 프로그램을 작성하시오.


# 내가 푼 방식
input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for number in array:
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        else:
            multiply_sum *= number
    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)

# 해답 풀이

input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for number in array:
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
    else:
        multiply_sum *= number
    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)


# 최대값과 최솟값


def solution(s):
    s = list(map(int, s.split()))
    return str(min(s)) + " " + str(max(s))


# 기능개선
# #Queue를 이용해서 구현
def solution(progresses, speeds):
    answer = []
    day = 1  # 날짜를 새는 변수
    count = 0  # 작업 완료된 기능을 카운트 하는 변수

    # 모든 기능이 완료되어 남은 기능이 없을때까지 반복
    while len(progresses) > 0:
        # 뒤의 기능이 완료가 되어도 앞의 기능이 완료되어야 배포가 가능하기 때문에 리스트의 첫번째 요소로 비교
        if progresses[0] + (day * speeds[0]) >= 100:
            # 기능이 완료되면 첫번째 요소를 제거
            progresses.pop(0)
            speeds.pop(0)

            # 완료된 기능 카운트
            count += 1
        else:
            # 완료된 기능이 있을경우 answer에 count를 넣고 count를 0으로 초기화한다.
            # 완료된 기능이 없을경우 날짜를 +1 해준다.
            if count > 0:
                answer.append(count)
                count = 0
            else:
                day += 1
    # 마지막 기능이 완료되면 안의 else문을 타지 않고 while문이 종료 되기 때문에 마지막 기능까지 추가해준다.
    answer.append(count)
    return answer


def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
