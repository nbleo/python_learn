class A:

    def test(self):
        print("test method")


class B:

    def demo(self):
        print("demo method")

    def test(self):
        print("test-2 method")


class C(B, A):
    pass


c = C()

c.test()
c.demo()

print(C.__mro__)

