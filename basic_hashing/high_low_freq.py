"""using brute force """
def count_freq(arr):
    n=len(arr)
    visited=[False]*n
    max_freq=0
    min_freq=n
    max_ele=0
    min_ele=0

    for i in range(n):
        if visited[i]:
            continue

        count=1
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                count+=1
                visited[j]=True


        if count > max_freq:
            max_ele=arr[i]
            max_freq=count

        if count<min_freq:
            min_ele=arr[i]
            min_freq=count


    print(f"element {max_ele} has highest freq {max_freq} "
              f" while element {min_ele} has lowest freq {min_freq}")

#count_freq([1,2,3,1,3,5,6,3,2,1,3,4,4,5,6,3,2,2,3,1,4,5,2])


"""using dictionary or inbuilt collections"""

from collections import Counter

def counter_freq(arr):

    freq=Counter(arr)

    min_ele=0
    max_ele=0
    min_freq=len(arr)
    max_freq=0

    for element,count in freq.items():
        if count > max_freq:
            max_freq=count
            max_ele=element

        if count < min_freq:
            min_freq=count
            min_ele=element

    print(f"element {max_ele} has highest freq {max_freq} "
          f" while element {min_ele} has lowest freq {min_freq}")


counter_freq([1,2,3,1,3,5,6,3,2,1,3,4,4,5,6,3,2,2,3,1,4,5,2])