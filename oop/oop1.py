# Enkapsulacja (kapsułkowanie)
# Information/data hiding

class Account:
    def __init__(self, balance):
        self.__balance = balance

    # setter (mutator)
    def set_balance(self, new_balance):
        if type(new_balance) != int or new_balance < 0:
            print("Podano niepoprawną wartość")
        else:
            self.__balance = new_balance

    # getter (accessor)
    def get_balance(self):
        return self.__balance


# a = Account(100)
# print(a.get_balance())
# a.set_balance(350)
# print(a.get_balance())

# Widoczności pól klasy
# Modyfikatorów dostępu (access modifiers)
# publiczne - bez modyfikatora (widoczne wszędzie - parki, ulice)
# chroniony - modyfikator "_" (wstępujesz na własne ryzyko)
# prywatny - modyfikator "__" (wstęp wzbroniony)

# property


class Account:
    def __init__(self, balance):
        self.__balance = balance

    # setter (mutator)
    def set_balance(self, new_balance):
        if type(new_balance) != int or new_balance < 0:
            print("Podano niepoprawną wartość")
        else:
            self.__balance = new_balance

    # getter (accessor)
    def get_balance(self):
        return self.__balance

    balance = property(get_balance, set_balance)


# a = Account(100)
# a.balance = -300
# a.balance = 25
# print(a.balance)


# Alternatywna notacja - przy użyciu dekoratorów
class Account:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if type(new_balance) != int or new_balance < 0:
            print("Podano niepoprawną wartość")
        else:
            self.__balance = new_balance

a = Account(100)
a.balance = -300
a.balance = 25
print(a.balance)
