class First(object):
    def __init__(self):
        print("first")

class Second(object):
    def __init__(self):
        print( "second")

class Third(First, Second):
    def __init__(self):
        super(Third, self).__init__()
        Second.__init__(self)
        print( "that's it")


o3 = Third()
