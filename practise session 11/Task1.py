class vehicle:
    brand="Hundai"
    model="i-20"

class gadi(vehicle):
    def dis(self,doors):
        print(f"{self.brand}{self.model}",doors)

obj1=gadi()
obj1.dis(5)