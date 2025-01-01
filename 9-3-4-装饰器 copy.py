from typing import Callable


def outFunc(paramFunc)-> Callable[[], None]:#输入参数为函数，返回值为函数
    def innerFunc(*args, **kwargs):#注意设置位置传参和关键字传参
        print('请先登陆')
        paramFunc(*args, **kwargs)#注意设置位置传参和关键字传参
    return innerFunc

@outFunc#等价于comment= outFunc(comment)
def comment():
    print("写评论")

if __name__ == "__main__":
    comment()