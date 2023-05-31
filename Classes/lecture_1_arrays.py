import sys
# Q2

def get_max_profit(array: list) -> int:
    """Returns the maximum profit between two prices without selling 
       in the past

    Args:
        array (list): array of prices

    Returns:
        int: maximum profit between two prices
    """
    min_val = sys.maxsize
    max_profit = 0

    for price in array:
        if price < min_val:
            min_val = price
        elif price - min_val > max_profit:
            max_profit = price - min_val

    return max_profit


# Q3

# def maxSubarray(array: list) -> list:

    

if __name__ == '__main__':
    print (
        get_max_profit([10,2,5,3,6,4,9])
        )
