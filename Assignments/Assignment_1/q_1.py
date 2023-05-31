# Brute force
def getIndices(array: list, target: int):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] != array[j] and array[i] + array[j] == target:
                return [i, j]


if __name__=='__main__':
    a = [2,7,11,11,15]
    t = 9
    print(getIndices(a, t))