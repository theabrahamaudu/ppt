def move_zeros(array: list) -> list:
    for i in array:
        if i == 0:
            array.remove(i)
            array.append(i)
    return array

if __name__ == '__main__':
    array = [0,1,0,3,12]
    print(move_zeros(array))