#print('hello,world','new','health')
# name = input('please input you name:')
#print('hello,',name)
#print('1024 * 768 =',1024*768) 
'''
a = 100
if a >=0:
    print(a)
else:
    print(-a)
'''
#print('''line1line2line3''')
print('hello')
'''
print(ord('李'))

print(chr(45789))

classmates = ['nana','noro','molia']
classmates.append('ama')
classmates.insert(2,'bomb')
classmates.pop()
print(classmates)

roommates=(4,5,6)
'''
'''
s = input('birth:')
birth = int(s)
if birth < 1990:
    print("90前1")
elif birth > 2000:
    print("00后")
else:
    print("你在输出啥")
'''
#print(list(range(8)))
'''
L = ['a','b','c']
for l in L :
    print("hello" + l)
    '''
'''
n1 = 255
n2 = 1000
print(hex(n1),hex(n2))

from ab import my_abs
print(my_abs(-99))
'''
'''
def add_end(L=[]):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end([1,2,3]))
print(add_end())
print(add_end())
print(add_end([1,2,3]))
print(add_end([1,2,3]))
print(add_end())
'''
'''
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2,3,4))
'''
'''
def person(name,age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)

print(person('silery', 24, city='Beijing', addr='Chaoyang', zipcode=123456))
'''
'''
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)

print(f1(1,2)    )
print(f1(1,2,c=3))
print(f1(1,2,3,'a','b'))
print(f1(1,2,3,'a','b',x=99))
print(f2(1,2,d=99,ext=None))
'''
'''
def fact(n):
    return fact_iter(n,1)

def fact_iter(num,prodect):
    if num == 1 :
        return prodect
    return fact_iter(num - 1,num * prodect)

print(fact_iter(5,5))
'''
'''
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L)
'''
'''
L = list(range(100))
print(L[:10])
'''
'''
def trim(s):
    if 0 ==len(s):
        return s

    while ' ' ==s[0]:
        s = s[1:]
        if 0 == len(s):
            return s

    while ' ' ==s[-1]:
        s=s[:-1]
        if 0 ==len(s):
            return s
    return s

print(trim(' hello hi '))
'''
'''
def findMinAndMax(L):
    if len(L)==0:
        return (None,None)
    min = L[0]
    max = L[0]
    for num in L:
        if num < min:
            min = num
        if num > max:
            max = num
    return (min,max)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
'''
'''
import os
print([d for d in os.listdir('.')])
print(isinstance(18,int))

'''
'''
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

b = fib(6)
#print(next(b))
#for n in b:
#    print(n)

while True:
    try:
        x = next(b)
        print('b:',x)
    except StopIteration as e:
        print('Generator retuen value:',e.value)
        break

'''
def normalize(name):
    name = name[0].upper()+name[1:].lower()
    return name
L1 = ['ada','lla','fafde']
L2 = list(map(normalize,L1))
print(L2)

from functools import reduce
def prod(L):
    return reduce(lambda x,y: x*y,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
'''
DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2float(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,map(char2num,s.replace(".","")))
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
'''
def str2float(s):
   def fn(x, y):
        return x * 10 + y
   def char2num(s):
         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
   return reduce(fn, map(char2num, s.replace(".","")))
s="1234.567"
if s.find(".")!=-1:
     print('str2float(\'%s\') ='%s, str2float(s)/pow(10,(len(s)-s.find(".")-1)))
else:
     print('str2float(\'%s\') ='%s, str2float(s))
