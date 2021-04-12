def moveZeroes1(nums):
    i, position = 0, 0
    while i < len(nums):
        if nums[i] == 0:
            position += 1
        else:
            if position > 0:
                nums[i], nums[i-position] = nums[i-position], nums[i]
        i += 1
    return nums

def moveZeroes2(nums):
    l = len(nums)
    i = 0
    while i < l:
        if nums[i] == 0:
            nums.append(nums.pop(i))
            l -= 1
        else:
            i += 1
    return nums
            
nums=[0, 1, 0, 3, 12]
print(moveZeroes1(nums))
print(moveZeroes2(nums))