#!/usr/bin/python
# -*- coding: utf-8 -*-

#if 判断
"""num =12
asd = '1'
try:
    print('123')
    if asd :
        print(num[0])
        print('456')
except:
    print('999')"""
"""height = float(input('请输入身高'))
strong = float(input('请输入体重'))
print('小明身高为%s,体重为%s'%(height, strong))
BIM = strong/height**2
print('小明身体状况指数为%s'%BIM)
if BIM < 18.5:
    print('过轻')
elif BIM >= 18.5 and BIM <= 25:
    print('正常')
elif BIM >= 25 and BIM <= 28:
    print('过重')
elif BIM >= 28 and BIM <= 32:
    print('肥胖')
elif  BIM >= 32:
    print('严重肥胖')
else :
    print('过度严重肥胖')"""


'''a = 1
b = 2
c = 3
d = 4
if a :
    print(1)
    if b==3:
        print(2)
    else:
        print(3)
else:
    print('不是1')
    if c ==4:
        print(3)
    else:
        print(4)'''


"""def outer():
    cheer = 'hello '
    def inner(name):
        return cheer + name
    return inner

if __name__ == "__main__":
    #输出hello kevin
    print(outer()('kevin'))"""

import time

# 这个是外函数
"""def record_time(func):
    def wrapper(*kwargs):
        print('function start at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ))
        total = func(*kwargs)
        print('function end at {}'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) ))
        return total
    return wrapper

# 这个是我们真正的功能函数
def sum(*kwargs):
    total = 0
    for ele in kwargs:
        total = total + ele
    time.sleep(2)
    return total


if __name__ == "__main__":
    # 外函数，内函数，和功能函数一起，实现了不改变功能函数的前提下，给功能函数加功能的操作。
    print(record_time(sum)(1,2,3,4))"""

import turtle,math
# bob = turtle.Turtle()
# print(bob)
# turtle.mainloop()     #停留在改页面

"""def polyline (t , n , length , angle ) :
    for i in range (n ) :
        t . fd ( length )
        t . lt ( angle )
def polygon (t , n , length ) :
    angle = 360.0 / n
    polyline (t , n , length , angle )
def arc (t , r , angle ) :
    arc_length = 2 * math . pi * r * angle / 360
    n = int ( arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float ( angle ) / n
    polyline (t , n , step_length , step_angle )
print(polyline(bob,10,10,10))
turtle.mainloop()
"""

#递归，函数调用自己的函数
"""def countdown ( n ) :
    if n <= 0:
        print ('Blastoff !')
    else :
        print (n)
        countdown (n-1)

countdown ( 3 )"""


#递归：函数调用自己本身的函数
"""def print_n (s , n ) :
    if n <= 0:
        return
    print (s )
    print_n (s , n-1)
print_n(3,2)"""


"""def countdown ( n ) :
    while n > 0:
        print ( n )
        n = n - 1
    print ('Blastoff !')

countdown ( 3 )
"""

"""def sequence ( n ) :
    while n != 1:
        print(n)
        if n % 2 == 0:  # n is even
            n = n / 2
        else : # n is odd
            n = n *3 + 1
sequence(3)"""


# *解包
"""def f(a,b,c):
    print(a,b,c)
a = [1,2,3]
b = [1,2,3]
c = [1,2,3]
f(a,b,c)
f(*a)"""

#可变参数args:
"""def func(n,*args):
    print(n)
    print(args) #未拆包
    print(*args)    #进行拆包
func(1,2,3,4)"""
# 压包过程,压包就是解包的逆过程，用zip函数实现
"""a = [0,1,2,3]
b = [1,2,3]
for i in zip(a,b):
    print(i)"""
# 压包与解包混合，先是函数将压包成为一个可迭代对象  对可迭代对象的每一个元素进行解包 此时就可以分别调用变量进行计算
"""a = [0,1,2,3]
b = [1,2,3]
for i,j in zip(a,b):
    print(i+j)"""

"""def choice():
    print('请选择，是左还是右')
    answer = input('请输入 左 或者 右 ：')
    if answer == '左' or answer == '左边':
        print('你选择了左')
    elif answer == '右' or answer == '右边':
        print('你选择了右')
    else:
        print('两个 你都没选择')
        choice()
choice()"""

"""list = ["这", "是", "一个", "测试","数据"]

for i in range(len(list)):

    print(i,list[i])"""



import os

#flask框架  路由不带参数    路由：用户请求地址与以及对应的视图函数
"""from flask import  Flask
app = Flask(__name__)
@app.route('/')
def app1():
    return "第一个程序"

if __name__ =="__main__":
    app.run(debug=True)
    
from flask import  Flask

app = Flask(__name__)
"""
#递归函数
"""import time
person_list = ['伊博乐','王斌','包子','治国','sss']
def ask_way(person_list):
    print('-'*20)
    if len(person_list)==0:
        return '没人知道'
    person=person_list.pop(0)
    if person == '治国':
        return '%s说：我知道，邮局对面' %person
    print('hi，%s,网吧在哪'%person)
    print('%s说：我不知道，我给你问问%s'%(person,person_list))
    time.sleep(1)
    res = ask_way(person_list)#把问的结果截取
    print('%s说'%person,res)
    return res
ask_way(person_list)"""


"""def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(g.send(7))
"""


"""def para(a):
    print(a)


def para(b):
    print(b)


if __name__ == '__main__':
    list01 = [para(1),para(2)]
    for i in list01:
        print(i)
"""


class MainClass:
    def shilifangfa(self):
        print('这是一个实例方法')

    @classmethod
    def leifangfa(cls):
        print('这是一个类方法', cls)

    @staticmethod
    def jingtaifangfa():
        print('这是一个静态方法')


m = MainClass()
MainClass.shilifangfa(1)
m.leifangfa()
m.jingtaifangfa()