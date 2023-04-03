
'''from random import randint

for i in range(10):
    guess_number = int(input("Enter a nummber(1-10) : "))
    random_number = randint(1,10)  # when the input prefer to computer and give a operator than use to (randint)
    if guess_number == random_number:
       print("You have won")

    else:
       print("you have lost")
       print("Answer is : ",random_number)
'''

import random
a = random.random()  # random number to floot number this is random 
                     # this range to 0 to 1
                     # always given to floot number

print(a)


b = random.uniform(1,5)  # this is another float it is range to 1 to 5 # this is give to float number
print(b)

# when give an integer to random number
c = random.randint(1,5)  # this is keyword give a integer random number
print(c)


# another keyword

d = random.randrange(1,10) # this is another keyword to an integer randis number
print(d)

# normal varible
e = random.normalvariate(0,1)
print(e)

mylist = [1,2,4,5]
local = list(map(lambda x : x*2,mylist))
print(local)

my_list_1 = list("ABCDEFGHIJKLMNOPQRSTWXYZ")  # this is print to induvidual character
print(my_list_1)  
a = random.choice(my_list_1)  # random choice to use random character to print character
print(a)


local_list = list("ABCDEFGIJK")
x = random.sample(local_list , 3) # this is count indivual number to print i mean  koto digit random character korba tai hoba
print(x)



people_tuples = list("KFKDFDFHIFANFSFDFKAL")
u = random.sample(people_tuples, 2)
print(u)


local_list = ["FJFHFJFH"]
random.shuffle(local_list)
print(local_list)
