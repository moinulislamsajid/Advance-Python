# decorators with argument

'''import functools

def local_people(num_times):
    def local_area(func):
        @functools.wraps(func)
        def local_upzilla(*args,**kwargs):
            for _  in range(num_times):
                result = func(*args,**kwargs)
            return result
        return local_upzilla
    return local_area


@local_people(num_times=3)
def people_name(name):
    print(f"Hello {name}")

people_print = people_name("sajid")
print(people_print)
people_name("Ayman Sajid")
'''
import functools
def people(num_peo):
    def people_area(func):
        @functools.wraps(func)
        def people_location(*args,**kwargs):
            for _ in range(num_peo):
                res = func(*args,**kwargs)
            return res
        return people_location
    return people_area


@people(num_peo=5)
def people_print(name):
    print(f"Hello {name}")

people_print("Dhaka International University")

    
              