noDataValue = -1

class ElementAbaidullin():
    name = ''
    symbol = ''
    number = noDataValue

    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(f'name: {self.name} \nsymbol: {self.symbol} \nnumber: {self.number}')

        

object = ElementAbaidullin('Ruslan', 'H', 1)
object.dump()

