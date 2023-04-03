"""
1.Differnt between argument and parameter'
2.Positional and keyword argument
3.varibale Length argument

"""

# what is positional argument 
# when argument is 1,2,3,5 this is called is positional argument

def positional_and_keyword(a,b,c):
    print(a,b,c)


positional_and_keyword(a=4,b=5,c=8)  # this is keyword argument


def dekhi_kih_hoi(a,b,*args,**kwargs): # this args is * args and ** kwargs are any name to set the name not to fixed name any name to use
    # * args means any are all positional argument to use
    # ** kwarges means all keyword argument to use
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key]) # always remember dict are [] braket




loka_kih_bola = dekhi_kih_hoi(1,2,3,4,5,6,five = 5,six = 6,seven = 7)


# keyword argument

def foo(*args,last): 
    for arg in args:
        print(arg)
    print(last)


foo(1,last=5) # when we declar paratmeter any variable than called to keyword argument

def allah_vorsha(a,b,c):
    print(a,b,c)


my_list = (1,2,3)
allah_vorsha(*my_list)
