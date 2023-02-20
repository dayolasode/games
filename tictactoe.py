from os import system


def display_board(*args):
   for row in args:
       print("    |    |    ")       
       print(f" {row[0]}  | {row[1]}  | {row[2]}  ")
       print("    |    |    ")
       print("____ ____ ____\n")




def found_position(choice):

    if choice == 1 and row3[0] == empty_cell:
        found_spot = True

    elif choice == 2 and row3[1] == empty_cell:
        found_spot = True
 
    elif choice == 3 and row3[2] == empty_cell:
        found_spot = True

    elif choice == 4 and row2[0] == empty_cell:
        found_spot = True

    elif choice == 5 and row2[1] == empty_cell:
        found_spot = True

    elif choice == 6 and row2[2] == empty_cell:
        found_spot = True

    elif choice == 7 and row1[0] == empty_cell:
        found_spot = True

    elif choice == 8 and row1[1] == empty_cell:
        found_spot = True

    elif choice == 9 and row1[2] == empty_cell:
        found_spot = True
        
    else:
        found_spot = False


    return found_spot

                 

def choices(player, player_map):

    accepted_vals = range(1,10)
    
    choice = str()


    while not choice.isdigit() or  choice.isdigit() not in accepted_vals or found_position(int(choice)) == False:        
        
        choice = input(f"\nPlayer {player}: which position would you like to place your marker  {player_map[player]}? Choose from 1 to 9:  ")
    
        display_board(sample_row1,sample_row2,sample_row3)
    
        if choice.isdigit() not in accepted_vals:
            print("Sorry, invalid choice! Try again (1-9): ")
            display_board(row1,row2,row3)
            print("\n")

        elif found_position(int(choice)) == False:
            print("*** Spot already taken!. Pick another vacant spot ***")
            print("\n")
            display_board(row1,row2,row3)
            print("\n")
        
        elif choice.isdigit() == False:
            print("Sorry, You have to enter a number!")
            display_board(row1,row2,row3)
            print("\n")
            pass
            
            
    return choice


def keep_playing():
    
    response = ''
    while response not in ['Y', 'N', 'y', 'n']:
        response = input("Would you like to play again? (Y/N)?:  ")
    
    return response.upper()


def play_game(player_map):

    display_board(sample_row1,sample_row2,sample_row3)

    sweep = False
    full_table = False

    while ((sweep == False) and ((' ' in row1) or (' ' in row2) or (' ' in row3)) and full_table != True ):      

    
            for player in list(player_map.keys()): 
                
                
                if (row1[0] == row1[1] == row1[2] and row1[0] != empty_cell ) or (row2[0] == row2[1] == row2[2] and row2[0] != empty_cell  ) or  (row3[0] == row3[1] == row3[2] and row3[0] != empty_cell  ):        
                    sweep = True
                    print("\nThe final board!\n")   
                    display_board(row1,row2,row3)
                    print("\n")
                    break

                
                if (row1[0] == row2[0] == row3[0] and row1[0] != empty_cell ) or (row1[1] == row2[1] == row3[1] and row1[1] != empty_cell) or  (row1[2] == row2[2] == row3[2] and row2[2] != empty_cell):                    
                    sweep = True
                    print("\nThe final board!\n")   
                    display_board(row1,row2,row3)
                    print("\n")
                    break
                
                if (row1[0] == row2[1] == row3[2] and row1[0] != empty_cell ) or (row1[2] == row2[1] == row3[0] and row1[2] != empty_cell ):             
                    sweep = True
                    print("\nThe final board!\n")   
                    display_board(row1,row2,row3)
                    print("\n")
                    break
                
                
                choice_output = choices(player, player_map)

                
                current_player = board_update(player, int(choice_output))

                print("\n")
                print("Board updated!")
                print("     ||       ")
                print("     \/       ")
                print("\n")
                display_board(row1,row2,row3)


                if ((' ' not in row1) and (' ' not in row2) and (' ' not in row3) and (sweep == False)):
                    full_table = True                 
                    break



    if full_table != True:                    
        print(f"Congratulations Player {current_player}. You've won!\n")

    elif full_table == True:
        print("We have a draw.....Well played!")
    
    


