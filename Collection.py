# Collection Modules

# 5 differnt collection of collection of modulos
# it also provide counter, namedtuple, OrderedDict, defaultdict,deque


from ctypes import pointer
from typing import Counter


a = "aaaaaabbbbbcccccddddddd"
first_counter = Counter(a)  # counter is import keyword this function use to how many time is called the modules
print(first_counter.items())
print(first_counter.keys())
#print(first_counter.elements())


# nametuple
from collections import namedtuple
point = namedtuple('point', 'x,y')
pt = point(1,-4)
print(pt)
print(pt.x,pt.y)

from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['b'])
print(d['v'])

from collections import deque
d = deque()
d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.extendleft([4,5,6])  # extend 2 ti list ak satha kora
print(d)
d.rotate(-1)
print(d)
