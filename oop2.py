class computer:
    def __init__(self,cpu,ram,hard):
        self.ram=ram
        self.cpu=cpu
        self.hard=hard
    def values(self):
        return self.ram+self.cpu+self.hard
    
class labtop(computer):
    def values(self):
        return self.ram+self.cpu+self.hard+self.size
    

labtop1 = labtop(1,2,3)
labtop1.size = 5
print(labtop1.values())



