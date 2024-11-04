class Player:
    def __init__(self,Faction, Name, level=1, status=1, health=1000): 
        self.Name = Name
        self.level = level
        self.status = status
        self.Faction = []
        self.health = health


    def getattack(self, attacker):
        if self.level - attacker.level >= 5 :
            self.health = self.health * 0.5

        elif attacker.level - self.level >=5:
            self.health = self.health * 1.5

        if self.health <=0 :
            self.health = 0
            self.status = 0

     

    def isallie(self, victim):
        for Faction in self.Faction:
            if Faction in victim.Faction:
                return True
            else:
                return False
    
    
    
    def Attack(self, victim ):
        flag = self.isallie(self, victim)
        if flag: 
            return print("you Cant damage him is your allie")
        else:
            self.getattack(victim, self)
      
        

    

    def EnterInAFaction(self, Faction):
        if Faction in self.Faction:
            return print("you are aleredy in this faction")
        
        else:
            self.Faction.append(Faction)



    def LeaveFaction(self, Faction):
        if Faction in self.Faction:
            return print("you are not in this Faction")
        else :
            self.Faction.remove(Faction)



    




