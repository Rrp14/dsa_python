"""brute force"""

def is_palindrome(s:str)->bool:

    left,right=0,len(s)-1

    while left<right:

        if not s[left].isalnum():
            left+=1
        elif not s[right].isalnum():
            right-=1

        elif s[left].lower()!=s[right].lower():
            return False

        else:
            left+=1
            right-=1
    return True

print(is_palindrome("rahul"))


"""recursion"""
"""T,S=O(n) , brute force is better for space complexity"""

def is_palindrome_rec(i:int,s:str):

    if i>=len(s)//2:
        return True

    if s[i]!=s[len(s)-1-i]:
        return False

    return is_palindrome_rec(i+1,s)


print(is_palindrome_rec(0,"ABCBA"))