def board_update(player, choice_output):
    
    if choice_output == 1 and row3[0] == empty_cell:
        row3[0] = player_map[player]        

    elif choice_output == 2 and row3[1] == empty_cell:
        row3[1] = player_map[player]

    elif choice_output == 3 and row3[2] == empty_cell:
        row3[2] = player_map[player]

    elif choice_output == 4 and row2[0] == empty_cell:
        row2[0] = player_map[player]

    elif choice_output == 5 and row2[1] == empty_cell:
        row2[1] = player_map[player]

    elif choice_output == 6 and row2[2] == empty_cell:
        row2[2] = player_map[player]

    elif choice_output == 7 and row1[0] == empty_cell:
        row1[0] = player_map[player]

    elif choice_output == 8 and row1[1] == empty_cell:
        row1[1] = player_map[player]

    elif choice_output == 9 and row1[2] == empty_cell:
        row1[2] = player_map[player]
        
    
    #display_board(row1,row2,row3)
    #print("\n")
    return player


    


def user_selection(accepted_symbols, selection):
    
    player_symbols_dict = {'1': None, '2': None}

    player_1_marker = ''

    while player_1_marker not in ['X','O', 'x', 'o']:
        player_1_marker = input("\nPlayer 1: Choose your marker. Do you want to be X or O?:  \n")
    
    player_symbols_dict['1'] = player_1_marker.upper()

    selection.remove(player_1_marker.upper())
    
    print("Ok...good choice. Player 1 will use '{}'\n".format(player_symbols_dict['1']))
    player_symbols_dict['2'] = selection.pop()
    print("Player 2, you will be '{}' ".format(player_symbols_dict['2']))
    print("\nLets Play!!")
    

    return player_symbols_dict



# START EXECUTION #
###################

response = 'Y'

while response == 'Y':

    empty_cell = ' '
    accepted_symbols = ['X','O']
    selection = accepted_symbols

    ## == Starting Game Map == ##
    row1 = [empty_cell,empty_cell,empty_cell]
    row2 = [empty_cell,empty_cell,empty_cell]
    row3 = [empty_cell,empty_cell,empty_cell]

    sample_row1 = ['7', '8' , '9']
    sample_row2 = ['4', '5' , '6']
    sample_row3 = ['1', '2' , '3']

    ## WELCOME MSG
    print('#' * 27)
    print('#' * 27)
    print('* Welcome to Tic Tac Toe !*')
    print('#' * 27 )
    print('#' * 27 + '\n')



    print("The board is numbered 1 - 9 like a numberpad similar to the below table: \n")
    display_board(sample_row1,sample_row2,sample_row3)
     
    print('''    
To play, you select the number that matches the position you want to fill

For example: 
    
Putting marker  'X' in postion '9' will appear like this:  

            |    |    
            |    | X  
            |    |    
        ____ ____ ____

            |    |    
            |    |   
            |    |    
        ____ ____ ____

            |    |    
            |    |   
            |    |    
        ____ ____ ____


Putting marker 'O' in position '4' will appear  like this: 

            |    |  
            |    |  X   
        ____ ____ ____

            |    |    
          O |    |   
            |    |    
        ____ ____ ____

            |    |    
            |    |   
            |    |    
        ____ ____ ____


          ''')
    
    
    ## GET PLAYER MAPPINGS
    player_map = user_selection(accepted_symbols, selection)
    
    ## START GAME 


    print("This is the starting board of the game\n")
    display_board(row1,row2,row3)
    print("\nThe numberpad will be displayed before each selection just as a reminder")

    print("\nThe game will start shortly. Godspeed!")
    system('sleep 10')
    system('clear')


    play_game(player_map)

    response = keep_playing()


print("Thanks for playing. Goodbye!")





