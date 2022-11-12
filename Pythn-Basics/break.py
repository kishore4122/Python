'''
for i in "Devops":
    print(i)
    if i == "v":     
        print("Found my data")
        break

print("out of loop")
'''

import random
vaccines = ["covaxin", "covishield", "pfzier", "moderna"]

#random.shuffle(vaccines)
#print(vaccines)

lucky = random.choice(vaccines)
print(lucky)

for vac in vaccines:
    print(f"Testing vaccines {vac}")
    if vac == lucky:
        print(f"{lucky} vaccine test successful")
        break
    print(f"{vac} testing failed")