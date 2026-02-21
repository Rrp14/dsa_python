def longestSubarray(nums):
    k=0
    seen={}
    max_count=0
    pre_sum=0

    for i,num in enumerate(nums):
        pre_sum+=num


        if pre_sum==k:
            max_count=i+1

        if pre_sum-k in seen:
            max_count=max(max_count,i-seen[pre_sum-k])

        if pre_sum not in seen:
            seen[pre_sum]=i


    return max_count



ans=longestSubarray([9, -3, 3, -1, 6, -5])
print(ans)
