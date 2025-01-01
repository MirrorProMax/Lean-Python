from typing import Callable


def outFunc(paramFunc)-> Callable[[], None]:#输入参数为函数，返回值为函数
    def innerFunc():
        print('请先登陆')
        paramFunc()
    return innerFunc

def comment():
    print("写评论")

if __name__ == "__main__":
    f= outFunc(comment)
    f()#请先登陆\n写评论