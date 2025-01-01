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

    runPorcess.start()
    runPorcess.join(timeout=1.5)
    # join方法必须放在start方法之后,否则会报错
    # 主进程的join方法会等待子进程结束后,再继续执行. 如果子进程不结束, 或未到timeout时间, 主进程会一直等待

    eatPorcess.start()
