from Objects import Player



P1 = Player("Larry",1)

P2 = Player("Juan", 5)

P1.EnterInAFaction("piedreros")
P2.EnterInAFaction("piedreros")
print(P1.Name)
def test_isallie():
    assert P1.isallie(P2) 

