# String : ordered,imutable,text representation
first_string = "Hello World!"
print(first_string)
sec_string = "I'm a Progrmmmer"
print(sec_string)
sec_string = 'I\'m a Software_Engineer'
print(sec_string)


# 3 double qutaction used to multiline string and use to docamanction
mul_string = """Bangladeesh
is 
a 
wonderful
country
it 
is 
has
many
river
"""

#print(mul_string)
print(mul_string)
print("Hello World")

my_fistr = "Ayman Sajid"
localf = my_fistr[::-1]  # when riverge the string than use to [::-1]
print(localf)

speace_string = "        Ayman sajid      "
speace_string = speace_string.strip()   # strip() function use to control white speace # when use to remove the speace
print(speace_string)


ano_list = ['a'] *7
print(ano_list)
my_string = ""
for i in ano_list:
    my_string+=i
print(my_string)

# alternative

local_string = "".join(ano_list)
print(local_string)