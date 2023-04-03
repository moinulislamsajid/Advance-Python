#lamda argument expression
from turtle import position


add_10 = lambda z: z*10  # this is lamda function first lamda than input : and expression , varibale name

print(add_10(10))

position2d = {(1,2),(15,1),(5,-1),(10,4)}
position2d_sorted = sorted(position2d, key=lambda x: x[1])
print(position2d)
print(position2d_sorted)

# map
a = [2,3,4,5,6]
b = list(map(lambda x: x*3,a))  # list a convert kortah hoba
print(b)

c = [t*2 for t in a]  # list compaharrsion
print(c)

d = [v*3 for v in a]
print(d)

# filtar
c = [1,2,3,4,5,6,7,8]
v = list(filter(lambda q : q%2==0,c))
print(v)

# this item list comperassion
d = [w for w in a if w%2==0]   # this a  is  varibale name important
print(d)

#again 
e = [s for s in c if s%2==0]
print(e)
# again
h = [t for t in c if t%2==0]
print(h)

# reduce
from functools import reduce

didt = [1,2,3,4,5,6]
# reduce always work on two function

pip = reduce(lambda d,f:d+f,didt) # reduce always 2 function neya kaj kora
print(pip)


local = [43,54,65,65,78,98]
hey = reduce(lambda j,k : j+k,local)
print(hey)