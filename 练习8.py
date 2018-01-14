#8函数
  #定义函数
def greet_user(username):
  """显示问候语"""
  print('Hello, '+username.title()+'!')
greet_user('he zexin')
        #username:形参；'he zexin'：实参。
def display_message(knowledge):
    print('I lern '+knowledge +' in this category.')
display_message('function')

  #传递实参
def describe_pet(animal_type,animal_name):
    print('\nI have a '+animal_type+',and '+animal_name.title()+' is her name.')
describe_pet('hamster','jike')
describe_pet('original','moudi')

      #关键字实参
      #还可以写成  describe_pet(animal_typ='original',animal_name='moudi')
      #或者写成    describe_pet(animal_name='moudi'，animal_type='original')
      #直接写时顺序很重要，按照关键字写时顺序没有影响

      #默认值
def describe_pet(animal_name,animal_type='dog'):
    print('\nI have a '+animal_type+',and '+animal_name.title()+' is her name.')
    #一条叫jike的小狗
describe_pet('jike')
    #或者describe_pet(animal_name='jike')
    #一只叫moudi的猫
describe_pet(animal_type='cat',animal_name='moudi')
#注意：将 animal_type设置成默认值后要放在后面，因为系统默认这个实参为位置实参     

    #返回值
def get_formatted_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return full_name.title()
musician=get_formatted_name('he','zexin')
print(musician)
    #让实参变成可选的
def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:  #python将非空字符串解读为True，相当于if middle_name==True
        full_name=first_name+' '+middle_name+' '+last_name
    else:
        full_name=first_name+' '+last_name
    return full_name.title()
musician1=get_formatted_name('he','zexin')
print(musician1)
musician2=get_formatted_name('he','xin','ze')
print(musician2)
    #返回字典
def build_person(fist_name,last_name):
    person={'first':first_name,'last':last_name}
    return person
musician3=build_person('jimi','hendrix')
print(musician3)

def build_person(first_name,last_name,age=''):
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age
    return person
musician4=build_person('jimi','hendrix',age=23)
print(musician4)
musician5=build_person('jimi','hendrix')
print(musician5)

    #结合使用函数和while循环
def get_formatted_name(first_name,last_name):
    full_name=first_name+' '+last_name
    return full_name.title()
while True:
    print('/nWrite down your name:')
    f_name=input('First_name：')
    if f_name=='q'
      break
    l_name=input('Last_name:')
    if l_name=='q'
      break
    formatted_name=get_formatted_name(f_name,l_name)
    print("\nHello, "+ formatted_name+'!')
    #练习
def city_country(city,country):
  full=city.title()+' , '+country.title()
  return full
first=city_country('beijing','china')
print(first)

def make_album(name,album_art,songs=''):
  if songs:
    message=name.title()+"'s new album art is a "+album_art+",with "+str(songs)+" songs."
  else:
    message=name.title()+"'s new album art is a "+album_art+"."
  return message
one=make_album('he zexin','cat',89)
print(one)

def make_album(name,album_art,songs=''):
  message=name.title()+"'s new album art is a "+album_art+",with "+str(songs)+" songs."
  return message
while True:
    print("Write down your message:")
    print("(enter 'q' at any time to quit)")
    singer=input("Name: ")
    if singer=="q":
      break
    art=input("Your album art: ")
    if art=="q":
      break
    print("You just finished registing. ")

  #传递列表
    #在函数中修改列表
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]
while unprinted_designs:
  current_design=unprinted_designs.pop()
  print("Printing model: "+ current_design)
  completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
  print(completed_model)

    #用函数形式重新编写：
def printed_designs(unprinted_designs,completed_models):
  while unprinted_designs:
    current_design=unprinted_designs.pop()
    print("Printing model: "+ current_design)
    completed_models.append(current_design)
def show_completed_models(completed_model):
  print("\nThe following models have been printed:")
    for completed_model in completed_models:
      print(completed_model)
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]
printed_designs(unprinted_designs,completed_models)
show_completed_models(completed_models)

  #禁止函数修改列表
