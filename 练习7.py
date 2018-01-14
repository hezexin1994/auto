#7用户输入和while循环
  #函数input()的工作原理
name=input("Please enter your name:")
print("Hello, "+name+" !")
    #input()让程序暂停运行，等待用户输入一些文本
  #创建多行字符串
prompt='If you tell us who you are,we can personalize the messages you see.'
prompt+='\nWhat is your name? '# +=表示在上一行prompt的后面再加一个字符串
name=input(prompt)  #input后面的（）表示将+前面的字符加在什么位置
print("Hello, "+name+" !")

  #使用int()来获取数值输入
age=input('How old are you? ')
age=int(age)
if age>18:
    print('You can have an ID-card.')
else:
    print('\nYou can not have an ID-card yet.')
  #求模运算符
number=input("Write down the number you choice,"+
             "and I'll tell you if it's even or odd: ")
number=int(number)
if number%2==0:#余数为0则为偶数，不为0则为奇数
    print("\n The number "+str(number)+" is even.")
else:
    print("\n The number "+str(number)+" is odd.")

#while循环简介
current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1  #current_number=current_number+1的简写

   #让用户选择何时退出
prompt="\nTell me something,and I will repeat it back to you: "
prompt+="\nEnter 'quit' to the end the program . "
message=""
while message!='quit':
    message=input(prompt)
    if message!='quit':
        print(message)
    
  #使用标志 让程序更整洁
prompt="\nTell me something,and I will repeat it back to you: "
prompt+="\nEnter 'quit' to the end the program . "
active=True
while active:
    message=input(prompt)
    if message=='quit':
        active=False
    else:
        print(message)

  #使用break退出循环
prompt="\nPlease enter the city you have visited: "
prompt+="\nEnter 'quit' when you are finished . "
while True:
    city=input(prompt)
    if city=='quit':
        break   #在任何循环中都可以使用break语句。
    else:
           print("I'd love to go to "+city.title()+"!")
           
  #在循环中使用continue
     #返回到循环开头，并根据条件测试结果决定是否继续执行循环
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

  #避免无限循环：使用Ctrl+C或者关闭窗口

  #使用while循环来处理列表和字典
    #在列表间移动元素
unconfirmed_users=['he zexin','wan wanting','zhang yuqing','wang yan']
confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print("Verifying user:"+current_user.title())
    confirmed_users.append(current_user)
print('\nThese users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

  #删除包含特定值的所有列表元素
pets=['pig','dog','cats','elephent']
print(pets)
while 'elephent'in pets:
    pets.remove('elephent')
print(pets)

  #使用用户输入来填充字典
responses={}
polling_active=True #设置一个标志，指出调查是否继续
while polling_active：
  name=input("\nWhat's your name?")
  response=input("Which mountain would you like to climb someday?")
  responses[name]=response  #等号左边是name对应的当前值
  repeat=input("Would you like to let another person respond?(yes/no)")
  if repeat=='no':
      polling_active=False
print("\n---Poll Results---")
for name,response in responses.items():
    print(name+"would you like to climb "+response+".")


sandwich_orders=['beef','fruit','cheese','original']
finished_sandwiches=[]
for sandwich in sandwich_orders:
    print('I made your '+sandwich.title()+'.')
while sandwich_orders:
    finished_sandwich=sandwich_orders.pop()
    finished_sandwiches.append(finished_sandwich)
print('The list of finished sandwiches:'+str(finished_sandwiches))


































