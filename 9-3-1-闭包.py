def outer(inNumA:int):#闭包
    def inner(inNumB:int):#内部函数
        resoult = inNumA + inNumB#内部函数的计算
        print(resoult)
    return inner#返回内部函数; 闭包的特点是返回的函数内部引用了外部函数的变量

f1=outer(100)
f1(1)#这里不需要print,因为inner函数内部已经print了

f2=outer(200)
f2(2)
