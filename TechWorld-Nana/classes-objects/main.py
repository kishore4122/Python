from user import User
from post import Post

app_user_one = User("kishore@gmail.com", "kishore", "strongpassword", "Devops Engineer")
app_user_one.get_user_info()

app_user_two = User("chandra@gmail.com", "chandra", "PasswOrd", "Devops")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()