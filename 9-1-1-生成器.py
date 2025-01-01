from typing import Generator
from SubFunc import printType
temp1: list[int]=[data**2 for data in range(0,5)]#平方使用**符号; 用中括号括起来会生成list
temp2: Generator[int,None,None] = (data**2 for data in range(0,5))#用小括号括起来会生成Generator
#当你定义一个生成器（Generator）时，它的类型注解通常会遵循一个特定的格式，即 Generator[YieldType, SendType, ReturnType]

printType(temp1)
printType(temp2)

try:
    print(next(temp2))#next()函数用于获取迭代器的下一个元素
    print(next(temp2))
    print(next(temp2))
    print(next(temp2))
    print(next(temp2))
    print(next(temp2))#StopIteration: 生成器已经迭代完毕，再次调用next()函数会抛出StopIteration异常
except Exception as e:
    print(e)