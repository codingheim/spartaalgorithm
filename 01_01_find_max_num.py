input = [3, 5, 6, 1, 2, 4]


# 숫자를 하나씩 비교하면서 진행하는 방법
def find_max_num(array):
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
        else:
            return num


result = find_max_num(input)
print(result)
