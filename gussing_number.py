# For run this game, you should run this in terminal and give Two number for list(first number and last number) after the __name__
# For example :- python gussing_number 1 10 (1=for staring number and 10= for last number of list)
#              -------------------------------

import random
import sys


if __name__ == '__main__':
    def check(x,y):
        #genrate random number       
        random_num = random.randint(x,y)
        new_list = list(range(x,y+1))
        
        while True:
            try:
                num = int(input(f"Enter the number between {x} and {y} :-  "))
                if num in  new_list : #For check num are exit in list
                    if int(num) == random_num:
                        print( "Congratulations! You won the game")
                        break                                    
                else:
                    print('** Please Enter the number in range **')
            except ValueError:
                print('Enter a valid number')  
           
 
check(int(sys.argv[1]),int(sys.argv[2]))
#sys.argv[1] for you enter first number after __name__ in terminal.
#sys.argv[2] for you enter second number after sys.argv[1]


