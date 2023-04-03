# generators is local function
# this is simple function
# this is use simple function type


from re import A


def mygenerators():
    yield 1
    yield 2
    yield 3
  

local = mygenerators()
for lol in local:
    print(lol)

def fristion(n):
    nums =[]
    num = 0
    while num<n:
        nums.append(num)
        num+=1
    return nums
print(fristion(10))



def local_number(x):
    count = []
    cout = 0
    while cout<x:
        count.append(cout)
        cout+=1
    return count
print(sum(local_number(20)))
print((local_number(10)))
print((local_number(30)))
print((local_number(5)))


# fibonacci serius
def fibonacci(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b, a+b
fib = fibonacci(30)
for item in fib:
    print(item)