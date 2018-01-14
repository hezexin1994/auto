#4循环语句——遍历整个列表
sushe327=['he zexin','wan wanting','zhang yuqing','wang yan']
for rommate in sushe327:#下面的每一行缩进命令都会执行循环
 print(rommate.title())#需要缩进一个字符
 print('I love you forever, '+rommate.title()+'.\n')
print('That is my honour to have all of you!')#没有缩进，只执行一次

#练习
animals=['dog','cat','tortoise','hourse']
for animal in animals:
    print('I like '+' '+animal)
    print('A'+' '+animal+' '+'can be hard to suport.'+'\n')
print('But,any of these animals would be a great pet!')

#函数range生成一系列数字
for vaule in range(1,36):
    print(vaule)
#将上一步的数字变成列表
numbers=list(range(1,36))
print(numbers)
#只打印偶数
even_numbers=list(range(2,38,2))
print(even_numbers)

#使用函数range()可以创建任何需要的数字集，1-10的平方
squares=[]#生成一个空列表
for value in range(1,11):
    squares.append(value**2)#生成1-10，平方后逐个加到列表末尾
print(squares)
   #第二种办法，复杂一点但是更清晰
squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)#生成1-10，平方后逐个加到列表末尾
print(squares)

#简单的统计计算
numbers=list(range(1,36))
min(numbers)
max(numbers)
sum(numbers)

#创建列表解析
squares=[value**2 for value in range(1,11)]
print(squares)

#练习
for geshu in range(1,21):
    print(geshu)
geshubiao=list(range(1,21))
print(geshubiao)
sum(geshubiao)
lists=[value**3 for value in range(1,11)]
print(lists)

#使用表的一部分
  #切片
cute=['cat','dog','pig','elephent','tortoise','hourse']
print(cute[0:3])
print(cute[:4])#如果没有第一个索引，将从头开始
print(cute[2:])#从第三个开始
print(cute[-3:])#最后三个
cute=['cat','dog','pig','elephent','tortoise','hourse']
print('Here are my favorite animals:')
for animal in cute[:2]:
    print(animal.title())
  #复制列表：包含整个列表的切片[:]
my_food=['pizza','bread','cake']
jinmeng_food=my_food[:]
print('My favorite foods are:')
print(my_food)
print('Jing Meng favorite foods are:')
print(jinmeng_food)
my_food.append('ice-cream')
jinmeng_food.insert(0,'apple')
print('My favorite foods are:')
print(my_food)
print('Jing Meng favorite foods are:')
print(jinmeng_food)

  #元组：创建一些不可修改的列表
dimensions=(200,50)
print(dimessions[0])
print(dimessions[1])
dimensions[0]=250#修改信息,不成功
#或者写成
dimensions=(200,50)
for dimension in dimensions:
    print(dimension)
  #不能修改元组，但是可以重新定义
dimensions=(200,50)
print('Original dimensions')
for dimension in dimensions:
    print(dimension)

dimensions=(400,100)
print('\nModified dimensions')
for dimension in dimensions:
    print(dimension)



