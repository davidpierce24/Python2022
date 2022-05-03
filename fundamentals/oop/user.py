class User:
    def __init__ (self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(self.name, self.account_balance)

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

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