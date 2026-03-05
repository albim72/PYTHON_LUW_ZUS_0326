class AddHelloMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs["hello"] = lambda self: print("Hello, Python!")
        return super().__new__(cls, name, bases, attrs)

class A(metaclass=AddHelloMeta):
    pass

a = A()
a.hello()


def helloB(self):
    print("Hello, nowa klasa B!")
class B(A):
    pass



#monkey patching
b = B()
B.hello = helloB
b.hello()

bt = B()
bt.hello()

class C(B):
    pass

c= C()
c.hello()
