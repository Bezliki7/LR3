class ElementBaulybaev():

    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    @property
    def name(self):
        return self._name
    
    @property
    def symbol(self):
        return self._symbol
    
    @property
    def number(self):
        return self._number

    def dump(self):
        print(f'name: {self.name} \nsymbol: {self.symbol} \nnumber: {self.number}')
        

object = ElementBaulybaev('Dinar', 'Li', 3)
object.dump()

print(object.name)