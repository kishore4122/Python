
'''
# Arithmetic operators
a = 10
b = 20

total = a + b
print(total)

total = a - b
print(total)

total = a * b
print(total)

total = a / b
print(total)

total = a % b
print(total)

total = a ** b
print(total)


# Comparison operators
a = 30
b = 60

out = (a > b)
print(out)

out = (a < b)
print(out)

out = (a == b)
print(out)

out = (a != b)
print(out)

out = (a >= b)
print(out)

out = (a <= b)
print(out)


# Assignmnet operators
a = 0
b = 1

#a+=b a = a + b
#print(a)

a-=b # a = a - b
print(a)


#Logical operators ( or   ---   and )
a = 40
b = 60

x = 2
y = 3

out = (a > b) or (x < y)    # False or True
print(out)                  # True

out = (a > b) or (x > y)    # False or False
print(out)                  # False


out = (a > b) and (x < y)   # False and True
print(out)                  #False

out = (a < b)  and (x < y)  #True and True
print(out)                  #Ture

out = (a > b) and (x > y)   #False and False
print(out)                  #False


# 
a = 1
b = 2

out = (a > b)   #False
print(out)      #False

out = not(a > b)    #not (False) --> True
print(out)          #True

out = (a < b)       # True
print(out)          #True

out = not(a < b)    #not (True) --> False
print(out)          #False

# Membership operators
string = "Ironman is the best suerhero in marvel" # best word is preset in the text so it return true
ans = "best" in string
print(ans)

ans = "hello" not in string
print(ans)

#Identity operators
a = 12
b = 15

result = a is b
print(result)

result = a is not b
print(result)


a = "letter"
b = "letter"

#out = a is b
#print(out)

#out = a is not b
#print(out)

out = a == b
print(out)


'''














