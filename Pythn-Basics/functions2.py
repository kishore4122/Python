# Variable length arguments

def order(min_order, *args):
    print(f"you have ordered {min_order}")
    print(args)
    for i in args:
        print(f"you have ordered {i}")


order("salad", "coke", "cool", "cake")