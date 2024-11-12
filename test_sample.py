

from Models import Player, MagicalObjects

from pattern_desings.iterator import MyIterator_Reverse, MyIterator_Random






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

def test_given_use_the_weapon_when_hit_another_player_then_the_opponent_dead():
     #given
    p1 = Player("Larry", 1)
    p2 = Player("simon", 3)
    p2.health = 500
    #when
    magical_poison = MagicalObjects("destruccion", "damage", 600)
    p1.use_weapon(magical_poison,p2)
    #then
    assert p2.health == 0

def test_given_use_the_weapon_when_hit_another_player_then_the_opponent_has_sustraction_of_the_health():
     #given
    p1 = Player("Larry", 1)
    p2 = Player("simon", 3)
    p2.health = 1000
    #when
    magical_poison = MagicalObjects("destruccion", "damage", 600)
    p1.use_weapon(magical_poison,p2)
    #then
    assert p2.health == 400

def test_given_the_player_is_lvl_1_when_he_enter_in_3_Factions_And_have_1000_damage_then_he_upgrade_level():
    #given
    p1 = Player("larry",2)
    #when
    p1.total_damage = 2010
    p1.enter_in_a_faction("locos")
    p1.enter_in_a_faction("locos2")
    p1.enter_in_a_faction("locos3")
    p1.enter_in_a_faction("locos")
    p1.enter_in_a_faction("locos2")
    p1.enter_in_a_faction("locos3")
    
    #then
    #p1.change_level()
    assert p1.level == 3

def test_given_the_player_is_lvl_6_when_he_enter_in_21_then_he_upgrade_level():
    #given
    p1 = Player("larry",6)
    #when
    p1.enter_in_a_faction("locos")
    p1.enter_in_a_faction("locos2")
    p1.enter_in_a_faction("locos3")
    p1.enter_in_a_faction("locos")
    p1.enter_in_a_faction("locos2")
    p1.enter_in_a_faction("locos3")
    p1.enter_in_a_faction("locos")
    p1.enter_in_a_faction("locos2")
    p1.enter_in_a_faction("locos3")
    p1.enter_in_a_faction("locos")
    p1.enter_in_a_faction("locos2")
    p1.enter_in_a_faction("locos3")
    p1.enter_in_a_faction("locos")
    p1.enter_in_a_faction("locos2")
    p1.enter_in_a_faction("locos3")
    p1.enter_in_a_faction("locos")
    p1.enter_in_a_faction("locos2")
    p1.enter_in_a_faction("locos3")
    p1.enter_in_a_faction("locos")
    p1.enter_in_a_faction("locos2")
    p1.enter_in_a_faction("locos3")
    #p1.change_level()
    #then
    assert p1.level == 7

def test_given_the_player_is_in_faction_when_he_leaves_the_faction_is_removed():
    #given
    p1 = Player("Larry",1)
    p1.enter_in_a_faction("locos")
    #when
    p1.leave_faction("locos")
    #then
    assert len(p1.faction) == 0

def test_given_the_player_get_magical_objects_when_he_get_that_then_the_list_has_1_item_more():
    #given
    p1= Player("larry", 1)
    magical_object = MagicalObjects("destrccuin", "health",30)
    #when
    p1.get_magical_objects(magical_object)
    #then
    assert len(p1.magical_objects) == 1

def test_given_the_player_has_magical_objects_when_he_dies_then_he_drop_the_magical_objects():
     #given
    p1= Player("larry", 1)
    magical_object = MagicalObjects("destrccuin", "health",30)
    p1.get_magical_objects(magical_object)
    #when
    p1.status = False
    p1.drop_magical_objects()
    #then
    assert len(p1.magical_objects) == 0



def test_given_we_have_a_list_when_we_need_to_take_that_in_reverse_then_the_iterator_give_us_the_list_in_reverse():
    items = [1, 2, 3]
    my_iter = MyIterator_Reverse(items)
    result = [item for item in my_iter]
    assert result == [3,2,1]


def test_given_we_have_a_list_when_we_need_to_take_that_with_random_items_then_the_iterator_give_us_the_list_random():
    items = [1,2,3]
    my_iter = MyIterator_Random(items)
    result = [item for item in my_iter]
    assert my_iter != result