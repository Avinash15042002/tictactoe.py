gameon = True
while gameon:
    print('Hello! welcome to the game')
    ref = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    def display_board(ref):
        row3 = print(f' {ref[1]} |  {ref[2]}  | {ref[3]} '.format())
        row3 = print('-------------')
        row3 = print(f' {ref[4]} |  {ref[5]}  | {ref[6]} '.format())
        row4 = print('-------------')
        row5 = print(f' {ref[7]} |  {ref[8]}  | {ref[9]} '.format())

    def symbol_select():
        symbol = 'wrong'
        while symbol not in ['X','O']:
            symbol = input(('which symbol you wanna play? X or O : '))
            if symbol not in ['X','O']:
                print('please enter a valid input')
        return symbol


    def position_select(ref,symbol):
        position = 'wrong'
        while position not in [1,2,3,4,5,6,7,8,9]:
            position = int(input('enter position : '))
            if position not in [1,2,3,4,5,6,7,8,9]:
                print('please enter a valid input')
        return position

    def turn_change(symbol):
        if symbol == 'X':
            return 'O'
        else:
            return 'X'

    def place_marker(ref,symbol,position):
        ref[position] = symbol
        display_board(ref)

    def win_check(ref,symbol):
        if ref[1] == ref[2] == ref[3] == symbol:
            print(ref[1], 'is won!')
            return True
        elif ref[4] == ref[5] == ref[6] == symbol:
            print(ref[4], 'is won!')
            return True
        elif ref[7] == ref[8] == ref[9] == symbol:
            print(ref[7], 'is won!')
            return True
        elif ref[1] == ref[4] == ref[7] == symbol:
            print(ref[1], 'is won!')
            return True
        elif ref[2] == ref[5] == ref[8] == symbol:
            print(ref[2], 'is won!')
            return True
        elif ref[3] == ref[6] == ref[9] == symbol:
            print(ref[3], 'is won!')
            return True
        elif ref[1] == ref[5] == ref[9] == symbol:
            print(ref[1], 'is won!')
            return True
        elif ref[3] == ref[5] == ref[7] == symbol:
            print(ref[3], 'is won!')
            return True
        
    def tie_check(ref):
        for i in ref:
            if ' ' not in ref:
                return True
        return False
    
    def replay():
        re = 'wrong'
        while re not in ['Y','N']:
            re = input('Play Again? Y or N : ')
        return re
        
    print('Here is the board')
    display_board(ref)
    symbol = symbol_select()
   
    while gameon:
            position = position_select(ref,symbol)
            while ref[position] != ' ':
                position = int(input('please enter a empty position : '))
            place_marker(ref,symbol,position)
            turn_change(symbol)
            if win_check(ref,symbol):
                print('game end')
                break
                

            elif tie_check(ref):
                print('TIE')
                break
            else:
                pass
            symbol = turn_change(symbol)
            print(symbol,"'s turn")   
    re = replay() 
    if re == 'N':
            gameon=False
    else:
        pass
           
    