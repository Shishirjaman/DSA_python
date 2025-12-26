from random import randint

# create randomized array of length 'length',
# array integers are of range 0, maxint
def create_array(length=10, maxint=50):
    new_arr = [randint(0, maxint) for _ in range(length)]
    return new_arr


# apply bubble sort algorithm to the  input array
def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swapped = True                
    return arr

# returns true if the passed array is sorted, else false
def is_sorted(arr):
    sorted_arr = sorted(arr)
    return arr == sorted_arr

# benchmarks the bubble sort against the built in python sorting method
def benchmark(n=[10, 100, 1000, 10000]):
    from time import time
    b0 = [] # bubble sort times
    b1 = [] # built-in sort times
    for length in n:
        a = create_array(length, length)
        
        t0 = time()
        s = sorted(a) # sort with built in
        t1 = time()
        b1.append(t1 - t0) # record built in time
        
        t0 = time()
        s = bubble_sort(a) # sort with bubble sort
        t1 = time()
        b0.append(t1 - t0) # record bubble sort time
        
    print("n \tBuild-in\tBubble Sort")
    print("_____________________________________________")
    for i, cur_n in enumerate(n):
        print(f"{cur_n}\t{b1[i]:.5f}\t\t{b0[i]:.5f}")
    
    
if __name__ == "__main__":
    a = create_array()
    print(a)
    a = bubble_sort(a)
    print(a)

    print(is_sorted(a))

    benchmark()