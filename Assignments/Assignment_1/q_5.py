def merge_sort(array_1: list, array_2: list) -> list:
    tmp_array = []
    for i in range(len(array_1)):
        if array_1[i] != 0 and array_2[i] < array_1[i]:
            tmp_array.append(array_1[i])
            tmp_array.append(array_2[i])
        elif array_1[i] != 0 and array_2[i] > array_1[i]:
            tmp_array.append(array_2[i])
            tmp_array.append(array_1[i])

    tmp_array.sort()
    return tmp_array


if __name__ == "__main__":
    a_1, a_2 = [1, 2, 3, 0, 0, 0], [2, 5, 6]

    print(merge_sort(a_1, a_2))
