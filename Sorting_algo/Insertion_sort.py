# creates randomized arrays for testing
def create_array(size=10, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]


# applies insertion sort to input array 'a'
def insertion_sort(a):
    for sort_len in range(1, len(a)):
        cur_item = a[sort_len] # next unsorted item
        insert_idx = sort_len # current index of item
        
        # iterate until we reach correct insert spot
        while insert_idx>0 and cur_item<a[insert_idx-1]:
            a[insert_idx] = a[insert_idx-1] #shift
            insert_idx += -1
            
        # insert item at correct spot
        a[insert_idx] = cur_item       
    return a


def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i-1]>arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swapped = True              
    return arr


def selection_sort(a):
    sort_len = 0 # length of current sorted portion
    while sort_len<len(a):
        min_idx = None # index of smallest item found
        for i, elem in enumerate(a[sort_len : ]):
            # check elem to see if smallest
            if min_idx == None or elem < a[min_idx]:
                # update with current smallest
                min_idx = i + sort_len
        a[sort_len], a[min_idx] = a[min_idx], a[sort_len]
        sort_len += 1  
    return a


def benchmark(n=[10, 100, 1000, 10000]):
    from time import time
    insertion_time = []
    bubble_time = []
    selection_time = []
    
    for size in n:
        a = create_array(size, size)
        
        t0 = time()
        bubble_sort(a)
        t1 = time()
        bubble_time.append(t1-t0)
        
        t0 = time()
        selection_sort(a)
        t1 = time()
        selection_time.append(t1-t0)
        
        t0 = time()
        insertion_sort(a)
        t1 = time()
        insertion_time.append(t1-t0)
    
    print("\n n\tInsertion\t\tBubble\t\tSelection")
    print(50*"_")
    for i,size in enumerate(n):
        print(f"{size}\t{insertion_time[i]:.5f}\t\t{bubble_time[i]:.5f}\t\t{selection_time[i]:.5f}")


if __name__ == "__main__":
    a = create_array()
    print(a)
    s = insertion_sort(a)
    print(s)
    benchmark()