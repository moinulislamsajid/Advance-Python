# Dictionary is collection of data type
# unorder to muteable
# Dictionary Decalar to {} and this is keyword base i mean bd menas Bangladesh and printed thr domain bd
# this is collection of key word



mydict = {
    
    "name":"Ayman Sajid",
    "Father_name" : "Mujibur Rahman",
    "Mother_name" : "Rebeka Akter",
    "Brother_name" : "Samiur Rahman Sakib",
    "Village" : "Goalpara"

    }
# dictonary ar jonno print and add ar jonno [] ai breaket use kortah hoi
mydict.popitem()
mydict["phone"] = 183912076   # add the value of dictonaries
print(mydict["Father_name"])
print(mydict["Mother_name"])
print(mydict["name"])
print(mydict["Brother_name"])
print(mydict["phone"])

for key in mydict:  # when use to key world print so use to key word
    print(key)
mydict_cpy = mydict  # this is for copy
print(mydict)

#local = dict("Name":"sajid","age":"20","Raligion":"islam")

mylook= {"name": "max","age" :20,"email":"sajid@gmail.com"}
mylook_2 = dict(name = "mary",age = 25, city = "Boston")
print(mylook_2)

my_tuple = (2,4,5,6)  # this is tuples
local ={my_tuple: 30} # this add dictonary function
print(local)


class Dictonary:
    def hey_dic(self):
        return  {"name" : "Ayman Sajid","Roll" : 20, "religion" : "Islam"}

       
               



people = Dictonary()
hey = people.hey_dic()
print(hey["name"])
print(hey["Roll"])
print(hey["religion"])