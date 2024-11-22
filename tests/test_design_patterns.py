
from pattern_desings.iterator import MyIteratorFilter, MyIteratorFind, MyIteratorMap, MyIteratorRandom, MyIteratorReverse







def test_given_we_have_a_list_when_we_need_to_take_that_in_reverse_then_the_iterator_give_us_the_list_in_reverse():
    #given
    items = [1, 2, 3]
    #when
    my_iter = MyIteratorReverse(items)
    #then
    result = [item for item in my_iter]
    assert result == [3,2,1]


def test_given_we_have_a_list_when_we_need_to_take_that_with_random_items_then_the_iterator_give_us_the_random_list():
    #given
    items = [1,2,3]
    #when
    my_iter = MyIteratorRandom(items)
    #then
    result = [item for item in my_iter]
    assert my_iter != result

def test_given_we_have_a_list_when_we_need_to_take_specific_items_then_the_iterator_give_us_the_list_filtered():
    #given
    items = [1,2,3,4,5,6,7,8,9,10]
    #when
    my_iter = MyIteratorFilter(items, lambda x: x % 2 == 0)
    #then
    result = [item for item in my_iter]
    assert result == [2,4,6,8,10]

def test_given_we_have_a_list_when_we_need_to_modify_specifily_the_items_then_the_iterator_give_us_the_list_filtered():
    #given
    items = [1,2,3]
    #when
    my_iter = MyIteratorMap(items, lambda x: x ** 2)
    #then
    result = [item for item in my_iter]
    assert result == [1,4,9]


def test_given_we_have_a_list_when_we_need_a_specific_item_then_the_iterator_give_us_the_item():
    #given
    items = [1,2,3]
    #when
    my_iter = MyIteratorFind(items, 1)
    #then
    result = [item for item in my_iter]
    assert result == [1]
