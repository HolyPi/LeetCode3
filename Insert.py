

nums = [1, 3, 5, 6]
target = 5

def searchInsert(nums, target):
    if target in nums:
            return nums.index(target)
        
    for i in range(len(nums)):
        if nums[i] > target:
            return i
        
    return i + 1

print(searchInsert(nums, target))


#Time complexity: 0(n)
#Space complexity: 0(n)
