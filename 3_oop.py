class Car:
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel
        self.a = userbrand
        self.b = usermodel
    
    def full_name(self):
        return self.brand + self.model
    
obj = Car(1, 2) 
print(obj)  # it will print the address of the object created
print(obj.full_name())  # it will print 3
# class Car:
#     def __init__(userbrand, usermodel):
#         brand = userbrand
#         model = usermodel
# car1 = Car("Toyota", "Corolla")
# print(car1)  # it will print the address of the object created
