'''
def is_palindrome(n):
    str_n = str(n)
    turn_n = str_n [::-1]
    if str_n == turn_n :
        return n

print(is_palindrome(3))
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
'''
'''
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)

L2 = list(filter(lambda x: x%2 == 1,range(1,20))) 
print('2:',L2)
'''

'''
import re

print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))

re.match(r'^\d{3}\-\d{3,8}$', '010 12345')

re_email = re.compile(r'^[\w]+\.?[\w]+@[\w]+\.com$')

def is_valid_email(addr):
    if re_email.match(addr):
        return True

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

re_name_of_email = re.compile(r'^<?([\w]+\s*[\w]*)>?\s*[\w]*@[\w]+\.org$')
# 正则解释             <一个或无 字母一个以上 空格不限 字母不限 >一个或无 @ 字母一个以上 .org
def name_of_email(addr):
    if re_name_of_email.match(addr):
        return re_name_of_email.match(addr).group(1)

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
'''

'''
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }

def print_score(std):
    print('%s: %s' % (std['name'], std['score']))

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
'''
'''
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        self.__gender = gender

bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

'''
'''
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
dog.run()

cat = Cat()
cat.run()

'''

'''
class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        self.__set_count()
 
    def __set_count(self):
        Student.count += 1
 
if Student.count != 0:
    print('测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student.count)
'''