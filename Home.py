class Bank:
    def __init__(self, money, name):
        self.__money = money
        self.__name = name

    def setmoney(self, money):
        self.__money = money

    def getmoney(self):
        return self.__money

    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    def moneyX(self):
        user = input('Внесите деньги:')
        return f'Ваш счет:{self.getmoney() + int(user)}'

    def _kill(self):
        return f'Вы успешно обнулили счет \nВаш счет:{self.getmoney() - self.getmoney()}'

    def __jackpot(self):
        return f'Вы лаки мен и получаете x10 \nВаш счет:{self.__money * 10}'

h1 = Bank('666','Optima')
h1.setname('Sultan')
print(f'Ваше имя:{h1.getname()} \nВаши деньги:{h1.getmoney()}')
print(h1.moneyX())
print(h1._kill())
print(h1._Bank__jackpot())