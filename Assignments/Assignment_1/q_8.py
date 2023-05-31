def find_duplicate(array: list) -> list[int]:
    for i in range(len(array)):
        if i < len(array) - 1:
            if array[i] == array[i+1]:
                return [array[i], array[i+1]+1]
            
if __name__ == '__main__':
    a = [1,2,2,4]
    print(find_duplicate(a))