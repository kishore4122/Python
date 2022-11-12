'''
def result(arg1, arg2):
    total = arg1 + arg2
    return total

print(result(2,3))


def adder(arg1, arg2):
    total = arg1 + arg2
    print(total)

#adder(10, 50)
print(adder(10, 50))
'''

def summ(arg):
    x = 0
    for i in arg:
        x = x + i
    return x

total = summ([2, 5, 10])
print(total)
#print(summ([1,2,3,4,5]))