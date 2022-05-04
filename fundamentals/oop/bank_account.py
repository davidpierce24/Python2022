class BankAccount:

    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        self.balance_list = [{'Balance': balance}]

    def deposit(self, amount):
        self.balance += amount
        self.balance_list.append({'Balance': self.balance})
        return self

    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
        else:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        self.balance_list.append({'Balance': self.balance})
        return self

    def display_account_info(self):
        print(f'Balance: ${self.balance}')
        return self

    def yield_interest(self):
        if(self.int_rate > 0):
            self.balance += (self.int_rate * self.balance)
        self.balance_list.append({'Balance': self.balance})
        return self

    def change(self):
        for item in self.balance_list:
            print('Balance: $'+ str(item['Balance']))



account1 = BankAccount(.01)
account2 = BankAccount(.05, 5000)

account1.deposit(500).deposit(3000).deposit(400).withdraw(300).yield_interest().display_account_info()
account2.deposit(4000).deposit(200).withdraw(300).withdraw(200).withdraw(400).withdraw(200).yield_interest().display_account_info()

account1.change()