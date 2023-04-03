# first a list create squire breaket
# list allot int and bollen and string and dupclicate elimate or copy element


list1111 = ["Dhaka","Faridpur","Gazipur"]
print(list1111)

mylist = [list()]
print(mylist)

long = [0]  * 5
print(long)

long1 = [1,2,3,4,5,6,7,8,9]
bz = long1[0:6]
print(bz)

org_list = ["banana","Apple","Orange","Mango"]
#list_cpy = org_list[:]
#list_cpy = list(org_list)
#list_cpy = org_list.copy()
list_cpy = org_list[:]
list_cpy.append("lemon")
print(list_cpy)
print(org_list)