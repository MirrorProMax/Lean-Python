from SubFunc import printType
# from collections.abc import Iterable#可迭代对象
# from collections.abc import Iterator#迭代器

class 斐波那契数列迭代器:
    def __init__(self, maxTimes):
        self.maxNum= maxTimes
        self.counter= 0
        self.a=0
        self.b=1

    def __iter__(self):#返回迭代器对象
        return self
    
    def __next__(self):
        if self.counter<self.maxNum:
            self.a,self.b = self.b,self.a+self.b
            self.counter+=1
            return self.a
        else:
            raise StopIteration#停止迭代

if __name__ == "__main__":
    f= 斐波那契数列迭代器(5)#此时并没有执行x次迭代
    printType(f)

    try:
        for i in range(10):
            print("For循环内:",next(f))
        
        print(f.__next__())#本质和next(f)一样
    except StopIteration:
        print("迭代器已经停止")
    except Exception as e:
        print(e)