class Player:
    def __init__(self, Name, level=1): 
        self.name = Name
        self.level = level
        self.status = True
        self.faction = []
        self.health = 1000
        self.max_health= 1000
        self.magical_objects = []


    def get_health(self, magical_object):
        if magical_object.type == "health":
            self.health += magical_object.value


    def apllydamage(self, attacker):
        if self.level - attacker.level >= 5 :
            self.health = self.health * 0.5

        elif attacker.level - self.level >=5:
            self.health = self.health * 1.5

        if self.health <=0 :
            self.health = 0
            self.status = False

     

    def is_allie(self, victim):
        for Faction in self.Faction:
            if Faction in victim.Faction:
                return True
            else:
                return False
    
    
    
    def attack(self, victim ):
        flag = self.isallie(victim)
        if flag: 
            return print("you Cant damage him is your allie")
        else:
            self.getattack(victim, self)
      
        

    

    def enter_in_a_faction(self, Faction):
        if Faction in self.Faction:
            return print("you are aleredy in this faction")
        
        else:
            self.Faction.append(Faction)



    def leave_faction(self, Faction):
        if Faction in self.Faction:
            return print("you are not in this Faction")
        else :
            self.Faction.remove(Faction)


class MagicalObjects:
    def __init__(self,name,type, value) :
        self.name = name
        self.type = type
        self.value = value



