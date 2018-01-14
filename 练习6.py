#6使用词典
  #简单的词典
alien_0={'color':'green','points':5}
  #访问词典中的值
new_points=alien_0['points']#键要用方括号括起来
print('You just earned '+str(new_points)+' points!')
  #添加键-值对
alien_0={'color':'green','points':5}
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
  #先创建一个空字典 
alien_1={}
alien_1['color']='yellow'
alien_1['points']=20
print(alien_1)
  #修改字典中的值
print('This alien is '+alien_1['color']+'.')
alien_1['color']='red'
print('This alien is now  '+alien_1['color']+'.')

alien_1={'x_position':0,'y_position':25,'speed':'fast'}
print("Original x_position:"+str(alien_1['x_position']))
if alien_1['speed']=='slow':#向右移动外星人
    x_increament=1
elif alien_1['speed']=='medium':
     x_increament=2
else:
    x_increament=3
alien_1['x_position']=alien_1['x_position']+ x_increament#新位置坐标
print("New x_position: "+str(alien_1['x_position']))
  #删除键-值对
del alien_0['points']#永远删除
  #由类似对象组成的字典
favorite_language={
    'he zexin':'Chinese',
    'wan wanting':'English',
    'zhang yuqing':'japanese',
    'wang yan':'korean',#在最后一行也添加逗号，为以后添加新值做准备
    }
print("He Zexin's favorite language is "+  #在每行的末尾添加运算符
    favorite_language['he zexin'].title()+ #每行前面可以用Tab键缩进
    ".")
  #遍历字典
messages={
    'first_name':'he',
    'last_name':'zexin',
    'age':23,
    'city':'beijing',
    }
for key,value in messages.items():#可以用两个变量来储存键和值
    print("\nKey: "+key)
    print("Value: "+str(value))

favorite_language={
    'he zexin':'Chinese',
    'wan wanting':'English',
    'zhang yuqing':'japanese',
    'wang yan':'korean',
    }
for name,language in favorite_language.items():
    print(name.title()+"'s favorite language is "+
          language.title()+".")
    #遍历字典中的键 keys()
favorite_language={
    'he zexin':'Chinese',
    'wan wanting':'English',
    'zhang yuqing':'japanese',
    'wang yan':'korean',
    }    
for name in favorite_language.keys():
    print(name.title()+
    #或者可以写成：
#for name in favorite_language:#遍历字典时默认遍历所有的键
    #print(name.title()+)
    
favorite_language={
    'he zexin':'Chinese',
    'wan wanting':'English',
    'zhang yuqing':'japanese',
    'wang yan':'korean',
    }  
  if 'jen' not in favorite_language.keys():
        print("Jen,please take our poll!")
    

favorite_language={
    'he zexin':'Chinese',
    'wan wanting':'English',
    'zhang yuqing':'japanese',
    'wang yan':'korean',
    }  
friends=['zhang yuqing','wan wanting']
for name in favorite_language.keys():
    print(name.title())
    if name in friends:
        print("Hi,"+name.title()+
              ",I know your favorite laguage is "+
              favorite_language[name].title()+".")
     #按顺序遍历字典中的所有键
favorite_language={
    'he zexin':'Chinese',
    'wan wanting':'English',
    'zhang yuqing':'japanese',
    'wang yan':'korean',
    }
for name in sorted(favorite_language.keys()):
    print(name.title())         

  #遍历字典中的所有值 values()
favorite_language={
    'he zexin':'Chinese',
    'wan wanting':'English',
    'zhang yuqing':'japanese',
    'wang yan':'korean',
    }          
for language in favorite_language.values():
           print(language.title())
    #为剔除重复值，可使用集合（set），集合类似于列表，但每个元素都是独一无二的
for language in set(favorite_language.values()):
           print(language.title())          

  #嵌套
      #字典列表
aliens=[]
for alien_number in range(30):
          new_alien={'color':'green','points':5,'speed':'slow'}
          aliens.append( new_alien)
for alien in aliens[:5]:
          print(alien)
print('...')


aliens=[]
for alien_number in range(30):
          new_alien={'color':'green','points':5,'speed':'slow'}
          aliens.append( new_alien)
for alien in aliens[0:3]:#修改前三个外星人的信息
          if alien['color']=='green':
          alien['color']='yellow'
          alien['speed']='medium'
          alien['points']=10
for alien in aliens[:5]:
          print(alien)
print('...')          

  
      #在字典中储存列表（每当需要在字典中将一个键关联到
                           #多个值时，都可以在字典中嵌套一个列表）
favorite_languages={
    'he zexin':['Chinese','korean'],
    'wan wanting':['English'],
    'zhang yuqing':['japanese','English'],
    'wang yan':['korean'],
    }
for name,languages in favorite_languages.items():
    if len(languages)==1:
      print("\n"+name.title()+"'s favorite language is:")
            for language in languages:
              print("\t"+language.title())
    else:
          print("\n"+name.title()+"'s favorite language are:")
            for language in languages:
              print("\t"+language.title())       
         
      #在字典中储存字典
cities={
    'beijing':{
        'population':90,
        'country':'China',
        'area':100,
        }
    'seoul':{
        'population':30,
        'country':'China',
        'area':40,
        }
    'tokyo':{
        'population':70,
        'country':'China',
        'area':80,
        }
    }
for city,city_info in cities.items():
          print('\n'+city.title()+'is in '+city_info['country']+
                'with '+str(city_info['population'])+' people'+
                'and the area of this city is about '+str(city_info['area'])+'.')




















