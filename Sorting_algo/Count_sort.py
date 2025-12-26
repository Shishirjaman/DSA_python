from random import randint

# create a random array of length 'size' with number
# range between 0 to 'max'
def create_array(size=10,max=50):
    return[randint(0,max)for _ in range(size)]

# sort the unsorted element using count sort
def count_sort(arr): # input array with values as non-negative integers
    n = len(arr)
    if n <= 1: return arr
    
    max_value = max(arr)
    count = [0]*(max_value + 1)
    
    # count frequency of each element
    for num in arr:
        count[num] += 1
        
    # calculate prefix sum
    for i in range(1, len(count)):
        count[i] += count[i-1]
        
    # build output array
    output = [0]*n
    for i in range(n-1, -1, -1):
        a = arr[i]
        b = count[a] - 1
        output[b] = a
        count[a] -= 1
        
    return output


if __name__ == "__main__":
    arr = create_array(5, 10)
    print(arr)
    s_arr = count_sort(arr)
    print(s_arr) 