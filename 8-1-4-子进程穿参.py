import multiprocessing
import os
import time


def intFunc(inInt: int):
    print("Int:", inInt)


def argsFunc(*args):
    print("Args:", args)


def kwargsFunc(**kwargs):
    print("Kwargs:", kwargs)


if __name__ == "__main__":
    print("Main进程:", str(os.getpid()))

    p1 = multiprocessing.Process(
        target=intFunc, args=(123,)
    )  # 如果参数格式与函数定义不符,会报错
    p2 = multiprocessing.Process(target=argsFunc, args=(789,))
    p3 = multiprocessing.Process(target=kwargsFunc, kwargs={"args": "0ab"})
    p1.start()
    p2.start()
    p3.start()
    print("Main进程结束")
