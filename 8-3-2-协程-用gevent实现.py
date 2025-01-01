import gevent#这是一个第三方的模块, 可以用于实现协程
from gevent import monkey
import time

monkey.patch_all()#这个方法会自动在time.sleep()等方法中插入协程切换的代码
#加上这句后,就不用考虑哪些方法是需要切换的,哪些方法是不需要切换的了
#否则需要使用gevent.sleep()来代替time.sleep()

def task(name):
    for i in range(5):
        print(name,"在执行任务")
        time.sleep(0.5)

if __name__=="__main__":
    print(__name__)

    g1= gevent.spawn(task,"QingWen")#gevent传参不需要使用元组,直接从第二个参数开始传
    g2= gevent.spawn(task,"TongYing")

    g1.join()
    g2.join()