class A:
    def __str__(self):
        self.num1 = 100
        self.num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.num2))


class B(A):
    def demo(self):
        # print("访问父类的私有属性 %d" % self.__num2)
        pass

b = B()

b.demo()

