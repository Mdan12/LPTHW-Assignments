class Penis(object):

    def __init__(self, penisname):
        print(penisname, "PARENT altered()")

class Child(Penis):

    def __init__(self):
        print("CHILD, BEFORE PARENT altered()")
        super().__init__('Suckmydick')
        print("CHILD, AFTER PARENT altered()")


son = Child()
