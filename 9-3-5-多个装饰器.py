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


@装饰器方法B
@装饰器方法A
def comment():
    return "ha"


if __name__ == "__main__":
    print(comment())
    # 装饰器B
    # 装饰器A
    # <B><A>ha<A><B>