def printed_designs(unprinted_designs,completed_models):
  while unprinted_designs:
    current_design=unprinted_designs.pop()
    print("Printing model: "+ current_design)
    completed_models.append(current_design)
def show_completed_models(completed_model):
  print("\nThe following models have been printed:")
  for completed_model in completed_models:
    print(completed_model)
unprinted_designs=['iphone case','robot pendant','dodecahedron']
completed_models=[]
printed_designs(unprinted_designs[:],completed_models)#让原列表中的信息保留
show_completed_models(completed_models)
print(unprinted_designs)

  #练习
def show_magicians(magicians):
  print("\nThe magicians list : ")
  for magician in magicians:
    print(magician.title())
magicians=['he zexin','zhang yuqing','wang yan','wan wanting']  
show_magicians(magicians)

def make_great(magicians):
   print("\nThe magicians list : ")
   for magician in magicians:
      print("the Great "+magician.title())
magicians=['he zexin','zhang yuqing','wang yan','wan wanting']  
make_great(magicians[:])
print(magicians)

  #任意数量的实参
def make_pizza(*toppings):
# * 创建一个名为topping的空元组，并将收到的所有值都封装到这个元组中
  print("\nMaking a pizza with follow topppings:")
  for topping in toppings:
    print("-"+topping)
make_pizza('pepperoni')
make_pizza('mushroom','green peppers')

  #结合使用位置实参和任意数量实参
    #要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量的实参的形参放在最后
def make_pizza(size,*toppings):
  print("\nMaking a "+str(size)+"-inch pizza with follow topppings:")
  for topping in toppings:
      print("-"+topping)
make_pizza(12,'pepperoni')
make_pizza(9,'mushroom','green peppers')  

  #使用任意数量的关键字实参
def build_profile(fist,last,**user_info):
  #两个*代表创建一个空字典
  profile={}
  profile['first_name']=first
  profile['last_name']=last
  for key,value in user_info.items():
    profile[key]=value
  return profile
user_profile=build_profile('albert','einstein',
                           location='princeton',
                           field='physics')
print(user_profile)

#练习
def sandwich(*materials):
  print("Your sandwich includes these materials: ")
  for material in materials:
    print("-"+material.title())
sandwich('onion','chicken')
  
def car(manufacturer,type,**info):
  information={}
  information['manu']=manufacturer
  information['model']=type
  for key,value in info.items():
    information[key]=value
  return information
user_info=car('Volkswagen','suv',
                color='yellow',
                paret='light')
print(user_info)

  #将函数储存在模块中
    #导入整个模块
    #在pizza.py文件中写以下程序
def make_pizza(size,*toppings):
  print("\nMaking a "+str(size)+"-inch pizza with follow topppings:")
  for topping in toppings:
      print("-"+topping)
    #重新创建一个名为making_pizzas.py的文件
import pizza  #打开文件pizza.py
pizza.make_pizza(12,'pepperoni')
pizza.make_pizza(9,'mushroom','green peppers')  
 
    #导入特定的函数
#from moduel_name import function_name
#from moduel_name import function_0,function_1,function_2
#示例
from pizza import make_pizza
make_pizza(12,'pepperoni')
make_pizza(9,'mushroom','green peppers')  

  #使用as给函数指定别名
  #如果要导入的函数的名称与现有的相冲突，或者名称太长，可用as指定一个名称
#from moduel_name import function_name as fn
from pizza import make_pizza as mp #将函数make_pizza()重命名为mp()
make_pizza(12,'pepperoni')
make_pizza(9,'mushroom','green peppers')  

  #使用as给模块指定别名
  #import module_name as mn
import pizza as p
p.make_pizza(12,'pepperoni')
p.make_pizza(9,'mushroom','green peppers') 

  #导入模块中的所有函数
#使用*可以导入模块中的所有函数，
###使用并非自己编写的大型模块时最好不要用这种方法，名称可能会出现重复
#form module_name import*
from pizza import *  #将模块pizza中的所有函数都复制到这个程序文件中
make_pizza(12,'pepperoni')
make_pizza(9,'mushroom','green peppers')






























