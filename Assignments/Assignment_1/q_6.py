def find_duplicate(array: list):
    for i in array:
        for j in array[i:]:
            if i == j:
                return True
            else:
                return False

if __name__ == '__main__':
    arr = [1,1,2,2,3]
    print(find_duplicate(arr))