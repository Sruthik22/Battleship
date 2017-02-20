from random import randint
from sys import exit
from graphics import *
while True:
        turns = int(input("How many turns would you like? "))
        board = []

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
        def play_again(x,y):
                return (x <= 350 and x >= 150 and y <= 400 and y >= 300)                       
        def color_red(x,y):
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

        def color_green(x,y):
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
                
        def random_row():
            return randint(0,4)
        def random_column():
            return randint(0,4)
        row = random_row()
        column = random_column()
        print (row)
        print (column)
        gameover = False
        gamewon = False
        i = int(0)
        xcoor = 100
        win2 = GraphWin("User Interface", 500, 500)
        win = GraphWin("Battle Ship Board", 500, 500)
        win.setBackground('blue')
        #Vertical Lines
        line2 = Line(Point(xcoor,0), Point(xcoor,500))
        line3 = Line(Point(2 * xcoor,0), Point(2 * xcoor,500))
        line4 = Line(Point(3 * xcoor,0), Point(3 * xcoor,500))
        line5 = Line(Point(4 * xcoor,0), Point(4 * xcoor,500))

        line2.draw(win)
        line3.draw(win)
        line4.draw(win)
        line5.draw(win)

        #Horizontal Lines
        line1 = Line(Point(0,xcoor), Point(500,xcoor))
        line6 = Line(Point(0,xcoor * 2), Point(500,xcoor * 2))
        line7 = Line(Point(0,xcoor * 3), Point(500,xcoor * 3))
        line8 = Line(Point(0,xcoor * 4), Point(500,xcoor * 4))

        line1.draw(win)
        line6.draw(win)
        line7.draw(win)
        line8.draw(win)

        anchorpoint = Point(250,100)
        s = Text(anchorpoint,"You have " + str(turns) + " turns left")
        s.setSize(36)
        s.setFace('helvetica')
        s.setTextColor('blue') 
        s.draw(win2)
        
        for j in range(turns):
                if i == turns:
                        break
                
                
                
                
                point = win.getMouse()
                print (point.getX())
                print (point.getY())

                
                guess_row = calc_choords(point.getX())
                guess_column = calc_choords(point.getY())

                print (guess_row)
                print (guess_column)
                
                while guess_column > (4) or guess_column < 0 or guess_row > (4) or guess_row < 0:
                    print ("Guess again the board size is only: " + str(4))
                    print ("You have " + str(turns - i - 1) + " turns left.")
                    s.undraw()
                    s = Text(anchorpoint,"You have " + str(turns - i - 1) + " turns left")
                    s.setSize(36)
                    s.setFace('helvetica')
                    s.setTextColor('blue') 
                    s.draw(win2)
                    guess_row = int(input("row: "))
                    guess_column = int(input("column: "))
                    i += 1
                    if turns - i - 1 == 0:
                        gameover = True
                        break
                if guess_row == row and guess_column == column:
                    print ("HIT!")
                    color_green(guess_row,guess_column)
                    gamewon = True
                    break
                else:
                    if gameover == True:
                            break
                    print ("Miss")
                    color_red(guess_row,guess_column)
                    print ("You have " + str(turns - i - 1) + " turns left.")
                    s.undraw()
                    s = Text(anchorpoint,"You have " + str(turns - i - 1) + " turns left")
                    s.setSize(36)
                    s.setFace('helvetica')
                    s.setTextColor('blue') 
                    s.draw(win2)
                    i += 1
        if gamewon == False:            
                print ("You have exceeded the number of turns given to you. GAME OVER")
                s.undraw()
                s = Text(anchorpoint,"YOU LOSE :(")
                s.setSize(36)
                s.setFace('helvetica')
                s.setTextColor('blue') 
                s.draw(win2)

                point1 = Point(150,300)
                point2 = Point(350,400)
                t = Rectangle(point1, point2)
                t.draw(win2)
                anchorpoint2 = Point(250,350)
                p = Text(anchorpoint2,"Play Again")
                p.draw(win2)

                point = win2.getMouse()
                print (point.getX())
                print (point.getY())
                click = play_again(point.getX(),point.getY())
                if click:
                        win.close()
                        win2.close()
                        continue
                else:
                        win.close()
                        win2.close()
                        exit("Exitting the program!")
        if gamewon == True:
                print ("You WON :)")
                s.undraw()
                s = Text(anchorpoint,"YOU WON :)")
                s.setSize(36)
                s.setFace('helvetica')
                s.setTextColor('blue') 
                s.draw(win2)

                point1 = Point(150,300)
                point2 = Point(350,400)
                t = Rectangle(point1, point2)
                t.draw(win2)
                anchorpoint2 = Point(250,350)
                p = Text(anchorpoint2,"Play Again")
                p.draw(win2)

                point = win2.getMouse()
                print (point.getX())
                print (point.getY())
                click = play_again(point.getX(),point.getY())
                if click:
                        win.close()
                        win2.close()
                        continue
                else:
                        win.close()
                        win2.close()
                        exit("Exitting the program!")
        #elif decisions == "rules":
            #print ("")
            #print ("OBJECT OF THE GAME: ")
            #print ("     To sink all of your opponents battle ships")
            #print ("HOW TO PLAY: ")
            #print ("     You will go first by printing your guess of row and column and the game will alert you of whether you hit or missed the ship")
            #print ("     You can only guess a row or column in range of the board size. Otherwise the game will alert you you have not guessed in ")
            #print ("     range and ask you to guess again. If you wish to change the board size go to the options menu.")
            #print ("WHO'S THE WINNER?: ")
            #print ("The first person to sink all the battleships of their opponent wins!")
            #print ("")
