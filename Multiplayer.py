from random import randint
from graphics import *
from sys import exit
while True:
    player1 = {"name" : "Player 1", "wins" : 0,"lose" : 0}
    player2 = {"name" : "Player 2", "wins" : 0,"lose" : 0}
    board1 = []
    board2 = []
    total_turns = 0
    changeWin = 0
    boardSize = 5
    gameTurns = 6

    turns = int(input("Enter number of turns: "))
                           
    def color_red(x,y,win):
        if (x == 0):
            point1 = Point(x,y * 100)
            point2 = Point(100,100 * (y + 1))
            r = Rectangle(point1, point2)
            r.setFill('red')
            r.draw(win)
        elif (y == 0):
            point1 = Point(x * 100,y)
            point2 = Point(100 * (x + 1),100)
            r = Rectangle(point1, point2)
            r.setFill('red')
            r.draw(win)
        else:
            point1 = Point(x * 100,y * 100)
            point2 = Point((x + 1) * 100,(y + 1) * 100)
            r = Rectangle(point1, point2)
            r.setFill('red')
            r.draw(win)

    def color_green(x,y,win):
        if (x == 0):
            point1 = Point(x,y * 100)
            point2 = Point(100,100 * (y + 1))
            r = Rectangle(point1, point2)
            r.setFill('green')
            r.draw(win)
        elif (y == 0):
            point1 = Point(x * 100,y)
            point2 = Point(100 * (x + 1),100)
            r = Rectangle(point1, point2)
            r.setFill('green')
            r.draw(win)
        else:
            point1 = Point(x * 100,y * 100)
            point2 = Point((x + 1) * 100,(y + 1) * 100)
            r = Rectangle(point1, point2)
            r.setFill('green')
            r.draw(win)
    def calc_choords(value):
        if (value <= 100):
                return 0
        elif (value <= 200 and value > 100):
                return 1
        elif (value <= 300 and value > 200):
                return 2
        elif (value <= 400 and value > 300):
                return 3
        elif (value <= 500 and value > 400):
                return 4
    def choose_turn():
        if total_turns % 2 == 0:
            print ("player1")
            return player1
        else:
            print ("player2")
            return player2
    def play_again():
        play_again = (x <= 350 and x >= 150 and y <= 400 and y >= 300)
        if play_again == 1:
            total_turns = 0
            ship_points = set_game(board1,board2)
        elif play_again == 0:
            exit()
    def set_game(board1,board2):

        row1 = random_row()
        row2 = random_row()
        column1 = random_column()
        column2 = random_column()
        print (row1, row2, column1, column2)
        return {"row1": row1, "row2":row2,"column1":column1,"column2":column2}
    def random_row():
        return randint(0,boardSize - 1)
    def random_column():
        return randint(0,boardSize - 1)

    #-------------DRAW----------------
    print ("Let's Play")
    xcoor = 100

    #Build Player 1 Board-----------------------------
    win1 = GraphWin("Battle Ship Player 1 Board", 500, 500)
    win1.setBackground('blue')

    #Vertical Lines
    line2 = Line(Point(xcoor,0), Point(xcoor,500))
    line3 = Line(Point(2 * xcoor,0), Point(2 * xcoor,500))
    line4 = Line(Point(3 * xcoor,0), Point(3 * xcoor,500))
    line5 = Line(Point(4 * xcoor,0), Point(4 * xcoor,500))

    line2.draw(win1)
    line3.draw(win1)
    line4.draw(win1)
    line5.draw(win1)

    #Horizontal Lines
    line1 = Line(Point(0,xcoor), Point(500,xcoor))
    line6 = Line(Point(0,xcoor * 2), Point(500,xcoor * 2))
    line7 = Line(Point(0,xcoor * 3), Point(500,xcoor * 3))
    line8 = Line(Point(0,xcoor * 4), Point(500,xcoor * 4))

    line1.draw(win1)
    line6.draw(win1)
    line7.draw(win1)
    line8.draw(win1)

    #Build Player 2 Board-----------------------------
    win2 = GraphWin("Battle Ship Player 2 Board", 500, 500)
    win2.setBackground('blue')
    #Vertical Lines
    line2 = Line(Point(xcoor,0), Point(xcoor,500))
    line3 = Line(Point(2 * xcoor,0), Point(2 * xcoor,500))
    line4 = Line(Point(3 * xcoor,0), Point(3 * xcoor,500))
    line5 = Line(Point(4 * xcoor,0), Point(4 * xcoor,500))

    line2.draw(win2)
    line3.draw(win2)
    line4.draw(win2)
    line5.draw(win2)

    #Horizontal Lines
    line1 = Line(Point(0,xcoor), Point(500,xcoor))
    line6 = Line(Point(0,xcoor * 2), Point(500,xcoor * 2))
    line7 = Line(Point(0,xcoor * 3), Point(500,xcoor * 3))
    line8 = Line(Point(0,xcoor * 4), Point(500,xcoor * 4))

    line1.draw(win2)
    line6.draw(win2)
    line7.draw(win2)
    line8.draw(win2)
    #-----------------------------------------------------------


    ship_points = set_game(board1,board2)



   
        
    
    for turns in range(turns*2):  # 6 turns total = 3 turns for each player
        total_turns += 1
       

        #-----------------------------set up--------------------
        global win_state_change
        global over
        over = 0
        guess_col = 0
        guess_row = 0

        ship_row1 = ship_points["row1"]
        ship_col1 = ship_points["column1"]
        ship_row2 = ship_points["row2"]
        ship_col2 = ship_points["column2"]

        
        
        if (choose_turn() == player1):
           #Player 2 Guess
            point1 = win1.getMouse()
            print ("board 1 row" + str(point1.getX()))
            print ("board 1 col" + str(point1.getY()))
           
            guess_row1 = calc_choords(point1.getX())
            guess_col1 = calc_choords(point1.getY())

            #Player 2 Check (2 guessing on board 1)
            match1 = guess_row1 == ship_row1  and guess_col1 == ship_col1
            print ("board 1 guessed " + str(match1))

            if match1:
                over = 1
                win_state_change = 1  # notes that someone has won the current game
                player1["wins"] += 1
                print ("Congratulations! You sunk my battleship!")
                color_green(guess_row1,guess_col1,win1)

            elif not match1:  # check the current player to then correlate with the correct board size

                print ("You missed my battleship!")
                color_red(guess_row1,guess_col1, win1)
                win_state_change = 0
        else:
            #Player 1 Guess
            point2 = win2.getMouse()
            print ("board 2 row" + str(point2.getX()))
            print ("board2 col" + str(point2.getY()))
           
            guess_row2 = calc_choords(point2.getX())
            guess_col2 = calc_choords(point2.getY())

            #Player 1 Check (1 guessing on board 2)
            match2 = guess_row2 == ship_row2 and guess_col2 == ship_col2
            print ("board 2 guessed " + str(match2))

            if match2:
                over = 1
                win_state_change = 1  # notes that someone has won the current game
                player2["wins"] += 1
                print ("Congratulations! You sunk my battleship!")
                color_green(guess_row2,guess_col2,win2)

            elif not match2:  # check the current player to then correlate with the correct board size

                print ("You missed my battleship!")
                color_red(guess_row2,guess_col2,win2)
                win_state_change = 0

    win1.close()
    win2.close()
                
    exit()



