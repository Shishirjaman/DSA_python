from random import randint

# create randomized unsorted array for testing
def create_array(size=10, max=50):
    return [randint(0,max)for _ in range(size)]


# applies quicksort to input array, returns sorted array
def quicksort(a):
    if len(a)<=1: return a
    
    smaller, equal, larger = [], [], []
    pivot = a[randint(0, len(a)-1)]
    
    for x in a:
        if x<pivot:     smaller.append(x)
        elif x==pivot:  equal.append(x)
        else:           larger.append(x)
        
    return quicksort(smaller)+equal+quicksort(larger)


def merge(a,b):
    c = []
    a_idx, b_idx = 0, 0
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


def merge_sort(arr):
    if len(arr)<=1: return arr
    left, right = merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:])
    
    return merge(left, right)


def benchmark(n=[10,100,1000,10000]):
    times={'quick':[], 'merge':[]}
    
    from time import time
    for size in n:
        arr = create_array(size, size)
        
        t0 = time()
        quicksort(arr)
        t1 = time()
        
        times['quick'].append(t1-t0)
        
        arr = create_array(size, size)
        t0 = time()
        merge_sort(arr)
        t1 = time()
        
        times['merge'].append(t1-t0)
        
    print("\nn\tQuick Sort\tMerge Sort")
    print(50*"_")
    for i,cur_n in enumerate(n):
        print(f"{cur_n}\t{times['quick'][i]:.5f}\t\t{times['merge'][i]:.5f}")


if __name__ == "__main__":
    a = create_array()
    print(a)
    s = quicksort(a)
    print(s)
    benchmark()