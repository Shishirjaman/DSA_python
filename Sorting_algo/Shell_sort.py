from random import randint

# create randomized array of length 'size' with values range
# 0 to 'max'
def create_array(size=10, max=50):
    return [randint(0,max)for _ in range(size)]


def insertion_sort_gap(a, start, gap):
    """
    Generalised version of your insertion sort:
    sorts elements a[start], a[start+gap], a[start+2*gap], ...
    in-place using your insertion-sort logic.
    """
    # sort_len walks along this gapped subsequence
    for sort_len in range(start + gap, len(a), gap):
        cur_item = a[sort_len]      # next unsorted item in this subsequence
        insert_idx = sort_len       # current index of item

        # iterate until we reach correct insert spot, stepping by 'gap'
        while insert_idx - gap >= start and cur_item < a[insert_idx - gap]:
            a[insert_idx] = a[insert_idx - gap]  # shift by 'gap'
            insert_idx -= gap

        # insert item at correct spot
        a[insert_idx] = cur_item


def shell_sort(a):
    """
    Shell sort using your insertion-sort logic generalised to gaps.
    Gap sequence: n//2, n//4, ..., 1.
    """
    n = len(a)
    arr = list(a)  # optional: work on a copy

    gap = n // 2
    while gap > 0:
        # For this gap, run gapped insertion sort starting at each offset
        for start in range(gap):  # 0 .. gap-1
            insertion_sort_gap(arr, start, gap)
        gap //= 2  # shrink gap

    return arr


if __name__ == "__main__":
    data = create_array()
    print("Original:", data)
    print("Shell sorted:", shell_sort(data))