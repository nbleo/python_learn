class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):

    def bark(self):
        print("汪汪汪")

class XiaoTian(Dog):

    def fly(self):
        print("我在飞飞飞")

    def eat(self):
        print("我吃天上的食物")

    def bark(self):
        print("叫汪汪汪")

class Cat(Animal):

    def catch(self):
        print("抓老鼠")

# 创建一个对象 - 狗对象

wangcai = XiaoTian()

wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()
wangcai.fly()
