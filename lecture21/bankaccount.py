class BankAccount:
    total_accounts = 0
    def __init__(self, name, balance=0):
        self.__name = name
        self.__balance = balance
        self.__account_id = BankAccount.total_accounts
        BankAccount.total_accounts += 1

    def __str__(self):
        return (f"Account id: {self.__account_id} "
                f"{self.__name}'s account balance is {self.__balance}")

    def deposit(self, amount):
        self.__balance = self.__balance + amount
    
    def withdraw(self, amount):
        self.__balance = self.__balance - amount
    
    def merge(self, another):
        self.__balance += another.__balance
        self.__name = self.__name + ' and ' + another.__name
        another.__balance = 0


if __name__ == '__main__':
    my_account = BankAccount('Charlotte', 100)
    print(my_account)
    other_account = BankAccount('Cali')
    other_account.deposit(50)
    print(other_account)

    my_account.merge(other_account)
    print(my_account)
    print(other_account)

    # print('Total accounts:', BankAccount.total_accounts)
    # BankAccount('Someone')
    # BankAccount('Someone')
    # BankAccount('Someone')
    # print('Total accounts:', BankAccount.total_accounts)
    # another_account = BankAccount('Someone else')
    # print(another_account)

    # deposit = float(input('Charlotte, how much would you like to deposit? '))
    # my_account.deposit(deposit)
    # print(my_account)