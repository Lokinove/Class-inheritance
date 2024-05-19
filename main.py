# class Rectangle:
#   def __init__(self, width, height):
#     self.width = width
#     self.height = height
#   def description(self):
#     return f"The Height : {self.height} and The Width : {self.width}"
#   def area(self):
#     return self.width * self.height
#   def change_width(self, width):
#     self.width = width
#     return self.width
# rectangle1 = Rectangle(7, 5)
# print(rectangle1.description())
# print("The area is ", rectangle1.area())
# rectangle1.change_width(4)
# print(rectangle1.description())
# print("The area is ", rectangle1.area())

class Vehicle(): #parent
  def __init__(self,type, engine, tyres, capacity):
    self.type = type
    self.engine = engine
    self.tyres = tyres
    self.capacity = capacity

class Car(Vehicle): #child
  def __init__(self, type, engine, tyres, capacity, brand):
    super().__init__(type, engine, tyres, capacity)
    self.brand = brand

class Airplane(Vehicle): #child
  def __init__(self, type, engine, tyres, capacity, brand, wings):
    super().__init__(type, engine, tyres, capacity)
    self.brand = brand
    self.wings = wings

  def airplane_info(self):
    return(f"Info :{self.brand} - {self.type} - {self.engine} - {self.tyres} - {self.capacity}")

  def change_engine(self):
    self.engine = "General Dynamics"

  def change_all_values(self, brand, type, engine, capacity):
    self.brand = brand
    self.type = type
    self.engine = engine
    self.capacity = capacity


# Boeing737 = Airplane("Airliner", "General Motors", 13, 300, "Boeing", 2)
# nissanconvertible370z = Car("Sedan", "electric engine", 4, 5, "Nissan")

# print(Airplane.airplane_info(Boeing737))
# Airplane.change_engine(Boeing737)
# print(Airplane.airplane_info(Boeing737))

# input_brand = input("Enter the new brand : ")
# input_type = input("Enter the new type : ")
# input_engine = input("Enter the new engine : ")
# input_capacity = input("Enter the new capacity : ")
# Airplane.change_all_values(Boeing737,input_brand,input_type,input_engine,input_capacity)

#Boeing737.self.engine = input_engine)
# print(Airplane.airplane_info(Boeing737))
flag_error = True

# while flag_error:
#   try:
#     number = int(input("Input an integer : "))
#     print((number), "Code Run Succesfully")
#     flag_error = False
#   except ValueError:
#     print("Invalid Input")


while flag_error:
  try:
    number = int(input("Input a number to be divided by 2 : "))
    print((number/2), "Code Run Succesfully")
    flag_error = False
  except ZeroDivisionError:
    print("Please input non zero")
  except ValueError:
    print("Invalid Input")

list = [1, 2, 3, 4, 5]
try:
  for i in range(6):
    print(list[i])
except IndexError:
  print("Index out of range")


