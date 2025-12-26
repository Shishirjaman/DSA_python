from random import randint

# create randomized array of length 'size' with values range
# 0 to 'max'
def create_array(size=10, max=50):
    return [randint(0,max)for _ in range(size)]


# insertion sort algorithm
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


# bucket sorting algorithm
def bucket_sort(arr):
    n = len(arr)
    if n <= 1: return arr
    
    # create empty buckets
    buckets = []
    for i in range(n):
        buckets.append([])
        
    # part 1: Normalize and place into bucketes
    max_val = max(arr)
    for num in arr:
        normalized = num / (max_val + 1)
        bucketNumber = int(n* normalized)
        buckets[bucketNumber].append(num)
        
    # part 2: sort each bucket
    for bucket in buckets:
        insertion_sort(bucket)
        
    # part 2: combine sorted buckets
    output = []
    for bucket in buckets:
        output.extend(bucket)
        
    return output


if __name__ == "__main__":
    arr = create_array()
    print(arr)
    s_arr = bucket_sort(arr)
    print(s_arr)