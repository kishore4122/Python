import random
def time_activity(*args, **kwargs):
    #print(args)
    #print(kwargs)

    min = sum(args) + random.randint(0, 100)
    #print(min)

    select = random.choice(list(kwargs.keys()))
    #print(select)
    print(f"you have to spend {min} for {kwargs[select]}")


time_activity(10, 20, 30, hobby="Dance", fun="cycling", work="Devops")  