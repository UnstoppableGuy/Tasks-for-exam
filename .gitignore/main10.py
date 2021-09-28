def merge_sort(l, r):
    if r - l <= 1:
        return
    d = (l + r) // 2
    merge_sort(l, d)
    merge_sort(d, r)
    ll, rr = l, d
    sorted = []
    while ll < d or rr < r:
        if ll != d and (rr == r or arr[ll] <= arr[rr]):
            sorted.append(arr[ll])
            ll += 1
        else:
            sorted.append(arr[rr])
            rr += 1
    for i in range(l, r):
        arr[i] = sorted[i - l]


arr = [1, 3, 19, 14, 2, 10, 2, 1, -10, 1000, 0]
merge_sort(0, len(arr))
print(arr)


def merge(left_list, right_list):  
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_length, right_list_length = len(left_list), len(right_list)
    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):  
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)

random_list_of_nums = [120, 45, 68, 250, 176]  
random_list_of_nums = merge_sort(random_list_of_nums)  
print(random_list_of_nums)