# *args

def add(*args):
    res =0
    for i in args:
        res+=i
    print(res)

add(2,3,4,5,6)


# **kwargs - Key word args
def calc(**kwargs):
    print(kwargs)

calc(add=True,num =5) # {'add': True, 'num': 5} (type dictionary)

class Car():
    def __init__(self, **kw) :
        self.make = kw.get('make') #get returns None if key not in dictionary
        self.model = kw.get('model')

car = Car(make = 'alto')
print(car.model,car.make)
