def linearSearch(array, size, num):
    for i in range(0, size):
        if(array[i] == num):
            return i
    return -1


if __name__ == "__main__":
    array = [2, 6, 8, 10, 3, 5, 1]
    x = 3

    n = len(array)

    result = linearSearch(array, n, x)

    if(result == -1):
        print("Element not found")

    else:
        print("Element is found")
