from typing import Generator

def 斐波那契数列Generator(times)->Generator[int,None,None]:
    a,b=0,1#斐波那契数列的前两个数是0和1
    yield a#先把0放入生成器
    yield b#再把1放入生成器
    for i in range(times-2):#因为已经有了0和1，所以只需要生成countNum-2个数
        a,b=b,a+b#斐波那契数列的规则是后一个数等于前两个数之和
        yield b#把新生成的数加入生成器

if __name__ == "__main__":
    times=10
    print(list(斐波那契数列Generator(times)))#Generator需要用list()函数转换成list