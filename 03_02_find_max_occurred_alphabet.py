
# 각 알파벳들을 하나하나 문자열과 비교하면서 몇 번 나왔는지 확인하는 방법
input = "hello my name is sparta"
char = "a"

def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0

    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence

    return chr(max_alphabet_index + ord("a"))

    print(max_alphabet_index)
    chr(max_alphabet_index + ord("a"))


result = find_max_occurred_alphabet(input)
print(result)
