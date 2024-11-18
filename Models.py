class MagicalObjects:
    def __init__(self,name,type, value) :
        self.name = name
        self.type = type
        self.value = value



class Player:
    def __init__(self, Name : str, level=1): 
        self.name = Name
        self.level = level
        self.status = True
        self.faction = []
        self.health = 1000
        self.max_health= 1000
        self.total_damage = 0
        self.magical_objects = []



        


    def get_health(self, magical_object: MagicalObjects)-> None:
        if magical_object.type == "health":
            self.health += magical_object.value
            if self.health > self.max_health:
                self.health = self.max_health

    def use_weapon(self, magical_object: MagicalObjects, player2: "Player")-> None:
        if magical_object.type == "damage":
            player2.health -= magical_object.value
            if player2.health <= 0:
                player2.health = 0
                player2.status = False
                player2.drop_magical_objects()

    

    def aplly_damage(self, victim: "Player")-> None:
        if self.level - victim.level <= 5 :
            victim.health = victim.health * 0.5

        elif victim.level - self.level >=5:
            victim.health = victim.health * 1.5

        if victim.health <=0 :
            victim.health = 0
            victim.status = False
            victim.drop_magical.objects()
    
    def game_results(self, player2: "Player")-> None:
        if self.status == 0:
            return
        if player2.status == 0:
            if player2.level < 6:
                self.total_damage += player2.max_health
            elif player2.level >= 6:
                self.total_damage += player2.max_health
        self.change_level()

    def change_level(self)-> None:
        if self.level >= 6:
            self.health = 1500
            self.max_health = 1500
        lenght_of_list = len(self.faction)
        faction_level = len(self.faction)//3
        if self.level== 1 and lenght_of_list >= 3 and self.total_damage >=1000:
            self.level = 2

        if self.level == 2 and lenght_of_list >= 6 and self.total_damage >= 2000:
            self.level = 3

        if self.level == 3 and lenght_of_list >= 9 and self.total_damage>= 3000:
            self.level = 4

        if  self.level >= 4 and self.level<10 and self.level < faction_level:
            if faction_level > 10:
                self.level = 10
            elif faction_level < 10:
                self.level = faction_level



    def is_allie(self, victim: "Player")-> bool:
        for Faction in self.faction:
            if Faction in victim.faction:
                return True
            
        return False
    
    
    
    def attack(self, victim: "Player")-> None:
        flag = self.is_allie(victim)
        if not flag: 
            self.aplly_damage(victim)
        
            
      
        

    

    def enter_in_a_faction(self, Faction):
        if Faction is not self.faction:
            self.faction.append(Faction)
            self.change_level()

        
            



    def leave_faction(self, Faction):
        if Faction in self.faction:
            self.faction.remove(Faction)
        
            

    def drop_magical_objects(self):
        if self.status == False:
            self.magical_objects.clear()      

    def get_magical_objects(self,magical_object):
        self.magical_objects.append(magical_object)
              






