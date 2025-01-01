#多线程
#多线程比多进程开销更小,切换速度快
import threading
import time

def run():  # 先定义一些给子进程用的方法
    print("Run: 当前线程为",threading.current_thread())
    for i in range(5):
        print("正在Run第", i+1, "次")
        time.sleep(0.2)


def eat():
    print("Eat: 当前线程为",threading.current_thread())
    for i in range(5):
        print("正在Eat第", i+1, "次")
        time.sleep(0.3)


if __name__ == "__main__":
    print("Main: 当前线程为",threading.current_thread())

    runThread = threading.Thread(
        target=run
    )
    eatThread = threading.Thread(target=eat)

    runThread.daemon = True  # 设置为守护线程, 当主线程结束时, 子线程还未执行完就结束了
    eatThread.daemon = True

    runThread.start()
    eatThread.start()

    print("开始执行RunThread.join()")
    runThread.join()  # 等待子线程结束
    print("结束执行RunThread.join()")

    print("开始执行EatThread.join()")
    eatThread.join()
    print("结束执行EatThread.join()")
    #看起来主线程是执行到eatThread.join()等待
    #实际上会先等待runThread结束,然后再等待eatThread结束
    #但因为runThread和eatThread结束的时间没差多少,所以看起来是同时结束的

    print("Main线程结束")