

from Models import Player, MagicalObjects








def test_given_Two_Players_and_when_both_are_in_the_same_Faction_then_they_are_allies():
    #given
    P1 = Player("Larry",1)

    P2 = Player("Juan", 5)
    #when
    P1.enter_in_a_faction("piedreros")
    P2.enter_in_a_faction("piedreros")
    #then
    assert P1.is_allie(P2) 

def test_given_level_is_greater_when_get_attack_then_health_is_half():
    # given
    p1 = Player("Larry", 1)
    p2 = Player("Juan", 4)

    # when
    p1.attack(p2)

    # then
    assert p2.health == 500


def test_given_the_player_has_specific_health_when_the_poison_increase_the_health_over_the_max_health_then_health_is_max_health():
    #given
    p1 = Player("Larry", 1)
    p1.health = 500
    #when
    magical_poison = MagicalObjects("curacion extrema", "health", 600)
    p1.get_health(magical_poison)
    #then
    assert p1.health == 1000

def test_given_the_player_has_specific_health_when_the_poison_increase_the_health_under_the_max_health_then_health_is_the_result_of_addition():
    p1 = Player("Larry", 1)
    p1.health = 500
    #when
    magical_poison = MagicalObjects("curacion extrema", "health", 300)
    p1.get_health(magical_poison)
    #then
    assert p1.health == 800

def test_given_use_the_weapon_when_hit_another_player_then_they_lost_the_health_with_the_value_of_damage():
     #given
    p1 = Player("Larry", 1)
    p2 = Player("simon", 3)
    p2.health = 500
    #when
    magical_poison = MagicalObjects("destruccion", "damage", 600)
    p1.use_weapon(magical_poison,p2)
    #then
    assert p2.health == 0






