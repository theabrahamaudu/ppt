def target_index(array: list, target: int) -> int:
    LO = 0
    HI = len(array)-1

    while LO < HI:
        if array[LO] < target:
            LO +=1

        if array[HI] > target:
            HI -= 1

        if array[LO] == target:
            return LO
        
        elif array[LO] == array[HI]:
            return LO+1

if __name__ == '__main__':
    a = [1,3,5,6]
    TARGET = 6

    print(target_index(a, TARGET))