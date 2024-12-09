class Appliance:
    def turn_on(self):
        print("The appliance is now on.")

class WashingMachine(Appliance):
    def turn_on(self):
        print("The washing machine is now on.")

class Refrigerator(Appliance):
    def turn_on(self):
        print("The refrigerator is now on.")

class Microwave(Appliance):
    def turn_on(self):
        print("The microwave is now on.")

appliances = [WashingMachine(), Refrigerator(), Microwave()]
for appliance in appliances:
    appliance.turn_on()
