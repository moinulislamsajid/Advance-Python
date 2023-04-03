# itertools modules collection of tules

# itertools
# product,peramutations,combinations,accumulate,groupby, and infinte iterators

#itertools work on list tuples and dictonary

from itertools import product
from platform import libc_ver
a = [1,2]
b = [3]
prod = product(a,b, repeat=2)
print(list(prod))


#permutations
from itertools import permutations
d = [1,2,3]
perum_oddring = permutations(d) # differant oddering for use permutations
print(list(perum_oddring))


#combinations


from itertools import combinations # joto dornar combination kora jai tai hoba thats it
f = [1,2,3]
fall = combinations(f,2)   # this 2 is observr to length and this is mentatory
print(list(fall))


from itertools import combinations_with_replacement

j = [2,3,4,5,6]
lol = combinations_with_replacement(j,2)  # all comination are replce 
print(list(lol))


#accumulate
from itertools import accumulate
s = [1,2,3,4,5]
accum = accumulate(s)  # default complite the sum
print(list(accum))

#accumlate with multiple
from itertools import accumulate 
import operator
z = [1,2,3,4]
goa = accumulate(z,func=operator.mul)
print(z)
print(list(goa))

#groupby
from itertools import groupby

#infinate iterators

from itertools import count,cycle,repeat

# count
for i in count(10):
    if i == 15:
        break
    print(i)


#cycle

f = [1,2,3,4,5]
for cy in cycle(f):
    if cy == 4:
        break
    print(cy)


#repeat

w = [1,2,3,4,5]
for re in repeat(w):
    print(re)


