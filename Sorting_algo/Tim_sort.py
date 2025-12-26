from random import randint


# create an random array of length 'size' with values range 0 to 'max'
def create_array(size=100, max=500):
    return [randint(0,max)for _ in range(size)]


# typical small run size used in many TimSort explanations
MIN_RUN = 32


def insertion_sort(a):
    for sort_len in range(1, len(a)):
        cur_item = a[sort_len]  # next unsorted item
        insert_idx = sort_len   # current index of item
        
        # iterate until we reach correct insert spot
        while insert_idx > 0 and cur_item < a[insert_idx - 1]:
            a[insert_idx] = a[insert_idx - 1]  # shift
            insert_idx -= 1
        
        # insert item at correct spot
        a[insert_idx] = cur_item
    return a


def merge(a, b):
    c = []  # final output array
    a_idx, b_idx = 0, 0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1

    if a_idx == len(a):
        c.extend(b[b_idx:])
    else:
        c.extend(a[a_idx:])
    return c


def timsort(arr):
    """
    Simple TimSort-style implementation:
    1) Sort small runs with insertion sort.
    2) Merge runs in a bottom-up way using your merge().
    """
    n = len(arr)
    if n <= 1:
        return arr

    # ---- 1) Sort small runs with insertion sort ----
    # Step over the array in blocks of size MIN_RUN
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN, n)  # Python slicing end is exclusive
        # Sort this slice in-place using insertion sort
        arr[start:end] = insertion_sort(arr[start:end])

    # ---- 2) Merge runs, doubling run size each time ----
    size = MIN_RUN
    while size < n:
        # Merge pairs of runs of length 'size'
        for left in range(0, n, 2 * size):
            mid = left + size
            right = min(left + 2 * size, n)

            if mid < right:  # there is a right run to merge
                left_run = arr[left:mid]
                right_run = arr[mid:right]
                arr[left:right] = merge(left_run, right_run)

        size *= 2
    return arr


if __name__ == "__main__":
    data = create_array()
    print("Original:", data)
    print("Timsort: ", timsort(data))
