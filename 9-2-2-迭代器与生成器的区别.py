from SubFunc import printType
from collections.abc import Iterable#可迭代对象
from collections.abc import Iterator#迭代器

strA= "tanqingwen"
print("StrA:",isinstance(strA,Iterable))#判断theStr是否为可迭代对象
print("StrA:",isinstance(strA,Iterator))#判断theStr是否为迭代器; theStr不是迭代器，但是是可迭代对象

strB= iter(strA)#将strA转换为迭代器
print("StrB:",isinstance(strB,Iterator))#判断theStr是否为迭代器

#转换为迭代器后，可以用next()函数获取迭代器的下一个元素
#而生成器不能用next()函数获取下一个元素
for i in range(5):
    print("For循环内:",next(strB))