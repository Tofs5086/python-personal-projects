class Human:
    def __init__(self,num_heart):
        print('calling init from human')
        self.num_eyes = 2
        self.num_nose = 1
        self.num_heart = num_heart
    def eat(self):
        print('I can eat')
    def work(self):
        print('I can code')

class Male():
    def __init__(self,name):
        print('calling init from male')
        self.name = name
    def flirt(self):
        print('i can flirt')
    def work(self):
        print('I can code')

class Boy(Human,Male): #This code shows that it is now the child of Class male and class Human
    def __init__(self,name,heart,language):
        Human.__init__(self,heart)
        Male.__init__(self,name)
        self.language = language
    def sleep(self):
        print('I can sleep')
    def work(self):
        print('I can test code')
    def display(self):
        print(f'Hi I am {self.name}, and i work on {self.language}')


boy_1 = Boy("Tofunmi",1,"python")
#boy_1.flirt()
boy_1.num_nose
print(boy_1.num_nose)
print(boy_1.num_heart)
boy_1.display()
#print(boy_1.language)
#boy_1.work()
#Male.work(boy_1)
#print(Boy.mro())# prints the function that lists the method resolution order of the boy class