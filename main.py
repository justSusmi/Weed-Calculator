from colorama import *
def main():

    clear()


                    
    print(f'                                                                                                         \n' +
f'{Fore.CYAN}                  ░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░     \n' +
           f'                  ██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗     \n' +
           f'                  ██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝     \n' +
           f'                  ██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗     \n' +
           f'                  ╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║     \n' +
           f'                  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝     \n' +
           f'                                                                                                         \n' +
           f'                      {Fore.BLUE}[{Fore.CYAN}1{Fore.BLUE}]{Fore.RESET}Profit-Calculator                  \n' +
           f'                      {Fore.BLUE}[{Fore.CYAN}2{Fore.BLUE}]{Fore.RESET}Gram-Calculator                    \n' +
           f'                                                                                                         \n' )  



    choice = input(f'{Fore.BLUE}[{Fore.CYAN}>>>{Fore.BLUE}] {Fore.RESET}Choice: {Fore.BLUE}')
    
    if(choice=='1'):
        clear()
        profit_calculator()
        main()
    if(choice=='2'):
        clear()
        gram_calculator()()
        main()
    else:
      clear()
      input(f'{Fore.BLUE}[{Fore.CYAN}Error{Fore.BLUE}] {Fore.RESET}Choose valid Choice. . . ') 
      main()
   
#-----------------------------------------------------------------------------------------------------------------------------------

def profit_calculator():
    purchase_price = int(input("Purchase Price: "))
    gram_amount = int(input("Gram Amount: "))
    profit_per_gram = int(input("Profit per gram: "))
    number_of_dealers = int(input("How many dealers: "))

    clear()

    gram_per_dealer = gram_amount/number_of_dealers
    profit_per_dealer = gram_per_dealer*profit_per_gram
    profit = profit_per_dealer*number_of_dealers - purchase_price

    print(f'{Fore.BLUE}[{Fore.CYAN}€{Fore.BLUE}]{Fore.RESET}Price per gram(for you): ' + str(purchase_price/gram_amount))
    print(f'{Fore.BLUE}[{Fore.CYAN}€{Fore.BLUE}]{Fore.RESET}Price per gram(for your customers): ' + str((purchase_price/gram_amount)+profit_per_gram))
    print(f'{Fore.BLUE}[{Fore.CYAN}€{Fore.BLUE}]{Fore.RESET}Gram per dealer: ' + str(gram_per_dealer))
    print(f'{Fore.BLUE}[{Fore.CYAN}€{Fore.BLUE}]{Fore.RESET}Profit per dealer: ' + str(profit_per_dealer))
    print(f'{Fore.BLUE}[{Fore.CYAN}€{Fore.BLUE}]{Fore.RESET}Profit from all dealers: ' + str(profit_per_dealer*number_of_dealers))
    input(f'{Fore.BLUE}[{Fore.CYAN}€{Fore.BLUE}]{Fore.RESET}Total profit: ' + str(profit))

#-----------------------------------------------------------------------------------------------------------------------------------

def gram_calculator():
    purchase_price = int(input("Total purchase price: "))
    gram_amount = int(input("Total amount(g): "))

    for x in range(5,21):
      calculation = (((purchase_price/gram_amount)-x)*-1)
      profit = calculation*gram_amount

      if profit < 0:
            profit_or_loose = "Loss"
            space = ""
      else:
            profit_or_loose = "Win"
            space = "  "

      if x < 10:
        space2 = "  "
      else:
        space2 = " "

      print(f'{Fore.BLUE}[{Fore.CYAN}' + str(x) + f'€{Fore.BLUE}]' + space2 + f'{Fore.RESET}' + profit_or_loose + f':   ' + space + str(int(profit)))

    input(f'{Fore.RESET}-----------------------')

#-----------------------------------------------------------------------------------------------------------------------------------

def clear():
   print("\033[H\033[J", end="")

#-----------------------------------------------------------------------------------------------------------------------------------

main()
