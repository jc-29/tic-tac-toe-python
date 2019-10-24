def check_win(x_coordinate, y_coordinate, game_state, count, current_player):

    if count >= 3:

        # horizontal check
        if game_state[y_coordinate][0] == game_state[y_coordinate][1] and game_state[y_coordinate][0] == game_state[y_coordinate][2] and game_state[y_coordinate][0] == current_player:
            # print('horizontal win')
            return True
        
        # vertical check
        elif game_state[0][x_coordinate] == game_state[1][x_coordinate] and game_state[0][x_coordinate] == game_state[2][x_coordinate] and game_state[0][x_coordinate] == current_player:
            # print('vertical win')
            return True

        # diagonal check left to right
        elif game_state[0][0] == game_state[1][1] and game_state[0][0] == game_state[2][2] and game_state[0][0] == current_player:
            # print('diagonal win')
            return True

        # diagonal check right to left
        elif game_state[2][0] == game_state[1][1] and game_state[2][0] == game_state[0][2] and game_state[2][0] == current_player:
            # print('diagonal win')
            return True
    
        #draw
        elif count == 9:
            return 'DRAW!'

        else: 
            return False






# Starting variables---------------------------------------------
current_player = "X"
game_state= [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]
game_win = False
count = 0
# --------------------------------------------------------

while not game_win:

# For Player X-------------------------------------------
    if current_player == 'X':
        space_taken_x = True
        while space_taken_x:
            print('''Player X
=========
Put in your X coordinate (0-2):''')
            player1_x_coordinate = int(input())
            print('Put in your Y coordinate (0-2):')
            player1_y_coordinate = int(input())
            
            if game_state[player1_y_coordinate][player1_x_coordinate] == "-":
                game_state[player1_y_coordinate][player1_x_coordinate] = current_player
                space_taken_x=False
            else: 
                print('That space is taken')

            count += 1

        if check_win(player1_x_coordinate, player1_y_coordinate, game_state, count, current_player) == 'DRAW!':
            game_win = True
            print('DRAW!')
        elif check_win(player1_x_coordinate, player1_y_coordinate, game_state, count, current_player):
            game_win= True
            print('Player X Wins!')
        else:     
            current_player = 'O'

        for row in game_state:
                print(row)
            
# For Player O-------------------------------------------------------------

    if current_player == 'O':

        space_taken_o = True
        while space_taken_o:
            print('''Player O
=========
Put in your X coordinate (0-2):''')
            player2_x_coordinate = int(input())
            print('Put in your Y coordinate (0-2):')
            player2_y_coordinate = int(input())
            
            if game_state[player2_y_coordinate][player2_x_coordinate] == "-":
                game_state[player2_y_coordinate][player2_x_coordinate] = current_player
                space_taken_o = False
            else: 
                print('This space is taken')
        
        count += 1

        if check_win(player2_x_coordinate, player2_y_coordinate, game_state, count, current_player) == 'DRAW!':
            game_win= True
            print('DRAW!')
        elif check_win(player2_x_coordinate, player2_y_coordinate, game_state, count, current_player):
            game_win= True
            print('Player O Wins!')

            
        else:           
            current_player = 'X'
        for row in game_state:
            print(row)
#-------------------------------------------------------------------------




