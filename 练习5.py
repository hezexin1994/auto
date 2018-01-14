#if语句
  #条件测试，检查是否相等
car='audi'
# car='bmw'
  #条件测试，检查是否不等，有时候效率更高
requested_topping='mushroom'
if requested_topping != 'anchovies':
    print('Hold the anchovies!')
  #检查多个条件是否同时成立and or
age_0=80
age_1=20
age_0>=30 and age_1<=20
age_0<50 or age_1>30
  #检查特定值是否包含在列表中
requested_topping=['mushroom','onions','pineapple']
'mushroom' in requested_topping
mine='salt'
if mine not in requested_topping:
    print(mine.title()+' '+'is not possible. ')
  #布尔表达式，布尔值常用于记录条件
game_active=True
can_edit=False
#练习
car='subaru'
print("Is car=='subaru'?I predict True.")
print(car=='subaru')
submit='SUV'
choice='suv'
print(choice==submit.lower())
weather=['sun','rain','wind','typhoon']
today='sun'
if today in weather:
    print('What a lovely day!')
tomorrow='snow'
if tomorrow not in weather:
    print("I do not know the weather.")

#if语句
  #if-else语句:执行两个操作中的一个
weather=['sun','rain','wind','typhoon']
if today=='sun':    
    print('What a lovely day!')
else:
    print("I do not like the weather.")
  #if-elif-else：执行多个条件，只能满足其中一个
age=38
if age<=4:
    price=0
elif age<18:#4岁以上，18以下的收费￥5
    price=5
else:
    price=10
print("Your admission cost is ￥"+str(price)+'.')
    #或者用elif取代else
age=38
if age<=4:
    price=0
elif age<18:#4岁以上，18以下的收费￥5
    price=5
elif age>=18:
    price=10
print("Your admission cost is ￥"+str(price)+'.')
  #如果想同时测试多个独立的条件，需要用一系列独立的if语句
  #练习
alien_color=['green','yellow','red']
player1='green'
if player1 in alien_color:
    print('coin=5')

if 'green'in alien_color:
    print('coin=5')
elif 'yellow'in alien_color:
    print('coin=10')
else:
    print('coin=15')

age=65
if age < 2:#在比较符号的左右最好各有一个空格
    print('He is a baby.')
elif age < 4:
    print('He is learning how to walk.')
elif age < 13:
    print('He is a child.')
elif age < 20:
    print('He is a tennager.')
elif age < 65:
    print('He is a men')
else:
    print('He is an older.')
    
  #检查特殊元素
requested_toppings=['mushroom','onions','pineapple']
for requested_topping in requested_toppings:
    print('Adding '+requested_topping+'.')
    #把点了的材料添加到披萨配料中
print('\nFinished making your pizza.')
    #如果蘑菇用完了
requested_toppings=['mushroom','onions','pineapple']
for requested_topping in requested_toppings:
    if requested_topping=='mushroom':
        print('Sorry,we are out of mushroom right now.')
    else:
        print('Adding '+requested_topping+'.')
print('\nFinished making your pizza!')
  #检查列表不是空的
requested_toppings=[]
if requested_toppings:
    for requested_topping in requested_toppings:
        print('Adding '+requested_topping+'.')
    print('\nFinished making your pizza!')
else:
    print('Are you sure you want a plain pizza?')
  #使用多个列表
available_toppings=['mushroom','olives','green peppers','pepperoni'
                    ,'pineapple','extra cheese']#店里有的配料
requested_toppings=['mushroom','french fries','extra cheese']#客人点的
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print('Adding '+requested_topping+'.')
    else:
        print("Sorry,we don't have "+requested_topping+'.')
print('\nFinished making your pizza!')
#练习
lists=['he zexin','wan wanting','zhang yuqing','wang yan','admin']
for name in lists:
  if name=='admin':
     print('Hello '+name.title()+',would you like to see a status report?')
  else:
      print('Hello '+name.title()+','+'thank you for your logging in again.' )


current_users=['mike','juedy','john','marry','jessica']
new_users=['Jessica','kindy','crystal','krystal','eve']
for new_user in new_users:
    if new_user.lower() in current_users:
        print('Sorry,you need change a name.')
    else:
        print('You name '+new_user.title()+' is OK.')

numbers=['1','2','3','4','5','6','7','8','9']
for number in numbers:
    if number=='1':
        print(str(number)+'st')
    elif number=='2':
        print(str(number)+'nd')
    elif number=='3':
        print(str(number)+'rd')
    else:
        print(str(number)+'th')


print('Hello World!')



    
