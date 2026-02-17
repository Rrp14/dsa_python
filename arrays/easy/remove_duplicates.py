def removeDuplicates(nums):
    if not nums:
        return 0

    k=1
    for i in range(1,len(nums)):

        if nums[i]!=nums[i-1]:
            nums[k]=nums[i]
            k+=1

    print(nums)
    return k

k=removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(k)


"""brute force using set"""

def rem_dup(nums):
    if not nums:
        return 0

    index=0
    seen=set()

    for num in nums:
        if num not in seen:
            seen.add(num)
            nums[index]=num
            index+=1
    print(nums)
    return index

rem_dup([0,0,1,1,1,2,2,3,3,4])




