class Player:
    def __init__(self,Faction, Name, level=1, status=1, health=1000): 
        self.Name = Name
        self.level = level
        self.status = status
        self.Faction = Faction
        self.health = health


    def getattack(self, attacker_level):
        if self.level - attacker_level >= 5 :
            self.health = self.health * 0.5

        elif attacker_level - self.level >=5:
            self.health = self.health * 1.5

        if self.health <=0 :
            self.health = 0
            self.status = 0

            

