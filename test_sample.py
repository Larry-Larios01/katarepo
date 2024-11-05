

from Objects import Player








def test_given_Two_Players_and_when_both_are_in_the_same_Faction_then_they_are_allies():
    #given
    P1 = Player("Larry",1)

    P2 = Player("Juan", 5)
    #when
    P1.EnterInAFaction("piedreros")
    P2.EnterInAFaction("piedreros")
    #then
    assert P1.isallie(P2) 

def test_given_level_is_greater_when_get_attack_then_health_is_half():
    # given
    p1 = Player("Larry", 10)
    p2 = Player("Juan", 4)

    # when
    p1.getattack(p2)

    # then
    assert p1.health == 500










