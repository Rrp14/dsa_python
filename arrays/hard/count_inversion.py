from sortedcontainers import SortedList
def count_inversion(nums):

    st=SortedList()
    cnt=0

    for v in nums:
        cnt+=len(st)-st.bisect_right(v)
        st.add(v)
    return cnt
res=count_inversion([5,4,3,2,1])
print(res)