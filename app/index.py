NO_VALUE = -1

developersInfo = '1st developer: Abaidullin Ruslan \n2nd developer: Abzalov Timur \n3rd developer: Baulybaev Dinar'

class Shape:
    s = NO_VALUE
    h = NO_VALUE

    @staticmethod
    def about():
        print(developersInfo)


Shape.about()