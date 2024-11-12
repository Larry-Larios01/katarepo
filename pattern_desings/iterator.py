import random



class MyIterator_Reverse:
    def __init__(self, items):
        self.items = items
        self.index = len(items)-1

    def __iter__(self):
        return self  

    def __next__(self):
        if self.index < 0:
            raise StopIteration  
        item = self.items[self.index]
        self.index += -1
        return item

class MyIterator_Random:
    def __init__(self, items):
        self.items = items
        self.indexs = random.sample(items, len(items))
        self.actual_index = 0

    def __iter__(self):
        return self  

    def __next__(self):
        if self.actual_index >= len(self.items):
            raise StopIteration  
        item = self.indexs[self.actual_index]
        self.actual_index+= 1
        return item
    


class MyIterator_Filter:
    def __init__(self, items, func):
        self.items = items
        self.func = func
        self.index = 0

    def __iter__(self):
        return self  

    def __next__(self):
        while self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            if self.func(item):
                return item
                
        raise StopIteration
    
class MyIterator_Map:
    def __init__(self, items, func):
        self.items = items
        self.func = func
        self.index = 0

    def __iter__(self):
        return self  

    def __next__(self):
        while self.index < len(self.items):
            item = self.items[self.index]
            self.index += 1
            item_final= self.func(item)
            return item_final
                
                
        raise StopIteration


class MyIterator_Find:
    def __init__(self, items, item):
        self.items = items
        self.item_final = item
        self.index = 0

    def __iter__(self):
        return self  

    def __next__(self):
        if self.item_final in self.items:

            while self.index < len(self.items):
                item = self.items[self.index]
                self.index += 1
                if item == self.item_final: 
                    return item
                
                
        raise StopIteration


       


    
