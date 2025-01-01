import multiprocessing
import multiprocessing.process
import time
import random

def putFunc(q:multiprocessing.Queue):
    for data in ["a", "b", "c", "d", "e"]:
        time.sleep(random.random())#随机休眠一段时间
        print("Put:", data)
        q.put(data)#将数据放入队列


def getFunc(q:multiprocessing.Queue):
   while True:
       value=q.get()
       print("Get:", value)

if __name__ == "__main__":
    queue= multiprocessing.Queue()
    putProcess= multiprocessing.Process(target=putFunc, args=(queue,))
    getProcess= multiprocessing.Process(target=getFunc,args=(queue,))

    putProcess.start()
    getProcess.start()

    putProcess.join()# 没有join会导致报错
    getProcess.terminate()# 由于getProcess是一个死循环，所以需要手动终止