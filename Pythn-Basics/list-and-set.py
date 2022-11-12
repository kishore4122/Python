'''
my_list = ["kishroe", "chandra", "govindu"]
print(my_list)
print(type(my_list))

print(my_list[1]) # print the value based on index in the list

print()

for i in my_list:
    print(i)
    for x in i:   # nested loop
        print(x)


my_set = {"kishore", "chandra", "govindu"}
print(my_set)
print(type(my_set))

print()

for i in my_set:
    print(i)
    for x in i:
        print(x)


my_list = ["kishroe", "chandra", "govindu"]

my_list.append("kishorechandra")
print(my_list)

my_list.remove("kishroe")
print(my_list)


my_set = {"kishore", "chandra", "govindu"}

my_set.add("kishroechandra")
print(my_set)

my_set.remove("kishore")
print(my_set)

my_set.update({"krish"})
print(my_set)

'''

