#SLOT MACHINE GAME

import random #ADDS RANDOM TO THE PROGRAM
import time   #ADDS TIME TO THE GAME

def main():
 
    def cash_ver(cash,bet):
        """Checks if player bet is not more than what they have"""
        if bet > cash:
            return False
        else:
            return True

    def restart_game(restart):
        """Checks if player wants to restart the game"""
        if restart == "y":
            return True
        else:
            exit()
        
    #GAME VARIABLES
    valid_input = False       #PLAYER ABLE TO BET
    shapes = ["〇","□","△"]   #LIST OF SHAPES USED IN SLOTS
    cash = 0                  #PLAYER CASH
    roll_time = 0             #USED FOR TIMER LOOP
    game = True               #GAME LOOP

    #PLAYER STATS
    spins_played = 0  #NUMBER OF ROUNDS PLAYED BY THE PLAYER
    cash_earned = 0   #CASH EARNED BY THE PLAYER
    cash_lost = 0     #CASH LOST BY THE PLAYER

    #LEADER BOARD
    player_scores = {} #PLAYER NAMES AND THERE SCORE WILL BE STORED AS DICTIONARY
    
    #GAME LOOP
    while game == True:
        #RESETS GAME STATS FOR NEW PLAYERS
        cash += 100 
        spins_played = 0
        cash_earned = 0
        cash_lost = 0
        
        #CHECKS IF PLAYER WANTS TO READ RULES
        rules = input("Would you like to read the rules(y/n)?: ").lower()#CONVERTS PLAYER INPUT TO LOWER CASE

        if rules == "y":
            game_rules = open("how_to_play.txt","r")#OPENS TEXT FILE IN READ 
            print(game_rules.read())#READS TEXT FILE
            
            game_rules.close()#CLOSES TEXT FILE 
        else:
            pass
        
        name = input("Enter your name: ").title() #CAPITALIZE FIRST LETTER
        print(name,"You have £",cash)

        #GAME BOARD VISUAL
        print("    |   |    ")
        print("---------------")
        print("  - | - | -")
        print("---------------")
        print("    |   |    ")

        #CHECKS IF PLAYER IS NOT OUT OF MONEY
        while not cash <= 0: 
            #RANDOMLY GENERATES THE SHAPE FOR EACH SLOT
            slot_1 = random.choice(shapes) #GENERATES RANDOM SHAPE FOR SLOT 1
            slot_2 = random.choice(shapes) #GENERATES RANDOM SHAPE FOR SLOT 2
            slot_3 = random.choice(shapes) #GENERATES RANDOM SHAPE FOR SLOT 3

            #THIS WHILE LOOP CHECKS IF MONEY INPUT NOT IS A VALID AMOUNT
            #LOOP WILL CONTINUE IF FALSE
            while valid_input == False:
                #CHECKS THAT WHAT PLAYER ENTERED IS A VALID AMOUNT
                #E.G NOT LETTER
                try:
                    bet = int(input("\nHow much do you want to bet: £"))#PLAYER BET,INTERGER INPUT
                except:
                    print("Invalid amount, try a whole number.")
                    continue

                verification = cash_ver(cash,bet) #VERIFICATION BET FUNCTION 

                if verification == True:
                    break #BREAKS OF LOOP
                else:
                    print("Not enough cash, try a differnt amount")
                #print(cash_ver(cash,bet))

            cash -= bet
            
            print("\nroling",end="")
            #WHILE LOOP FOR DOT ANIMATION
            for x in range(3):
                time.sleep(0.5) #ADDS HALF A SECOUND DELAY
                print(".",end="")

            time.sleep(0.5)#ADDS HALF A SECOUND DELAY
            #GAME BOARD PRACTICAL
            print("")
            print("    |   |    ")
            print("---------------")
            print(" ",slot_1,"|",slot_2,"|",slot_3) #SHOWS PLAYER SHAPES THEY GOT 
            print("---------------")
            print("    |   |    ")

            #WINNING CONDITIONS 
            if slot_1 == "〇" and slot_2 == "〇" and slot_3 == "〇": 
                time.sleep(0.8) #ADDS A DELAY
                print("winner!!!")
                earnings = bet * 2 #DOUBLES BET 
                cash += earnings #ADDS CASH EARNED TO PLAYER CASH
                print("You have £",cash)

                spins_played += 1 #ADDS ONE TO GAMES PLAYED FOR STATS
                cash_earned += bet #ADDS CASH EARNED FOR STATS
 
            elif slot_1 == "□" and slot_2 == "□" and slot_3 == "□":
                time.sleep(0.8) #ADDS A DELAY
                print("winner!!!")
                earnings = bet * 2 #DOUBLES BET 
                cash += earnings #ADDS CASH EARNED TO PLAYER CASH
                print("You have £",cash)

                spins_played += 1 #ADDS ONE TO GAMES PLAYED FOR STATS
                cash_earned += bet #ADDS CASH EARNED FOR STATS
                
            elif slot_1 == "△" and slot_2 == "△" and slot_3 == "△":
                time.sleep(0.8) #ADDS A DELAY
                print("winner!!!")
                earnings = bet * 2 #DOUBLES BET 
                cash += earnings #ADDS CASH EARNED TO PLAYER CASH
                print("You have £",cash)

                spins_played += 1 #ADDS ONE TO GAMES PLAYED FOR STATS
                cash_earned += bet #ADDS CASH EARNED FOR STATS
                
            #LOOSING CONDITION 
            else:
                time.sleep(0.2) #ADDS A DELAY
                print("You didn't win this time.")
                
                print("You have £",cash)

                spins_played += 1 #ADDS ONE TO GAMES PLAYED FOR STATS
                cash_earned += 0  #ADDS CASH EARNED FOR STATS
                cash_lost -= bet  #ADDS CASH LOST FOR STATS

        player_scores[name]=cash_earned #ADDS PLAYER NAME AND THEIR SCORE TO DICIONARY

        time.sleep(1) #ADDS A DELAY
        print("\nSorry, you're out of money.")
        stats = input("Would you like to see your game stats?(y/n): ").lower()#CONVERTS PLAYER INPUT TO LOWER CASE

        if stats == "y": #IF PLAYER TYPES "y" STATS ARE SHOWN
            print("\n-----------------------------")
            print("Game Stats\n")
            print("Total Spins played:",spins_played)
            print("Total cash earned: £",cash_earned)
            print("Total cash lost: £",cash_lost)
            print("-----------------------------")

            print("\nPlayer Scores")
            print("--------------")

            #PRINTS PLAYER AND SCORE IN A LIST 
            for x in player_scores:
                print(x,":",player_scores[x])#PRINTS PLAYER NAME NEXT TO SCORE
            
            time.sleep(1) #ADDS A DELAY
            restart = input("\nwould you like to play again?(y/n):").lower()#CONVERTS PLAYER INPUT TO LOWER CASE

            restart_game(restart) #PLAYER INPUT IS RUN THOUGH THE "RESTART_GAME" FUNCTION 

        else:
            restart = input("would you like to play again?(y/n):").lower()#CONVERTS PLAYER INPUT TO LOWER CASE

            restart_game(restart) #PLAYER INPUT IS RUN THOUGH THE "RESTART_GAME" FUNCTION 

main()
