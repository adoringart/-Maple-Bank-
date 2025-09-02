import sys
import re


class Bank:
    def __init__(self, balance=0):
        self._balance = balance

    def dep(self, d):
        self._balance += d

    def withdraw(self, w):
        self._balance -= w

    def check_balance(self):
        return self._balance

    def amount(self, p, r, t):
        try:
            s = float(p)*float(r)*float(t)
            a = float(s)+float(p)
            self._balance+=s
            return f'interest: {s}, amount: {a}'

        except ValueError:
            print('kindly enter numeric values only.')

    def create_account(self, name):
        return f'account for {name} created.'


print('Welcome to Maple bank!\nPlease select an option below:\n1.Create account\n2.Deposit\n3.Withdraw\n4.Check balance\n5.Apply interest\n6.Exit')
print('kindly only provide the numerical representation.')


bank = Bank()

while True:
    choice = input('menu: ').lower()
    if choice == '1':
        name = input('name: ')
        f = bank.create_account(name)
        print(f)

    elif choice == '2':
        no = input('enter deposit: ')
        y = re.search(r'(\d+\.?\d*)', no)
        n = float(y.group(1))
        f = bank.dep(n)

    elif choice == '3':
        wo = input('withdrawal amount: ')
        k = re.search(r'(\d+\.?\d*)', wo)
        w = float(k.group(1))
        f = bank.withdraw(w)

    elif choice == '4':
        print(bank._balance)

    elif choice == '5':
        data = input('give principal,rate and time: ')
        a = re.search(r'p.+?(\d+\.?\d*?)', data)
        pa = a.group(1)
        p = float(pa)

        b = re.search(r'r.+?(\d+\.?\d*?)', data)

        rob = float(b.group(1))
        r = rob/100

        c = re.search(r't.+?(\d+\.?\d*?)', data)
        ta = c.group(1)
        t = float(ta)

        print(bank.amount(p, r, t))

    elif choice == '6':
        sys.exit()

    else:
        print('invalid input.')
