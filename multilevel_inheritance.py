class Human(object): #this is the root class
    def __init__(self,num_heart):
        print('calling init from human class')
        self.eyes = 2
        self.heart = num_heart
        self.nose = 1
    def eat(self):
        print('I can eat')
    def work(self):
        print('I can work')
class Male(Human):
    print('calling init from male class')
    def __init__(self,name):
        self.name = name
    def sleep(self):
        print("I can sleep")
class Boy(Male):
    def __init__(self,heart,name, can_read): ## you have to also put in the parameters of the previous base classes if you want to call them
        Human.__init__(self,heart,) #this calls properties from the human clas
        Male.__init__(self,name)
        self.read = can_read
    def work(self):
        #Human.work(self) #this code will enable the boy class to access the work function from the human class and it's own
        super().work() #this code does the same thing as the code above
        print("I can code")



boy_1 =Boy(1,"tofunmi",True)
boy_1.eat()
boy_1.work()
print(boy_1.read)
Boy.mro()
print(Boy.mro())
