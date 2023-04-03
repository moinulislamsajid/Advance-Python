# sets is collection of data type
# set is a unordered ,mutable,no duplicates
# it just like a dicttionary but it have no keyword but it has single value and and evevry time it declar and shows it commma 

from operator import add


my_sets = {1,2,2,2,4,5,5,3,4,5} #sets means jaisob value aca seisoba ar common gula jaba i mean 1 ar besi kono value repeat korla value tah akbar ei count korba that it
print(my_sets)
# sets does not allot duplicates
len_set = set("Ayman Sajid")  # this key word or function use to indivuadial charcter printout function name is set
print(len_set)

empty_set = {}  # when called the empty set than he use to dictionary
print(type(empty_set))

empty_set1 = set() # this is set type
print(type(empty_set1))

add_value = set()
add_value.add(1)
add_value.add(2)
add_value.add(3)
add_value.add(4)
add_value.remove(4)
#add_value.remove(5)  # this key error
if 5 in add_value:
    print("Yes")

else:
    print("NO")


# union and intersection

# union
odds = {1,3,5,7,9}
even = {2,4,6,8}
prime = {2,3,5,7}

u = odds.union(even)   # union means sob common value but duplicates value neaba nah
print(u)

d = odds.intersection(even) # this function is called common thing for two sets 
print(d)


c = even.intersection(prime)
print(c)

setq = {2,3,4,5,6,7,8,9}
sete = {2,3,4,12,13,14,15}


local = sete.difference(setq)
print(local)

setv = {2,3,4,5,6,7,8,9}
setn = {2,3,4,12,13,14,15}

foll = setv.symmetric_difference(setn) # jaigula common seigula bad jaba 
print(foll)


sett = {2,3,4,5,6,7,8,9}
sety = {2,3,4,12,13,14,15}
koi = sety.difference_update(sett)
print(koi)

seta = {2,3,4,5,6,7,8,9}
seteb = {2,3,4,12,13,14,15}
goal = seteb.issuperset(seta)
print(goal)


copy_1 = {1,2,3,4,5,6,7,8}
copy_2 = copy_1

copy_1.add(70)
print(copy_1)
print(copy_2)

people = frozenset([1,2,3,4,5])  # thia value can not be changed it is almost fixed
                                 # any kind of opearation are error

print(people)
