## Basic Slicing
'''
planet = "Closest planet to sun"

print(planet)
print(planet[0])
print(planet[1])
print(planet[-1])
print(planet[:7])
print(planet[:-4])
print(planet[-3:])
print(planet[8:14])
print(planet[-13:-7])

# Slicing a string, get a substring from a string
planet = "Closest planet to sun"

print(planet[:7])
print(planet[:7][:5])
print(planet[:7][:5][-1])


# Tuples Slicing
devops = ("Linux", "Vagrant", "Bash", "AWS", "Jenkins", "Python")

print(devops)
print(devops[:4])
print(devops[:-1])
print(devops[-1])
print(devops[-1][0:4])


# List Slicing
devops = ["Linux", "Vagrant", "Bash", "AWS", "Jenkins", "Python"]
print(devops)
print(devops[:4])

'''
# Dictonary Slicing
skills = {"DevOps":("Aws", "Jenkins", "Ansible"), "Development" : ["Nodejs", "HTML", "Bootstrap", ".net"]}

"""print(skills)"""
print(skills["DevOps"])
print(skills["Development"])

print(skills["DevOps"][2])
print(skills["DevOps"][2][:3])
print(skills["DevOps"][2][:3][-1])
