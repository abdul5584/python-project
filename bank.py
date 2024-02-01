balance=0
def deposit():
    global balance
    amt=int(input('enter amount:'))
    balance=balance+amt
def withdraw():
    global balance
    amt=int(input('enter amount:'))
    balance=balance-amt
def balacheck():
    global balance
    print('available balance',balance)
def menu():
    ch=0
    while(ch!=4):
        print('1.deposit\n2.withdraw\n3.balance\n4.Exit')
        ch=int(input('enter your choice :'))
        if ch==1:
            deposit()
        elif ch==2:
            withdraw()
        elif ch==3:
            balacheck()
from colorama import Fore,Back,Style
def welcome():
    print(Fore.RED,'welcome to MGC Bank')
    pin=int(input(  'enter your ATM pin:'))
    if pin==123:
        menu()
    else:
        print('invalid pin number')
        welcome()
welcome()