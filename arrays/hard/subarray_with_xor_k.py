"""brute force"""
def xor_array(nums,k):

    counter=0
    n=len(nums)

    for i in range(n):
        xor=0
        for j in range(i,n):
            xor^=nums[j]

            if xor==k:
                counter+=1
    return counter






"""optimal"""
def xor_hmap(nums,k):
    counter=0
    pre_xor=0
    seen={}

    for i,num in enumerate(nums):
        pre_xor^=num

        if pre_xor==k:
            counter+=1

        if pre_xor^k in seen:
            counter+=seen[pre_xor^k]

        seen[pre_xor]=seen.get(pre_xor,0)+1
    return counter

res=xor_hmap([4, 2, 2, 6, 4],6)
print(res)

