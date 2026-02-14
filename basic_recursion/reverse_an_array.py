"""brute force approach , lets pop last element to new list """
from typing import List


def reverse_arr_bf(arr:List):
    rev_arr=[]

    for _ in arr[:]:
        rev_arr.append(arr.pop())

    print(rev_arr)


arr1=[5,4,3,2,1,0]
reverse_arr_bf(arr1)

"""optimal reversal use left and right"""

def rev_arr_op(arr:List):
    left=0
    right=len(arr)-1

    while left<right:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    print(arr)

rev_arr_op([5,4,3,2,1,0])

"""using inbuilt reverse() gives o(1) space complexity """

def rev_arr_inb(arr:List):

    arr.reverse()
    print(arr)

rev_arr_inb([5,4,3,2,1,0])



"""using slicing: slicing in python it creates a copy so space is O(n) unlike O(1) in other languages"""
def rev_arr_slice(arr:List):


    arr[:]=arr[::-1]
    print(arr)


rev_arr_slice([5,4,3,2,1,0])