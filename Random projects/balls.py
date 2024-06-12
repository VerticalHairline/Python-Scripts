#Tehe balls

class balls():

    info = "a place to store ball-related data"

    universalAtributes = ["spherical"]
    
    def __init__(self, *atribute):
        atributes = list(atribute)
        self.atributes = atributes
        
    def addAtribute(self, atribute):
        self.atributes.append(atribute)
        print("current atributes:""\n")
        print(self.atributes)
              

    def addUniAtribute(self, uniAtribute):
        self.universalAtributes.append(uniAtribute)

    def removeAtribute(self, remAtribute):
        if remAtribute in self.atributes:
            self.atributes.remove(remAtribute)
        else:
            print("please remove an atribute that is already on the list. Here is that list:""\n")
            print(self.atributes)

    def removeUniAtribute(self, remUniAtribute):
        if remUniAtribute in self.universalAtributes:
            self.universalAtributes.remove(remUniAtribute)
        else:
            print("please remove an atribute that is already on the list. Here is that list:""\n")
            print(self.universalAtributes)

aiden = balls("hairy",2,"huge")

