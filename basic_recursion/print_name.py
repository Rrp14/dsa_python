def print_name(name:str,n:int):

    if n==0:
        return

    print(name)
    print_name(name,n-1)


print_name("Rahul",0)


