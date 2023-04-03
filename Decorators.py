# Decorators is one of the best tools in python tools
# every python developer known the Decorators tools

# there are 2 differnt decorators 
# such as
# function decorators
# class decorators

# function decorators
#decorators use korar somay @ use kortah hoi



def start_and_decorator(func):

        def wrapper():
            print("Start")
            func()
            print("End")
        return wrapper
@start_and_decorator     # this is function decorator   
def print_name():
    print("Alex")
@start_and_decorator
def local_name():
    print("Bangladesh")
@start_and_decorator
def university_name():
    print("Dhaka International university")

'''print_name = start_and_decorator(print_name)
local_name = start_and_decorator(local_name)
DIU = start_and_decorator(university_name)'''
# uporar privotra function decortor use kortah hoi hoba
print_name()
local_name()
university_name()

def local_people_local(func):
    def legend(*args,**kwargs):
        print('start')
        result = func(*args,**kwargs)
        return result
        print('end')
    return legend

@local_people_local
def hey_bro(y):
    return y+10


result = hey_bro(5)
print(result)
print(hey_bro.__name__)