from typing import List


def linear_search(nums:List[int],ele:int)->int:
    n=len(nums)
    for i in range(n):
        if nums[i]==ele:
            return i

    return -1

index=linear_search([1,3,4,56,2,6,5],2)
if index==-1:
    print("not found")
else:
    print(f"element found at index {index}")

