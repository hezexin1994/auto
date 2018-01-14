#11测试代码
    #测试函数
"""name_function.py"""
def get_formated_name(first,last):
    """Generate a neatly formated full name."""
    full_name=first+' '+last
    return full_name.title()

"""names.py"""
from name_function import get_formated_name
print("Enter 'q' at any time to quit.")
while True:
    first=input("\nPlease give me a first name: ")
    if first=='q':
        break
    last=input("Please give me a last name: ")
    if last=='q':
        break
formated_name=get_formated_name(first,last)
print("/tNeatly formatted name: "+formatted_name+'.')

    #单元测试
"""test_name_function.py"""
import unittest
from name_function import get_formated_name
class NamesTestCase(unittest.TestCsae):
    """测试name.function.py"""
    def test_first_last_name(self):
        """能够正确处理像Janis Joplin这样的姓名吗？"""
        formatted_name=get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
unittest.main()
    #不能通过的测试

    #添加新测试
import unittest
from name_function import get_formated_name
class NamesTestCase(unittest.TestCsae):
"""测试name_function.py"""
    def test_first_last_name(self):
      """能够正确地处理像Janis Joplin这样的姓名吗？"""
        formatted_name=get formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
    def test_first_last_middle_name(self):
      """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name=get formatted_name(
            'wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')  
unittest.main()


   #测试类
       #unittest Module中的断言方法
         #assertEqual(a,b)  核实a==b
         #assertNotEqual(a,b)  核实a!=b
         #assertTrue(x)  核实x为True
         #assertFalse(x)  核实x为False
         #assertIn(item,list)  核实item在list中
         #assertNotIn(item,list)  核实item不在list中
"""survey.py"""
class AnonymousSurvey():
    """收集匿名调查问卷的答案"""
    def __init__(self,question):
        """储存一个问题，并为储存答案做准备"""
        self.question=question
        self.responses=[]
    def show_question(self):
        """显示调查问卷"""
        print(self.question)
    def store_response(self,new_response):
        """储存单份调查答卷"""
        self.responses.append(new_response)
    def show_results(self):
        """显示收集到的所有答卷"""
        print("Survey results:")
        for response in self.responses:
            print('- '+response)

"""language_survey.py"""   
from survey import AnonymousSurvey
  #定义一个问题，并创建一个表示调查的AnonymousSurvey对象
question="What language did you first learn to speak?"
my_survey=AnonymousSurvey(question)
  #显示问题并储存答案
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response =='q':
        break
    my_survey.store_response(response)
  #显示调查结果
print("\nThank you  to everyone who participated in the survey.")
my_survey.show_results()

###AnonymousSurvey类可用于简单的匿名调查

    #测试AnonymousSurvey类：如果用户面对调查问题时只提供了一个答案，这个答案
#也能被妥善储存。

"""test_survey.py"""
import unittest
from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
"""针对AnonymousSurvey类的测试"""
def test_store_single_response(self):
    """测试单个答案会被妥善地储存"""
    question="What language did you first learn to speak?"
    my_survey=AnonymousSurvey(question)
    my_survey.store_response('English')
    self.assertIn('English',my_survey.responses)
uittest,main()

"""提供三个答案时也能被妥善储存"""
import unittest
from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
"""针对AnonymousSurvey类的测试"""
def test_store_single_response(self):
    """测试单个答案会被妥善地储存"""
    question="What language did you first learn to speak?"
    my_survey=AnonymousSurvey(question)
    my_survey.store_response('English')
    self.assertIn('English',my_survey.responses)
def test_store_three_response(self):
    """测试三个答案会被妥善地储存"""
    question="What language did you first learn to speak?"
    my_survey=AnonymousSurvey(question)
    responses=['English','Spanish','Mandarin']
    for response in responses:
        my_survey.store_response(response)
    for response in responses:
    self.assertIn(response,my_survey.responses)   
uittest,main()

  #方法setUp()
import unittest
from survey import AnonymousSurvey
class TestAnonymousSurvey(unittest.TestCase):
"""针对AnonymousSurvey类的测试"""
      def setUp(self):
          """创建一个调查对象和一组答案，供使用的测试方法使用"""
           question="What language did you first learn to speak?"
           self.my_survey=AnonymousSurvey(question)
           self.responses=['English','Spanish','Mandarin']
      def test_store_single_response(self):
          """测试单个答案会被妥善的储存"""
          self.my_survey.store_response(self.response[0])
          self.assertIn(self.response[0],self.my_survey.responses)
      def test_store_three_response(self):
         """测试三个答案会被妥善地储存"""
          for response in responses:
              self.my_survey.store_response(response)
          for response in responses:
              self.assertIn(response,my_survey.responses)   
uittest,main()
 








































































































































































































































































































































































































































