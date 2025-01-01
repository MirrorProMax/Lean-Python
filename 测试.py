# 创建多线程
import multiprocessing  # 用于创建子进程
import os  # 用于获取进程id
import time  # 用于sleep


def run():  # 先定义一些给子进程用的方法
    print("Run进程:", str(os.getpid()), "父进程:", os.getppid())
    for i in range(5):
        print("正在Run第", i, "次")
        time.sleep(0.5)


def eat():
    print("Eat进程:", str(os.getpid()), "父进程:", os.getppid())
    for i in range(5):
        print("正在Eat第", i, "次")
        time.sleep(1)


if __name__ == "__main__":
    print("Main进程:", str(os.getpid()))

    runPorcess = multiprocessing.Process(target=run)
    eatPorcess = multiprocessing.Process(target=eat)

    runPorcess.start()
    eatPorcess.start()