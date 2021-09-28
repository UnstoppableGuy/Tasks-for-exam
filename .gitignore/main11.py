import random


def quick_sort(l, r):
    if l >= r - 1:
        return
    d = (random.randint(l, r - 1))
    md = arr[d]
    i, j = l, r - 1
    while i <= j:
        while i < r and arr[i] < md:
            i += 1
        while j >= l and arr[j] > md:
            j -= 1
        if i <= j:
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t
            i += 1
            j -= 1
    quick_sort(l, i)
    quick_sort(i, r)


arr = [1, 3, 19, 14, 2, 10, 2, 1, -10, 1000, 0, -119]
quick_sort(0, len(arr))
print(arr)


def partition(nums, low, high):  
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):  
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

random_list_of_nums = [22, 5, 1, 18, 99]  
quick_sort(random_list_of_nums)  
print(random_list_of_nums) 