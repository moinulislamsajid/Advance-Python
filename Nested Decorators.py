
class countCalls:
    def __init__(self,func):
        self.func = func
        self.num_calls = 0

    def __call__(self,*args,**kwargs):
        #result = func(*args,**kwargs)
        #print("Location There")
        self.num_calls+=1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)


'''cc = countCalls(None)
cc()'''
@countCalls
def print_say():
    print("This is a local area")


print_say()
print_say()





    
        
