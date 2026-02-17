"""using map"""
def union(nums1,nums2):
    freq={}
    new_num=[]

    for x in nums1:
        freq[x]=freq.get(x,0)+1

    for x in nums2:
        freq[x]=freq.get(x,0)+1

    freq=dict(sorted(freq.items()))

    for k,v in freq.items():
        new_num.append(k)


    print(new_num)





union([4,3,2,1],[2,3,4,5])
