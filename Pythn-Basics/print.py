name = "sars_cov_2"
disease = "Covid 19"

print("The name of the virus is", name) 
print("The name of the virus is", name + " " + "The name of disease is", disease)

print("The name of the virus is" + " " + name)

#using format

print("The name of the virus is {}".format(name))
print("{} virus causes the {} disease".format(name, disease))
print(f"{name} virus cause the {disease} disease")