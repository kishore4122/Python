'''
def qwe(x):
    a = 0
    for b in x:
        a = a + b
    return a

out=qwe([1,2,3,4,5])
print(out)
'''

def greetings(msg):  # def greetings(msg="Morning"):
    print(f"Good {msg}")

greetings("Morning")