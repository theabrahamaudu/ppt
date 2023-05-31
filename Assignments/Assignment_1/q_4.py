def increment_integer(array: list, increment: int):
    string = ''
    new_array = []

    for i in array:
        string = string + str(i)

    integer = int(string)
    integer += increment
    integer_str = str(integer)
    
    for i in integer_str:
        new_array.append(int(i))

    return new_array

if __name__ == '__main__':
    input_digits = [1,2,3]
    INCREMENT = 1

    print(increment_integer(input_digits, INCREMENT))
