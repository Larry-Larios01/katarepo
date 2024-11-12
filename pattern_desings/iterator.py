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
    


    
    
