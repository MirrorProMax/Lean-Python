import greenlet#这是一个第三方的模块, 可以用于实现协程
import time

def run():
    while True:
        print('run')
        g2.switch()
        time.sleep(0.5)

def eat():
    while True:
        print('eat')
        g1.switch()
        time.sleep(0.5)

if __name__=='__main__':
    g1= greenlet.greenlet(run)
    g2= greenlet.greenlet(eat)

    print("Main: g1启动")
    g1.switch()#启动g1
    print("Main: g1完成启动")

    print("Main: g2启动")
    g2.switch()#这行并不会被触发, 因为g1中会切换到g2
    print("Main: g2完成启动")