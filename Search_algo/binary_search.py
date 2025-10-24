#binary search can be performed only in a sorted array
#if an array is not sorted first you need to sort it before applying binary search

#binary search in iterative method (using loop)
def binarySearchIterative(array, x, low, high):
    
    while low <= high:
        
        mid = low + (high - low)//2

        if x == array[mid]:
            return mid

        elif x > array[mid]:
            low = mid + 1

        else:
            high = mid - 1

    return -1

#binary search in recursive method
def binarySearchRecursive(array, x, low, high):
    if high >= low:
        mid = low + (high - low)//2

        if x == array[mid]:
            return mid

        elif x > array[mid]:
            return binarySearchRecursive(array, x, mid+1, high)

        else:
            return binarySearchRecursive(array, x, low, mid-1)
    
    else:
        return -1



if __name__ == "__main__":
    array = [3, 4, 5, 6, 7, 8, 9]
    x1 = 9
    x2 = 10

    result1 = binarySearchIterative(array, x1, 0, len(array)-1)
    result2 = binarySearchRecursive(array, x2, 0, len(array)-1)

    if result1 != -1:
        print("Element is present at index " + str(result1))

    else:
        print("Not found")

    if result2 != -1:
        print("Element is present at index "+ str(result2))

    else:
        print("Not found")


