from typing import List

"""brute force"""
def count_freq(arr:List):
    n=len(arr)
    visited=[False]*n

    for i in range(n):
        if visited[i]:
            continue

        count=1
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                count+=1
                visited[j]=True


        print(arr[i],count)

#count_freq([1,3,4,2,1,2,4,5,3,2])


"""using default dict"""

from collections import defaultdict

def freq(arr):
    n=len(arr)

    freq_map=defaultdict(int)

    for i in range(n):
        freq_map[arr[i]]=freq_map[arr[i]]+1


    for key,value in freq_map.items():
        print(key,value)


#freq([1,3,4,2,1,2,4,5,3,2])


"""using dictionary"""
"""get(x,0) will see fetch value of key x and incr value by 1 if key is not present ie 0 it will add key and incr value to 1"""

def dic_freq(arr):
    freq_d={}

    for x in arr:
        freq_d[x]=freq_d.get(x,0)+1


    for key,value in freq_d.items():
        print(key,value)


#dic_freq([1,3,4,2,1,2,4,5,3,2])


"""using counter"""
from collections import Counter
def counter_freq(arr):

    freq_c=Counter(arr)

    for key,val in freq_c.items():
        print(key,val)


counter_freq([1,3,4,2,1,2,4,5,3,2])
