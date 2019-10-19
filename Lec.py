# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 19:28:20 2019

@author: 薛
"""

#%%
print('hello, world')

#%%输入与输出
print(100 + 200)
print('aaa''bbb')
print('aaa','bbb')
print('aaa',end = '');print('bbb')
#%%
name = input('please enter your name: ')
print('hello,', name)
#%%
print('100 + 200 =',300)
print('100 + 200 =', 300)
print('100 + 200 = ',300)
print(f'100 + 200 = {300}')


#%%数据类型
#%%整数
#整数间的精确除法与科学计数法
print('%.2f'%(1/3))
print(1.2e-1)
#各种除法
print(9/3)
print(10//3)
print(10%3)

#%%字符串
#转义字符与引号&字符串
print('I\'m "OK"')
print('I\'m \"OK\"')
print('I\'m\nOK')
print('\\\n\\')
print(r'\\\n\\')

#python换行输出与特殊的字符串
str1='''
line1
line2
line3'''
print(str1)

print('line1\nline2\nline3')

#%%布尔值
5 > 3 and 3 < 1
True and False

5 > 3 or 3 < 1
True or False

not 1 > 2
not False

#%%空值
None


#%%变量
a = 'ABC'
b = a
a = 'XYZ'
print(b)

#%%常量
#我感觉他没解释什么是python中的常量
PI=3.14159265359
print(PI)

#%%格式化
#和C大致相同！
print('Hello,%s' % 'world!')#单个变量可以不用括号
print('Hi, %s, you have $%d.' % ('Michael', 1000000))#多个变量用括号
print('Age: %s. Gender: %s' % (25, True))#%s啥情况都好用
print('%-2d-%05.2f' % (3, 1/3))#复习一下C的格式化输出
print('growth rate: %d %%' % 7)#输出%的方法

#format方法
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))
print(f'Hello, {"小明"}, 成绩提升了 {17.125:.1f}%')

#%%新的变量类型
#list&tuple&dict&set
#廖雪峰的网站讲解的已相当好了

#%%流程控制
#if&while&break&continue
#廖雪峰的网站讲解的已相当好了

#%%函数
#
abs(-20)
max(1,2,3)
#数据类型的转化
print(int(12.3))
print(float('12.3'))
#变量指向函数
a=abs
a(-1)
#%%定义函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
        #参数检查
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-233))
print(my_abs('A'))
#%%函数不一定要返回值！
def print_hello_world():
    print('Hello, world!')
print_hello_world()
#用pass表示什么也不做
def nop():
    pass

if 2 >= 1:
    pass
#返回多值
def lots():
    return 1,2,3

r = lots()
print(r)
x,y,z=lots()
x, y = lots()

#默认参数的可变对象的陷阱
#见廖雪峰和一个网页
#https://www.cnblogs.com/wuchenggong/p/9505119.html

#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
calc(1, 2, 3)#在函数内部，参数numbers接收到的是一个tuple
calc()
nums = [1, 2, 3]
calc(*nums)

#%%关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

man1=person('Adam', 45, gender='M', job='Engineer')
print(man1)

extra = {'city': 'Beijing', 'job': 'Engineer'}
man2=person('Jack', 24, **extra)
#kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，
#对kw的改动不会影响到函数外的extra
print(man2)
#%%命名关键字
def person(name, age, *, city = '北京', job):
    print(name, age, city, job)

person('Jack', 24, job='Engineer')

person('Jack', 24)
#会报错，没有输入关于job的信息
person('Jack', 24, work='Engineer')
#会报错，没有这样的关键字
#%%
def person(name, age, *args, city , job):
    print(name, age, args, city, job)

person('Jack', 24, 'Beijing', 'Engineer')
#会报错，关键字参数在传入时必须加入关键字
#%%
def person(name, age, *, city = '北京', job, **kw):
    print(name, age, city, job)

person('Jack', 24, job='Engineer',hobby='python')

#%%参数组合
def f1(a, b, c=0, *args, d , **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'd =',d, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2, d=3)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

#%%递归按照廖雪峰的内容讲解
#这里只展示汉诺塔问题
def hano(n,a,b,c):
    if n==1:
        print(a,'-->',c)
        return None
    hano(n-1,a,c,b)
    hano(1,a,b,c)
    hano(n-1,b,a,c)

hano(3, 'A', 'B', 'C')


#%%高级特性
#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
#取出元素的索引是0，1，2
print(L[:3])

print(L[1:3])

print(L[-2:])
print(L[-2:-1])

#%%
L=list(range(10))
#关于range的介绍参考：
#https://blog.csdn.net/TCatTime/article/details/82941022
print(L[:])
print(L[-5:])
print(L[::2])

print((0, 1, 2, 3, 4, 5)[:3])
print('ABCDEFG'[:3])

#%%迭代
#可迭代对象
#dict
d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)

for value in d.values():
    print(value)

for k,v in d.items():
    print(k,v)
#因为dict的存储不是按照list的方式顺序排列，
#所以，迭代出的结果顺序很可能不一样。
#其他可迭代对象list,tuple,range,str
for i in ('a','b'):
    print(i)

for i in range(2):
    print(i)

for ch in 'ABC':
    print(ch)

#几个特别的迭代对象
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

for x in [(1, 1), (2, 4), (3, 9)]:
    print(x)

#列表生成式
#见廖雪峰的讲解
#%%生成器
def triangles():
    L = [1]
    while 1:
        yield L
        L = [0] + L + [0]
        L = [L[i] + L[i + 1] for i in range(len(L) - 1)]

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break
print(results)
#%%高阶函数
#函数名与变量
abs2=abs
print(f'''
{abs(-10)}
{abs2(-10)}
''')
#函数名也可以被赋值
#函数可以通过函数名被传递
def add(x, y, f):
    return f(x) + f(y)
print(add(-10,90,abs2))

#%%
#map
#map()函数接收两个参数，
#一个是函数，一个是Iterable，
#map将传入的函数依次作用到序列的每个元素，
#并把结果作为新的Iterator返回
a_map=map(str, [1, 2, 3, 4, 5])
for i in a_map:
    print(i)
#%%我们的疑问
a_map=map(str, [1, 2, 3, 4, 5])
print(list(a_map))

print(list(map(str, [1, 2, 3, 4, 5])))

L3=range(10)
print(L3)
#%%reduce
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#见廖雪峰的讲解
