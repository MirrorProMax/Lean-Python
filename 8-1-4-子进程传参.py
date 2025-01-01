import multiprocessing
import os
import time


def theFunc(inInt:int,inStr:str):
    print("inInt:", int, "inStr:", inStr)

if __name__ == "__main__":
    print("Main进程:", str(os.getpid()))

    p1 = multiprocessing.Process(
        target=theFunc, args=(123,)
    )  # 如果参数格式与函数定义不符,会报错
    p3 = multiprocessing.Process(target=theFunc, kwargs={"args": "0ab"})#这里的字典并不是真的传一个字典,而是按关键字给target传参
    p1.start()
    p3.start()
    print("Main进程结束")
