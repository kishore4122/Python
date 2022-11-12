import requests

response = requests.get("https://gitlab.com/api/v4/users/kishore4122/projects")
my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}\nProject URL is: {project['web_url']}\n")

#print(response.json())  This will give output in List format
#print(type(response.json()))
#print(response.json()[0]) 

#print(response.text)  This will give you output in String format
#print(type(response.text))