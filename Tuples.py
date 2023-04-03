# this is declar to () karli braket
# tuples value cannotne changed
mytuple = ("Bangladesh",2020,"Dhaka")
print(mytuple)

hey = ("Bangladesh",)  # when use one element or one argument to tuples at last to observe (,)
print(hey)

local = ("Faridpur",7800,"Domrakandi")
people = local[1:]
print(people)


variable = ["Sajid","Sakib","Ayon","Hasib","Senthu","Nazmulq"]
for item in variable:
    if item == "Nazmul":
        break
    elif item == "Sajid":
        continue
    print(item)

world_class = ("Leion Messi","Pele","Maradona")
if "Leion Messi" in world_class:
    print("World No 1 best and hones player")

else:
    print("World No 1 best and hones player")

kop =('a','b','a','c','d','e','f','g','a')
hurrah = len(kop)
print(hurrah)
print(kop.count('a'))
print(kop.index('a'))
print(kop.index('f'))

num = (1,2,3,4,5,6,7,8,9)
wants = num[::-1]
print(wants)