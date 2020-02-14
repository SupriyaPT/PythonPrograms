from test1 import TestClass1


class TestClass2(TestClass1):
    a=0
    def test(self):
        print("from child 1")
        TestClass2.a=10
        print(self.a)
        print (TestClass2.a)
        super(TestClass2, self).test()

    @staticmethod
    def test_method():
        print("from static")

    def test1(self):
        return None, None

a=TestClass2()
a.test()
a.test_method()

c,d = a.test1()
print(c)
print(d)
