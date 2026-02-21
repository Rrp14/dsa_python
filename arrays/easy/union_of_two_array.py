"""using map"""
def union(nums1,nums2):
    freq={}


    for x in nums1:
        freq[x]=freq.get(x,0)+1

    for x in nums2:
        freq[x]=freq.get(x,0)+1

    result=sorted(freq.keys())




    print(result)





union([4,3,2,1],[2,3,4,5])


"""using set"""

def union_of_two_array_set(num1,num2):
    set_arr=set()
    new_arr=[]

    for num in num1:
        if num not in set_arr:
         set_arr.add(num)
         new_arr.append(num)



    index=0

    for num in num2:
        if num not in set_arr:
         set_arr.add(num)
         new_arr.append(num)



    new_arr.sort()
    print(new_arr)


union_of_two_array_set([4,3,2,1],[2,3,4,5])


"""simple method"""
def union_of_two_arr_set2(num1, num2):
    print(list(set(num1) | set(num2)))
    
union_of_two_arr_set2([4,3,2,1],[2,3,4,5])

