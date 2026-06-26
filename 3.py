class Laptop:
    storage_type="ssd"
    def __init__(self,RAM,storage):
     self.RAM =RAM
     self.storage =storage
    def get_info(self):
        print(f"hey the ram is {self.RAM} THE STORAGE IS {self.storage}")#instance method


    
l1=Laptop(445,56)
l1.get_info()
#