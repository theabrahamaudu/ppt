# Brute force

def remove_val(array: list, val: int):
    array.sort()
    for i in range(len(array)):
        if array[i] == val:
            array[i] = ''

    return array



if __name__ == '__main__':
    nums = [3,2,2,3]
    VAL = 3
    print(remove_val(nums, VAL))
