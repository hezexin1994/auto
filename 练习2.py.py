#2.3.1修改字母大小写
name='he zexin'
print(name.title())
print(name.upper())
print(name.lower())
#2.3.2合并字符串
first_name='he'
last_name='zexin'
full_name=first_name+''+last_name
print('Hello,'+full_name.title()+'!')
#2.3.3制表符和换行符
print("'本学期课程：'\n\t‘劳动经济学’\n\t'专业英语'\n\t'社会保险基金'")
print("本学期课程：\n\t劳动经济学\n\t专业英语\n\t社会保险基金")
#2.3.4 删除空白
favorite_language='  python  '
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()

message='Hello HeZexin,would you like to learn some Python today?'
print(message)
author='albert einstein'
famous='"A person who never made a mistake never tried anything new."'
print (author.title()+' '+'once said,'+famous)
person1='wan wanting'
person2='wang yan'
person3='zhang yuqing'
print("\n\t 'person1'\n\t'person2'\n\t'person3'")
#2.4数字
age=23
message='Zexin,happy'+' '+str(age)+'rd Birthday!'
print(message)
print(3+5)
print(1*8)
print(16-8)
print(8/1)
number=5
say='My lucky number is'
print(say+' '+str(number)+'!')
#2.5注释
print("hello python world!")
