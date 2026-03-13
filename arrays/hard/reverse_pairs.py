from sortedcontainers import SortedList
def reverse_pair(nums):

    st=SortedList()
    cnt=0

    for v in nums:
        cnt+=len(st)-st.bisect_right(v*2)
        st.add(v)

    return cnt

