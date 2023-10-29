
#Complete the following class
'''
The VendingMachine class constructor should take one parameter: password
Inside the constructor, add three fields: balance, password, and items.
balance should be initialized to 0, and items should be initialized to an empty list

Add an add_item method for the admin, that takes in a name, price, and password:
-Assume the name is a str, and that price is always a positive int or float
-If the password is incorrect, print the message "Incorrect Password"
-Else, create a new item object with the name and price, and add it to the list of items

Add a purchase_item method for the user, that takes in an index, and pay:
-Assume the index is positive and within range, and that pay is always a positive int or float
-If the pay is not sufficient, return a tuple (None, pay)
-Else, make the transaction by adding the item price to balance and return a tuple (item, change)

The __str__ operator should return a string to display the vending machine detail in the following format:
Vending Machine Balance: (balance)
(item 1) : (price 1)
(item 2) : (price 2)

Hint: Use a for loop to iterate through the items and add the new line character '\n' to each line
'''

#Given
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return self.name + ": " + str(self.price)
    
    def __repr__(self):
        return str(self)


class VendingMachine:
    def __init__(self, password):
        pass



#TEST CODE
my_password = "apple"
wrong_password = "banana"

vm = VendingMachine(my_password)

vm.add_item("Oreos", 1.25, my_password)
vm.add_item("Lays Chips", 1.5, my_password)
vm.add_item("Coca-Cola", 1.75, my_password)
vm.add_item("Cheetos", 1.50, my_password)
vm.add_item("Cheez-its", 1.25, wrong_password) #Incorrect Password
vm.add_item("Water", 1, my_password)
vm.add_item("Oreos", 1.25, my_password)

print("\nBefore:")
print(vm)
'''
Vending Machine Balance: 0
Oreos: 1.25
Lays Chips: 1.5
Coca-Cola: 1.75
Cheetos: 1.5
Water: 1
Oreos: 1.25
'''

print(vm.purchase_item(0, 1)) #(None, 1)
print(vm.purchase_item(0, 1.50)) # (Oreos: 1.25, 0.25)
print(vm.purchase_item(4, 2.50)) # (Water: 1, 1.5)
print(vm.purchase_item(1, 1.50)) # (Lays Chips: 1.5, 0.0)
print(vm.purchase_item(2, 50)) # (Coca-Cola: 1.75, 48.25)

print("\nAfter:")
print(vm) 
'''
Vending Machine Balance: 5.5
Oreos: 1.25
Lays Chips: 1.5
Coca-Cola: 1.75
Cheetos: 1.5
Water: 1
Oreos: 1.25
'''