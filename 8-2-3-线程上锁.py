import threading

x=0
mutex = threading.Lock()  # 实例化一个互斥锁对象; Mutex是标准术语

def task():  # 先定义一些给子进程用的方法
    global x#声明全局变量
    mutex.acquire()#抢锁; 如果没抢到就会等待; 抢到了就会继续执行, 直到Release
    try:
        for i in range(1000):
            x += 1
    finally:
        mutex.release()#解锁; 让别的线程可以抢锁
        #一定要放在return之前,否则会出现死锁
    print("task: ",x)


if __name__ == "__main__":
    threadA = threading.Thread(target=task)
    threadB = threading.Thread(target=task)

    threadA.start()
    threadB.start()
    print("Main",x)#此时两个线程才刚开始,所以只会打印0

    threadA.join()
    threadB.join()
    print("Main",x)#通过join()等待两个线程结束后,再打印x,此时x有值