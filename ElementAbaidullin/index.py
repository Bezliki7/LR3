class ElementAbaidullin():
    def __init__(self, name, symbol, number):
        self._name = name
        self._symbol = symbol
        self._number = number
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(f'name: {self._name} \nsymbol: {self._symbol} \nnumber: {self._number}')

object = ElementAbaidullin('Ruslan', 'H', 1)
object.dump()

print(object.name)

