#3列表简介
#3-1
#3.1构建列表并访问列表元素
friends=['wan wanting','wang yan','zhang yuqing']
print(friends[0].title())
print(friends[1].title())
print(friends[-1].title())
print(friends[0].title()+':'+'grandpa')
print(friends[1].title()+':'+'father')
print(friends[-1].title()+':'+'brother')
#3.2修改、添加和删除元素
sushe327=['wan wanting','wang yan','zhuang zheng']
print(sushe327)
sushe327[-1]='zhang yuqing'
print(sushe327)
#在列表末尾添加元素
sushe327.append('zhuang zheng')
print(sushe327)
#在列表中任意位置插入元素
sushe327.insert(-1,'guan lijing')
print(sushe327)
#删除已知位置的元素，永久删除
del sushe327[-2]
print(sushe327)
#使用方法pop()删除列表末尾元素，删除后可以使用它的值
popped_sushe327=sushe327.pop()
print (sushe327)
print(popped_sushe327)
#弹出任意位置的元素
sushe327.append('zhuang zheng')
sushe327.insert(-1,'guan lijing')
person1=sushe327.pop(-1)
print('My friend' +':'+person1+'.')
#删除已知值的元素，删除后也可以接着使用它的值
person2='guan lijing'
sushe327.remove(person2)
print(sushe327)
print('\nREASON:'+'guan lijing'.title()+' '+'is just my friend but not my rommate'+'.')
#练习
list=['jin meng','wang pan','liu xuece','wang jian']
print(list)
list.remove('wang jian')
print(list)
print ('\nReason:'+'wang jian'.title()+' '+'is out of my world'+'.')
list.append('liu qi')
print(list)
print('\nI just found a big table!')
list.insert(0,'wan wanting')
list.insert(3,'wang yan')
list.insert(-1,'zhang yuqing')
print(list)
print('\nI am so sorry for that only two person can be invivted.')
boy1=list.pop(-1)
print(list)
print('\n'+boy1.title()+':'+'I am so sorry.')
boy2=list.pop()
print('\n'+boy2.title()+':'+'I am so sorry.')
boy3=list.pop()
print('\n'+boy3.title()+':'+'I am so sorry.')
boy4=list.pop()
print('\n'+boy4.title()+':'+'I am so sorry.')
boy5=list.pop()
print('\n'+boy5.title()+':'+'I am so sorry.')
print(list)
del list[0]
print(list)
del list[0]
print(list)
#组织列表
#按照字母顺利排序，永久性修改排列顺序
list=['jin meng','wang pan','liu xuece','wang jian']
list.sort()
print(list)
#按照反字母顺利排序，永久性修改排列顺序
list=['jin meng','wang pan','liu xuece','wang jian']
list.sort(reverse=True)
print(list)
#使用函数对列表进行临时排序
list=['jin meng','wang pan','liu xuece','wang jian']
print('Here is the original list:')
print(list)
print('Here is the sorted list:')
print(sorted(list))
print(sorted(list,reverse=True))
#倒序打印列表
list=['jin meng','wang pan','liu xuece','wang jian']
print(list)
list.reverse()
print(list)
#确定列表的长度
list=['jin meng','wang pan','liu xuece','wang jian']
len(list)
#练习
place=['Budapest','Greece','Austria','Korea','Turkey','NK']
print(place)
print(sorted(place))
print(sorted(place,reverse=True))
print(place)
print(sorted(place,reverse=True))









