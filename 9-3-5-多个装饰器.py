from typing import Callable


def 装饰器A(inFuncA: Callable[[], str]) -> Callable[[], str]:
    print("2: 装饰器A完成进入,即将定义innerFuncA")

    def innerFuncA() -> str:
        print(
            "10*: 装饰器A的innerFunc进入"
        )  # 这里的外层其实是装饰器B的innerFuncB,所以9会先被执行,然后再执行10
        return (
            "<A>" + inFuncA() + "<A>"
        )  # 这里的inFuncA()就是comment,所以10会先于11被执行

    print("3: innerFuncA完成定义,装饰器A即将退出")
    return innerFuncA


def 装饰器B(inFuncB: Callable[[], str]) -> Callable[[], str]:
    print("4: 装饰器B完成进入,即将定义innerFuncB")

    def innerFuncB() -> str:
        print("9*: 装饰器B的innerFunc进入")
        return (
            "<B>" + inFuncB() + "<B>"
        )  # 这里的inFuncB()就是装饰器A的innerFuncA,所以9会先被执行

    print("5: innerFuncB完成定义,装饰器B即将退出")
    return innerFuncB


print("1: 文件进入")


@装饰器B
@装饰器A
def comment():
    print(
        "11*: comment进入,并即将将值返回给外部"
    )  # 这里的外层其实是装饰器A的innerFuncA,所以10会先于11被执行

    return "ha"  # 当文本被时,会按照innerFuncA被组装成<A>ha<A>,然后再按照innerFuncB被组装成<B><A>ha<A><B>


print(
    "6: comment完成装饰"
)  # 这里因为装饰了comment, 所以装饰器内的代码被执行了; 当然装饰器内的innerFunc只是被定义了, 并没有被调用

if __name__ == "__main__":
    print("7: 进入Main")
    print("8*: comment开始调用")
    c = comment()
    print("12*: comment完成调用,并已赋值给c")
    print("13: c开始打印")
    print(c)  # <B><A>ha<A><B>
    print("14: c完成打印")
