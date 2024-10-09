class person:
    count = 0
    
    def __init__(self,name,age):
        self.age= age
        self.name= name
        person.count = person.count + 1
    def get_name(self):
        print('the name is %s .'% (self.name))
    def get_age(self):
        print('the age is %i'%(self.age))
    def info(self):
        print('the name is %s and age is%i'%(self.name,self.age))
    def berthday(self):
        self.age = self.age+1
        print('happy berthday %s and you are is %i'%(self.name,self.age))
    def return_count(self):
        return (person.count)

mohammadreza = person('mohammadreza',20)
mohammadreza.info()
mohammadreza.berthday()

print('fefefefef%i'%(mohammadreza.return_count()))


