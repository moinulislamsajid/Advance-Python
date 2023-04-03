from multiprocessing.resource_sharer import stop
from timeit import default_timer as timer
from tracemalloc import start
my_list = ['a'] * 6
print(my_list)

# bad 
start = timer()
my_string = ""
for i in my_list:
    my_list+=i
stop = timer()
print(stop - start)


#good
start = timer()
my_string = ''.join(my_list)  # this is a  best function join this is called to the and remember this term
stop = timer()
print(stop - start)

# formating systle
var = "sajid" # when use integer we use %d when use float we use %f 
locall = "My Variable is %s" % var
print(locall)
# formatig systle
var1 = 202020
var2 = 6
my_string = f"this is {var1} and this is {var2}"
print(my_string)
