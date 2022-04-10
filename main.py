from random import randint as ri
from colorama import Fore,Back
import colorama
colorama.init()
from os import system
system('cls')

def lshuffle(ilist: list) -> list:
    for i in range( ri(len(ilist), len(ilist)+ri(10,50000)) ):
        r1 = ri(0,len(ilist)-1)
        r2 = ri(0,len(ilist)-1)

        t1 = ilist[r1]
        t2 = ilist[r2]

        ilist[r1] = t2
        ilist[r2] = t1

    return ilist


def main():
    ilist = input(f'{Fore.CYAN}List: {Fore.RESET}')
    ilist = ilist.split(' ')
    ilist = [int(i) for i in ilist]

    olist = []
    for n in ilist:
        olist.append(n)

    attempts = 0
    while True:
        sortedlist = lshuffle(olist)
        attempts+=1

        system('cls')
        print(f'{Fore.CYAN}List: {ilist}{Fore.RESET}')
        print(f'{Fore.RED}{sortedlist}{Fore.RESET}')

        if sortedlist == sorted(ilist):
            done(ilist,sortedlist,attempts)
            

def done(ilist:list,sortedlist:list,attempts:int):
    system('cls')
    print(f'{Fore.CYAN}List: {ilist}{Fore.RESET}')
    print(f'{Fore.GREEN}{sortedlist}{Fore.RESET}')
    print(f'{Fore.GREEN}Attempts: {attempts}{Fore.RESET}')
    main()

        
main()