

# *args and **kwargs

# *args = postional arguments spasifecly, 
# **kwargs = keyword arguments

def func1(arg1, arg2, arg3):
    print(arg1, arg2, arg3)


def func2(arg1 = None, arg2= None, arg3= None):
    print(arg1, arg2, arg3)

args = [1, 2, 3]
kwargs = {"arg2": 2, "arg1": 1, "arg3": 3}




func1(args[0], args[1], args[2])

# *args wil do is unpack this and split this into individual items = 1, 2, 3 like that
func1(*args)
print(args)

func2(*kwargs)




