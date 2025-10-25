# class Car:
#     def __init__(userbrand, usermodel):
#         brand = userbrand
#         model = usermodel


# car1 = Car("Toyota", "Corolla")
# print(car1)  # it will print the address of the object created

class Memo:
    def __init__(self, usname, date):
        # usname =  self.my_name this is wrog we cant use parameter on left side
        self.my_name = usname  # correct way to assign parameter to instance variable
        self.hellodate = date
        # date = self.hellodate
Memo_obj = Memo("Meeting", "2024-06-15")
print(Memo_obj)  # it will print the address of the object created
print(Memo_obj.my_name)  # it will print "Meeting"
# print(car1.brand)  # This will raise an error since brand is not defined as an instance variable

print(Memo_obj.hellodate)  # it will print "2024-06-15"
