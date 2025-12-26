# constructs randomized array of length 'size', each element
# is randomly selected from the range 0 up to 'max'
def create_array(size=10, max=50):
    from random import randint
    return[randint(0,max) for _ in range(size)]


def merge(a,b):
    c = [] # final output array
    a_idx, b_idx = 0,0
    while a_idx<len(a) and b_idx<len(b):
        if a[a_idx]<b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
            
    if a_idx == len(a): c.extend(b[b_idx:])
    else:               c.extend(a[a_idx:])
    return c


def merge_sort(a):
    # a list of zero or one elements is sorted, by definition
    if len(a)<=1: return a
    
    # split the list in half and call merge sort recursively on each half
    left, right = merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:])
    
    # merge the sorted sublists
    return merge(left, right)


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


def benchmark(n=[10,100,1000,10000]):
    times = {'bubble':[],'selection':[], 'insertion':[],'merge':[]}
    from time import time
    for size in n:
        arr = create_array(size, size)
        t0 = time()
        bubble_sort(arr)
        t1 = time()
        times['bubble'].append(t1-t0)
        
        arr = create_array(size, size)
        t0 = time()
        selection_sort(arr)
        t1 = time()
        times['selection'].append(t1-t0)
        
        arr = create_array(size, size)
        t0 = time()
        insertion_sort(arr)
        t1 = time()
        times['insertion'].append(t1-t0)
        
        arr = create_array(size, size)
        t0 = time()
        merge_sort(arr)
        t1 = time()
        times['merge'].append(t1-t0)
        
    print("\nn \tBubble\t\tSelection\t\tInsertion\t\tMerge")
    print(100*"_")
    for i, cur_n in enumerate(n):
        print(f"{cur_n}\t{times['bubble'][i]:.5f}\t\t{times['selection'][i]:.5f}\t\t{times['insertion'][i]:.5f}\t\t{times['merge'][i]:.5f}")


if __name__ == "__main__":
    a = create_array()
    print(a)
    s = merge_sort(a)
    print(s)
    benchmark()