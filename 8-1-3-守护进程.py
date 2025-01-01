import multiprocessing
import os
import time


def run():
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

    runPorcess = multiprocessing.Process(target=run)
    eatPorcess = multiprocessing.Process(target=eat)

    runPorcess.daemon = True  # 守护进程
    eatPorcess.daemon = True

    runPorcess.start()
    eatPorcess.start()

    print("Main进程结束")
    exit()  # 退出主进程直接打断子进程
