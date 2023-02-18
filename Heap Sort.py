def heapify(nums, length, i):
    largest = i
    l = i*2+1
    r = i*2+2
    if l<length and nums[l]>nums[largest]:
        largest = l
    if r<length and nums[r]>nums[largest]:
        largest = r
    if largest != i:
        nums[largest], nums[i] = nums[i], nums[largest]
        heapify(nums, length, largest)

def heapsort(nums):
    length = len(nums)
    for i in range((length//2)-1, -1, -1):
        heapify(nums, length, i)
    for i in range(length-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    return nums

print(heapsort([5,3,1,7,4]))