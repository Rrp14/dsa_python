def find_leader(nums):
    n=len(nums)
    leader=[nums[n-1]]
    sub_leader = leader[0]

    for i in range(n-2,-1,-1):

        if nums[i]>sub_leader:
            leader.append(nums[i])
            sub_leader=nums[i]

    leader.reverse()
    print(leader)

find_leader([10, 22, 12, 3, 0, 6] )