# creates array of length 'size', each  element is 
# randomly selected from the range (0, max)

def create_array(size=10, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]

# performs the selection sort algorithm on the passed
# list, returns the sorted version
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

# applies bubble sort to input array
def bubble_sort(a):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(a)):
            if a[i-1] > a[i]:
                a[i], a[i-1] = a[i-1], a[i]
                swapped = True
    
    return a

# benchmark of selection sort against bubble and built-in sorting method 
def bechmark(n=[10, 100, 1000, 10000]):
    bub_times = []
    sel_times = []
    builtin_times = []

    from time import time

    for length in n:
        a = create_array(length, length)
        
        t0 = time()
        s = sorted(a)
        t1 = time()
        builtin_times.append(t1 - t0)
        
        t0 = time()
        s = bubble_sort(a)
        t1 = time()
        bub_times.append(t1 - t0)
        
        t0 = time()
        s = selection_sort(a)
        t1 = time()
        sel_times.append(t1 - t0)
        
    print("n \tBuilt-in\tBubble\t\tSelection")
    print("______________________________________________________")
    for i, cur_n in enumerate(n):
        print(f"{cur_n}\t{builtin_times[i]:.5f}\t\t{bub_times[i]:.5f}\t\t{sel_times[i]:.5f}")
        
        

if __name__ =="__main__":
    a = create_array()
    print("Unsorted: ", a)
    a = selection_sort(a)
    print("Sorted: ", a)
    bechmark()