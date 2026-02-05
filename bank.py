money = 100
transactions_list = []
class Items:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
def load():
    print(f"Your money: {money}.")
    print("type t for transactions, d for deposit, g to get money) ), b to buy, q for quit")
def deposit(amount):
    global money
    money += amount
    print(f"Deposited {amount}. New balance: {money}.")
def get_money(amount):
    global money
    money += amount
    print(f"Got {amount}. New balance: {money}.")
def buy(Item):
    global money
    if money >= Item.cost:
        transactions_list.append(f"Bought {Item.name} for {Item.cost}")
        money -= Item.cost
        print(f"Bought {Item.name} for {Item.cost}. New balance: {money}.")
    else:
        print(f"Not enough money to buy {Item.name}. Current balance: {money}.")
def transactions():
    print("Transaction history:")
    for transaction in transactions_list:
        print(transaction)
def main():
    load()
    while True:
        command = input("Enter command: ")
        if command == 'd':
            amount = int(input("Enter amount to deposit: "))
            deposit(amount)
        elif command == 'g':
            amount = int(input("Enter amount to get: "))
            get_money(amount)
        elif command == 'b':
            name = input("Enter item name: ")
            cost = int(input("Enter item cost: "))
            item = Items(name, cost)
            buy(item)
        elif command == 't':
            transactions()
        elif command == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid command.")
if __name__ == "__main__":
    main()