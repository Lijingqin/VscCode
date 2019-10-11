'''
class Student(object):
    _slots_ = ('name','age')
'''

'''
class Student(object):

    def get_score(self):
        return self.get_score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an.integer!')
        if value<0 or value>100:
            raise ValueError('score must between 0~100!')
        self._score = value
'''
'''
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2019 - self._birth

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @width.getter
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @height.getter
    def height(self):
        return self._height

    @property 
    def resolution(self): 
        return self._width*self._height     

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')



class Student(object):
     def __init__(self, name):
         self.name = name
     def __str__(self):
         return 'Student object (name: %s)' % self.name

print(Student('Michael'))
'''
'''
from enum import Enum

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name,'=>',member,',',member.value)

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1)

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')

'''
'''
fpath = r'C:\Windows\system.ini'

with open(fpath,'r') as f:
    s = f.read()
    print(s)

'''
'''
from io import BytesIO
f= BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
'''

#序列化
'''
import pickle
d = dict(name = 'Bob', age = 20, score=88)
pickle.dumps(d)

f = open('dump.txt','wb')
pickle.dump(d,f)
f.close()
print(d)
'''

import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(std):
        return {
          'name': std.name,
          'age': std.age,
           'score': std.score
        }    

s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)