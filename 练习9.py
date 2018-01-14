#9类
#根据类创建实例
class Dog():
    """类的第一个字母要大写"""
    def __init__(self,name,age):
        """init前后有两条下划线"""
        self.name=name
        self.age=age
        """self是必须设定的，通过self访问的变量称为属性"""
        """只用形参self定义两种方法sit和roll_over"""
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title()+' is mow sitting.')
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title()+' rolled over!')
my_dog=Dog('willie',6)
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+".")
my_dog.sit()
my_dog.roll_voer()
"""注意函数的调用方法"""
your_dog=Dog('lucy',2)
print("Your dog's name is "+your_dog.name.title()+".")
print("Your dog is "+str(your_dog.age)+".")
your_dog.sit()

#练习
class Restaurant():
    def __init__(self,name,cuisine):
      self.name=name
      self.cuisine=cuisine
    def describe_restaurant(self):
        print("I have a restaurant named "+self.name.title()+".")
    def open_restaurant(self):
        print("Our cuisine type is "+self.cuisine+".")
my_restaurant=Restaurant('goodsoup','france')
print("My restaurant named "+my_restaurant.name.title()+".")
print("My restaurant's cuisine type is  "+my_restaurant.cuisine.title()+".")
susz_restaurant=Restaurant('goodsoup','france')
print("Susz's restaurant named "+my_restaurant.name.title()+".")
print("Susz's restaurant's cuisine type is  "+my_restaurant.cuisine.title()+".")

  #使用类和实例
class Car():
    def __init__(self,make,model,year):
      self.make=make
      self.model=model
      self.year=year
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

    #给属性制定默认值
class Car():
    def __init__(self,make,model,year):
      self.make=make
      self.model=model
      self.year=year
      self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

  #修改属性的值
    #直接修改属性的值
class Car():
    def __init__(self,make,model,year):
      self.make=make
      self.model=model
      self.year=year
      self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=23
my_new_car.read_odometer()

    #通过方法修改属性的值
class Car():
    def __init__(self,make,model,year):
      self.make=make
      self.model=model
      self.year=year
      self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()  
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()

    #通过方法对属性的值进行递增
class Car():
    def __init__(self,make,model,year):
      self.make=make
      self.model=model
      self.year=year
      self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()  
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
         self.odometer_reading+=miles
my_used_car=Car('audi','a4',2016)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()   
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

  #继承：一个类（子类）需要继承另一个类（父类）
     #先写父类
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+"miles on it.")
    def update_odometer(self,mileage):
        if mileage>= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
class ElectricCar(Car):
    def __init__(self,make,model,year):
        """初始化父类属性"""
        super().__init__(make,model,year)
        """特殊函数，将父类和子类关联起来"""
my_tesla=ElectricCar('tesla','model s','2016')
print(my_tesla.get_descriptive_name())      
      

    #给子类定义属性和方法
class Car():
    --snip--
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size=70
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kwh battery")
my_tesla=ElectricCar('tesla','model s','2016')
print(my_tesla.get_descriptive_name())       
my_tesla.describe_battery()

    #重写父类的方法
#对于父类的方法，只要它不合符子类模拟的实物的行为，都可以进行重写。假设Car类
#有一个名为fill_gas_tank()的方法，它对全电动汽车来说毫无意义，需要重写：
class ElectricCar(Car):
    --snip--
     gas_tank=0
    def fill_gas_tank(self):
        """电动车没有油箱"""
        print("This car don't need a gas tank!")
my_tesla=ElectricCar('tesla','model s','2016')
print(my_tesla.get_descriptive_name())      
my_tesla.describe_battery()
my_tesla.battery.fill_gas_tank()

    #将实例用作属性
#在给类添加细节时会发现越加越多，可以把需要的类的一部分作为一个独立的类提取出来
#将大型类拆分成协同工作的小类
class Car():
  --snip--
class Battery():
    """定义一个新类，没有任何继承"""
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe_battery(self):
      print("This car has a "+str(self.battery_size)+"-kwh battery.")
class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
my_tesla=ElectricCar('tesla','model s','year')
print(my_tesla.get_descriptive_name())    
my_tesla.battery.describe_battery()

class Car():
  --snip--
class Battery():
  --snip--   
    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270
        message="This car can go approximately "+str(range)
        message+= "miles on a full charge."
        print(message)
class ElectricCar(Car):        
  --snip--
my_tesla=ElectricCar('tesla','model s','year')
print(my_tesla.get_descriptive_name())    
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

  #导入类
"""一个可用于表示汽车的类"""
"""存为文件car.py"""
class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+"miles on it.")
    def update_odometer(self,mileage):
        if mileage>= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles
"""存为文件my_car.py"""
from car import Car
my_new_car=Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=23
my_new_car.read_odometer()

  #在一个模块中储存多个类
class Car():
  --snip--
class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kwh battery.")
     def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270
        message="This car can go approximately "+str(range)
        message+= "miles on a full charge."
        print(message)
class ElectricCar(Car):  
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery=Battery()
"""新建一个名为my_electric_car.py的文件，导入ElectricCar类"""
from car import ElectricCar
my_tesla=ElectricCar('tesla','model s',2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery..get_range()

  #从一个模块中导入多个类:用逗号分隔
"""创建一个文件名为my_car.py,将Car和Battery类都导入"""
from car import Car,ElectricCar
my_battery=Car('volkswagen','beetle',2016)
print(my_battery.get_descriptive_name())
my_tesla=ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())

  #导入整个模块
"""创建一个文件名为my_car.py，导入整个car模块"""
import car
my_battery=Car('volkswagen','beetle',2016)
print(my_battery.get_descriptive_name())
my_tesla=ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())

  #导入模块中的所有类
from module_name import *
"""不建议使用这个方法，最好导入整个模块，
并使用module_name.class_name语法来访问类"""

  #在一个模块中导入另一个模块
"""将Car类储存在一个模块中，并将ElectricCar和Battery类储存在另一个模块中，
将第二个模块命名为electric_car.py"""
"""electric_car.py"""
from car import Car
class Battery():
    --snip--
class ElectricCar(Car):
    --snip--
"""car.py"""
class Car():
    --snip--
"""可以分别从每个模块中导入类"""
"""my_car.py"""
from car import Car
from electric_car import ElectricCar
my_battery=Car('volkswagen','beetle',2016)
print(my_battery.get_descriptive_name())
my_tesla=ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())
































































































































