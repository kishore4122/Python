# class is like an object constructor
# all classes have a __init__() function
# __init__() is executed automatically whenever we create the objects from this class 

# "self" Parameter
# self is a reference to the current instance of the class
# is used to access variables that belong to the class


class User:
    def __init__(self, user_email, user_name, user_password, user_current_job_title):
        self.email = user_email
        self.name = user_name
        self.password = user_password
        self.current_job_title = user_current_job_title

    def change_password(self, new_password):
        self.password = new_password
    
    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently working as {self.current_job_title}. You can contact them at {self.email}")


