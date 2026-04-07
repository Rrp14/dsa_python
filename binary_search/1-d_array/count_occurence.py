def find(nums,target):

    def first_occur():
        left, right = 0, len(nums) - 1
        first= -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                first = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first

    def last_occur():
        left, right = 0, len(nums) - 1
        last=-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                last= mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last

    return [first_occur(),last_occur()]

res=find([2, 2 , 3 , 3 , 3 , 3 , 4],3)

if res[0]==-1:
    print("0")
else:
    print(res[1]-res[0]+1)
