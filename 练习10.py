#10文件和异常
  #从文件中读数据
    #读取整个文件
"""pi_digits.txt"""
3.1415926535
  8979323846
  2643383279
"""file_reader.py"""
with open('pi_digits.txt')as file_object:
    contents=file_object.read()
    print(contents.rstrip())
"""read()到达文件末尾时会返回一个空字符串，显示出来就是一个空行，
所以用rstrip()来删除字符串末尾的空白"""

    #文件路径：打开不在程序文件所属目录中的文件
"""文件夹text_file位于文件夹python_work中，要打开的文件位于文件夹text_file中"""
"""相对路径"""
with open('text_file\filename.txt')as file_object:
"""绝对路径"""
file_path='C:Users\ehmatthes\other_files\text_file\filename.txt'  
with open(file_path)as file_object:

    #逐行读取
"""file_reader.py"""
filename='pi_digits.txt'
"""使用文件时的常用做法"""
with open(filename)as file_object:
    for line in file_object:
        print(line.rstrip())

    #创建一个包含文件各行内容的列表
filename='pi_digits.txt'
"""使用文件时的常用做法"""
with open(filename)as file_object:
    lines=file_object.readlines()
"""readlines()从文件中读取每一行并将其储存在一个列表中"""
    for line in lines:
        print(line.rstrip())

    #使用文件内容
"""pi_string.py"""
filename='pi_digits.txt'
with open(filename)as file_object:
    lines=file_object.readlines()
pi_string = ''
    for line in lines:
        pi_string+=line.strip()
print(pi_string)
print(len(pi_tring))

    #包含一百万位的大型文件：命令没有任何变化

  #写入文件
"""write_message.py"""
filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.")
"""打开文件时，可以指定读取模式('r')，写入模式('w')，附加模式('a'),
读取和写入的模式('r+')，如果省略了模式参考，Python将以默认的只读模式
打开文件。要将数值数据储存到文本文件中，必须先使用str()将其转换成字符串格式。"""
     #写入多行
filename='programming.txt'
with open(filename,'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
     #附加文件
"""write_message.py"""
filename='programming.txt'
with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

  #异常
    #处理ZeroDivisionError异常    
"""division.py"""
print(5/0)
"""除以0会出现错误，改为："""
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero.")
"""try-except代码块，当try中的代码能正常运行时，跳过except"""

    #使用异常避免崩溃
"""创建一个只执行除法运算的简单计算器"""
print("Give me two numbers ,and I'll")
print("Enter 'q' to quit.")

while True:
    first_number = input ("\nFirst number: ")
    if first_number=='q'
    break
    second_number = input("Second number: ")
    if second_number=='q'
    break
    answer=int(first_number)/int(second_number)
    print(answer)
    """如果除数为0则崩溃"""

    #else代码块：将可能引起错误的代码放在try-except代码块中，
    #可提高这个程序抵御错误的能力
print("Give me two numbers ,and I'll")
print("Enter 'q' to quit.")

while True:
    first_number = input ("\nFirst number: ")
    if first_number=='q'
    break
    second_number = input("Second number: ")
    try:
    answer=int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0.")
    else:
    print(answer)    
    
    #处理FileNotFoundError异常：找不到要打开的文件
"""没有将文件alice.txt储存在alice.py中"""
filename = 'alice.txt'
with open(filename)as f_obj:
    contents = f_obj.read()
    """python无法读取不存在的文件"""
"""修正"""
filename = 'alice.txt'
try:
with open(filename)as f_obj:
    contents = f_obj.read()
except FileNotFoundError:
    msg='Sorry,the file '+filename +' does not exist.'
    print(msg)

    #分析文本
    title="Alice in Wonderland"
    title.split()
    """以空格为分隔符，将字符串拆分"""

filename='alice.txt'
try:
  with open(filename)as f_obj:
            contents=f_obj.read()
except FileNotFoundError:
        msg='Sorry,the file '+filename +' does not exist.'
    print(msg)
else:
        #计算文件大致包含多少个单词
words=contents.split()
num_words=len(words)
print("The file "+filename+" has about "+str(num_words)+" words.")

    #使用多个文件
def count_words(filename):
        """计算一个文件大致包含多少个单词"""
    try:
        with open(filename)as f_obj:
                contents=f_obj.read()
    except FileNotFoundError:
           msg='Sorry,the file '+filename +' does not exist.'
           print(msg)
    else:
        #计算文件大致包含多少个单词
        words=contents.split()
        num_words=len(words)
        print("The file "+filename+" has about "+str(num_words)+" words.")

filename='alice.txt'
count_words(filename)

    #失败时一声不吭
def count_words(filename):
        """计算一个文件大致包含多少个单词"""
    try:
        with open(filename)as f_obj:
                contents=f_obj.read()
    except FileNotFoundError:
           pass
    else:
        #计算文件大致包含多少个单词
        words=contents.split()
        num_words=len(words)
        print("The file "+filename+" has about "+str(num_words)+" words.")

filename='alice.txt'
count_words(filename)

     #储存数据
        #使用json.dump()和json.load()
imput json
number=[2,3,5,7,11,13]
filename='numbers.json'
with open(filename,'w')as f_obj:
    json.dump(numbers,f_obj)

        #使用json.load()将这个列表读取到内存中
imput json
filename='numbers.json'
with open(filename,'w')as f_obj:
   numbers=json.load(f_obj)
print(numbers)

      #保存和读取用户生成的数据
imput json
username=input("What is your name?")
filename='username.json'
with open(filename,'w')as f_obj:
   json.dump(username,f_obj)
print("We'll remember you when you come back, "+username+"!")


imput json
#如果以前储存了用户名，就加载他
#否则，就提示用户输入用户名并储存他

filename='username.json'
try:
  with open(filename,'w') as f_obj:
      username=json.load(f_obj)
except FileNotFoundError:
    username=input("What is your name?")
    with open(filename,'w')as f_obj:
       json.dump(username,f_obj)
       print("We'll remember you when you come back, "+username+"!")
else:
    print("Welcome back, "+username+"!")

    #重构
imput json
def greet_user():
    """问候用户，并指出其名字"""
    filename='username.json'
    try:
        with open(filename)as f_obj:
            username=json.load(f_obj)
        except FileNotFoundError:
            username=input("What is your name?")
        with open(filename,'w')as f_obj:
           json.dump(username,f_obj)
           print("We'll remember you when you come back, "+username+"!")
    else:
        print("Welcome back, "+username+"!")
greet_user()


imput json
def greet_user():
    """如果储存了用户名，就获取它"""
    filename='username.json'
    try:
        with open(filename)as f_obj:
            username=json.load(f_obj)
        except FileNotFoundError:
            return None
        else:
            return username
def greet_user():
    """问候用户，并指出其名字""""
    username=get_stored_username()
    if username:
        print("Welcome back, "+username+"!")
    else:
        username=input("What's your name?")
        filename='username.json'
        with open(filename,'w')as f_obj:
            json.dump(username,f_obj)
            print("We'll remember you when you coma back, "+username+"!")
greet_user()
            





























































































































































