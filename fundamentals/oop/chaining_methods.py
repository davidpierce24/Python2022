class User:
    def __init__ (self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.name, self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

tim = User("Tim Riggins", "tim@gmail.com")
jim = User("Jimmy Dean", "jim@gmail.com")
john = User("John Wick", "john@gmail.com")

tim.make_deposit(2000).make_deposit(300).make_deposit(4500).make_withdrawal(3000).display_user_balance()

jim.make_deposit(4000).make_deposit(200).make_withdrawal(300).make_withdrawal(200).display_user_balance()

john.make_deposit(40000).make_withdrawal(500).make_withdrawal(300).make_withdrawal(200).display_user_balance()

jim.transfer_money(john, 2000).display_user_balance()

john.display_user_balance()