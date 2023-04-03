
#from secrets import randbelow

# for password and secorty purpose to use (secrets)

# only 3/' function has secrests

import secrets
from threading import local

'''pass_word = secrets.randbelow(5)
print(pass_word)
# this ranbelow item is 10 is very secrets 
'''

local_pass = secrets.randbits(15)
print(local_pass)


people_local = secrets.randbits(5)
print(people_local)

my_list = list("FHDFHIDFHAI")
doc = secrets.choice(my_list)
print(doc)