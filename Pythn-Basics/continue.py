'''
for i in "Devops":
    if i == "o":
        print("found data")
        continue
    print(i)

'''
import random
vaccines = ["covaxin", "covishield", "pfzier", "moderna"]

lucky = random.choice(vaccines)
print(lucky)

for vac in vaccines:
    print(f"{vac} vaccine is testing")
    if vac == lucky:
        print(f"{vac} test is successful")
        continue
    print(f"{vac} test is failed")