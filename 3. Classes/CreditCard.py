
#attributes = data members, fields,
#behaviors = methods

class CreditCard:
    def __init__(self, name, number, limit = 8000, bank = "Python Bank"):
        self.name = name
        self.number = number
        self.bank = bank
        self.balance = 0
        self.limit = limit
    
    def charge(self, amount):
        #not int or not not float
        if not (isinstance(amount, int) or  isinstance(amount, float)) or (amount <= 0):
            print("Charge Denied")
        else:
            self.balance += amount
    
    def pay(self, amount):
        if not (isinstance(amount, int) or  isinstance(amount, float)) or (amount <= 0):
            print("Charge Denied")
        else:
            self.balance -= amount

    def __str__(self):
        info = "Name: " + self.name + "\n"
        info += "Number: " + "XXXX" + self.number[4:] + "\n"
        info += "Bank: " + self.bank + "\n"
        info += "Balance: " + str(self.balance)
        return info

    def __repr__(self):
        return str(self)

card = CreditCard("Kenny", "12345678")
print(card)
card.charge(10000)
print(card)
card.charge(200)
print(card)

card.pay(5000)
print(card)