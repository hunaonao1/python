
class Hello:
    def __init__(self,name):
        self.name=name
    def sayhello(self):
        print("Hello {0}".format(self.name))

class Hi(Hello):
    def __init__(self,name):
       Hello.__init__(self.name)
    def sayHi(self):
        print("Hi {0}".format(self.name))

h=Hello("baby")
h.sayhello()

h1=Hi("hunao")
h1.sayHi()