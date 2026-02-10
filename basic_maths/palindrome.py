def is_palindrome(x: int) -> bool:
    g=str(x)

    if g[0]=="-":
        return False

    g=g[::-1]
    g=int(g)

    if g !=x:
        return False
    return True


