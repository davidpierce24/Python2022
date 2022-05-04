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

class User:
    def __init__ (self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def make_deposit(self, amount):
        self.account.balance += amount

    def make_withdrawal(self, amount):
        self.account.balance -= amount

    def display_user_balance(self):
        print(self.name, self.account.balance)

    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount

tim = User("Tim Riggins", "tim@gmail.com")
jim = User("Jimmy Dean", "jim@gmail.com")
john = User("John Wick", "john@gmail.com")

tim.make_deposit(2000)
tim.make_deposit(300)
tim.make_deposit(4500)
tim.make_withdrawal(3000)

tim.display_user_balance()

jim.make_deposit(4000)
jim.make_deposit(200)
jim.make_withdrawal(300)
jim.make_withdrawal(200)

jim.display_user_balance()

john.make_deposit(40000)
john.make_withdrawal(500)
john.make_withdrawal(300)
john.make_withdrawal(200)

john.display_user_balance()

jim.transfer_money(john, 2000)

jim.display_user_balance()
john.display_user_balance()

# account1 = BankAccount(.01)
# account2 = BankAccount(.05, 5000)

# account1.deposit(500).deposit(3000).deposit(400).withdraw(300).yield_interest().display_account_info()
# account2.deposit(4000).deposit(200).withdraw(300).withdraw(200).withdraw(400).withdraw(200).yield_interest().display_account_info()

# account1.change()