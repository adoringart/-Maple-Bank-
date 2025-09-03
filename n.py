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


print('Welcome to Maple bank!\nPlease select an option below:\n1.Deposit\n2.Withdraw\n3.Check balance\n4.Apply interest\n5.Exit')
print('kindly only provide the numerical representation.')


bank = Bank()
name=input('name: ')
while True:
    choice = input('menu: ').lower()
    if choice == '1':
        bank.create_account(name)
        no = input('enter deposit: ')
        try:
            y = re.search(r'(\d+\.?\d*)', no)
            n = float(y.group(1))
            if n>0:
                f = bank.dep(n)
            else:
                print('only deposit positive sums.')
        except AttributeError:
            print('please provid valid data.')

    elif choice == '2':
        bank.create_account(name)
        wo = input('withdrawal amount: ')
        try:
            k = re.search(r'(\d+\.?\d*)', wo)
            w = float(k.group(1))
            if w<bank._balance:
                f = bank.withdraw(w)
            else:
                raise ValueError('withdrawal amount too high for current balance.')
        except AttributeError:
            print('please provid valid data.')
    elif choice == '3':
        bank.create_account(name)
        print(bank._balance)

    elif choice == '4':
        bank.create_account(name)
        data = input('give principal,rate and time: ')
        try:
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
        except AttributeError:
            print('please provide valid data.')

    elif choice == '5':
        sys.exit('have a great day!')

    else:
        print('invalid input.')
        break
