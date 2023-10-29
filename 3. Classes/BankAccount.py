
#Complete the following class
'''
The BankAccount class constructor should take in the following parameters in order:
self, name (str), number (str), bank (str). the bank parameter should default to "Python Bank"

The fields are as followed: self.name, self.number, self.bank, and self.balance, which is default to 0.

The deposit method takes in an amount (assume it will always be integer). 
If the amount is not positive, print("Deposit Failed") 
Else, increase the account balance by the given amount and print("+ $"+amount).

The withdraw method takes in an amount (assume it will always be integer).
If the amount is not positive or is greater than the account balance, print("Withdraw Failed"). 
Else, decrease the account balance by the given amount and print("- $"+amount).

The __str__ operator should return a string to display the account detail in the following format:
Name: (account owner's name)
Number: (account number)
Bank: Python Bank
Balance: (account balance)
'''

class BankAccount:
    def __init__(self):
        pass

    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        return str(self)


#TEST CODE
account1 = BankAccount("Kenny", "12345678")

print(account1) 
'''
Name: Kenny
Number: 12345678
Bank: Python Bank
Balance: 0
'''

account1.deposit(1000)  # + $1000
account1.withdraw(5000) # Withdraw Failed

account1.deposit(-2000) # Deposit Failed
account1.deposit(5000)  # + $5000
account1.withdraw(750)  # - $750

print(account1)
'''
Name: Kenny
Number: 12345678
Bank: Python Bank
Balance: 5250
'''

