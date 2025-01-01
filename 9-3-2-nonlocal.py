def outer(inNumA:int):#闭包
    def inner(inNumB:int):
        nonlocal inNumA#声明inNumA是外部函数的变量;
        #nonloacl的范围比global小
        #与global的区别是global是全局变量, nonlocal是外部函数的变量
        inNumA+=10
        resoult = inNumA + inNumB
        print(resoult)
    return inner

if __name__ == "__main__":
    f1=outer(100)
    f1(1)

    f2=outer(200)
    f2(2)