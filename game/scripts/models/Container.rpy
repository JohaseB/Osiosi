init python:
    class Container(object):
        def __init__(self, weight_max):
            self.inventory = []
            self.weight_max = weight_max

        def add_item(self, item, amount=1):
            if item.weight * amount > self.weight_max - sum(i.item.weight * i.amount for i in self.inventory):
                return('too heavy')
            else:
                if item in [i.item for i in self.inventory]:  # I can't believe I got this line to work with my first try
                    self.finditem(item).amount += amount   # oh god why
                else:
                    self.inventory.append(InvItem(item, amount))
                return('success')

        def has_item(self, item, amount=1):
            if item in [i.item for i in self.inventory]:
                if self.finditem(item).amount >= amount:
                    return(self.finditem(item).amount)
                else:
                    return(False)
            else:
                return(False)

        def finditem(self, item):
            return(self.inventory[[i.item for i in self.inventory].index(item)])
        
        def remove_item(self, item, amount=1):
            if self.has_item(item):
                self.finditem(item).amount -= amount
                if self.finditem(item).amount <= 0:
                    self.inventory.pop(self.inventory.index(self.finditem(item)))
                    return('gone')
                else:
                    return('more left')
            else:
                return('not found')
