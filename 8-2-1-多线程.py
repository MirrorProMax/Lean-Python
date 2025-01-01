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

    runThread.start()
    eatThread.start()