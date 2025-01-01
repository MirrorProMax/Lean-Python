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
        time.sleep(0.5)


if __name__ == "__main__":
    print("Main进程:", str(os.getpid()))

    runPorcess = multiprocessing.Process(
        target=run
    )  # 这里的Process只是创建了一个进程对象, 并没有真正启动进程
    # 需要target参数, 并且函数后面不能带括号.
    # 如果带括号则会导致在主进程中被调用
    eatPorcess = multiprocessing.Process(target=eat)

    runPorcess.start()
    eatPorcess.start()
