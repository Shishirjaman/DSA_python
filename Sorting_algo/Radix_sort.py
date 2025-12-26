from random import randint

def create_array(size=20, max=10000):
    return [randint(10,max)for _ in range(size)]


def count_sort_digit(arr, exp, base=10):
    """
    Stable counting sort of arr[] according to the digit at position 'exp'.
    exp = 1 for units, 10 for tens, 100 for hundreds, ...
    base = 10 for decimal numbers.
    """
    count = [0] * base

    # 1) Count frequency of each digit
    for num in arr:
        digit = (num // exp) % base
        count[digit] += 1

    # 2) Prefix sums
    for i in range(1, base):
        count[i] += count[i - 1]

    # 3) Build output (right-to-left for stability)
    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        digit = (num // exp) % base
        count[digit] -= 1
        pos = count[digit]
        output[pos] = num

    return output


def radix_sort(arr):
    """
    LSD radix sort using count_sort_digit as the stable subroutine.
    Works for non-negative integers.
    """
    n = len(arr)
    if n <= 1:
        return arr

    #a = list(arr)
    max_value = max(arr)
    exp = 1
    base = 10

    while max_value // exp > 0:
        arr = count_sort_digit(arr, exp, base)
        exp *= 10

    return arr


if __name__ == "__main__":
    data = create_array()
    print("Original:", data)
    sorted_data = radix_sort(data)
    print("Sorted:  ", sorted_data)
