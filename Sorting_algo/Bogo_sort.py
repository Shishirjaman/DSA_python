from random import randint, shuffle

# create a randomize array of length 'size'
def create_array(size=10, max=50):
    return [randint(0,max) for _ in range(size)]

def is_sorted(a):
    for i in range(1, len(a)):
        if a[i]<a[i-1]: return False
    return True

def bogo_sort(a):
    ct = 0
    while not is_sorted(a):
        shuffle(a)
        ct += 1
    return ct, a


if __name__ == "__main__":
    arr = create_array(5,10)
    print(arr)
    itr, sorted_arr = bogo_sort(arr)
    print(sorted_arr)
    print("number of iteration: ", itr)
    