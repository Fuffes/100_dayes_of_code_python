def add(*args):
    return sum(args)


sum_test = add(1,2,3,4)
print(sum_test)



def calculate(**kwargs):
    return kwargs["add"]
print(calculate(add = 5))



class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")



my_car = Car( model="m5")
print(my_car.make)