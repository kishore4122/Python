DevOps = ["Jenkins", "Ansible", "Bash", "Puppet", "Kubernetes", "Terraform"]
Development = ("Nodejs", "Angular", ".net", "python")
cntr_emp1 = {"Name":"kishore", "Skill":"BlockChain", "Code":1234}
cntr_emp2 = {"Name":"chandra", "Skill":"BootStrap", "Code":12345}

usr_skill = input("Enter your Desired skill:")

if usr_skill in DevOps:
    print(f"we have {usr_skill} in DevOps team")
elif usr_skill in Development:
    print(f"We have {usr_skill} in Development Team")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print(f"we have a contract employee  with {usr_skill} this skill")
else:
    print("Skill is not found")