def 装饰器方法A(inFunc):
    def innerFunc():
        print("装饰器A")
        return "<A>" + inFunc() + "<A>"

    return innerFunc


def 装饰器方法B(inFunc):
    def innerFunc():
        print("装饰器B")
        return "<B>" + inFunc() + "<B>"

    return innerFunc


# 靠近函数的装饰器优先
@装饰器方法B
@装饰器方法A
def comment():
    return "hahaha"


if __name__ == "__main__":
    print(comment())
