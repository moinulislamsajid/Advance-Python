
f = open("local.txt","rt")
print(f.readline())
print(f.readline())
print(f.readline())

f.close()
g = open("sajid","w")
print(g.write("Hey i am Ayman Sajid"))
g.close()