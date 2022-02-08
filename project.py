import random      # provides random values
import os          # used to interact with the system and provide lease of automation 
import re          # check if a particular string matches a given regular expression
import turtle      # provides moving turtle that can be controlled using the modules present under python turtle
import time        # gives us control over time in a program like delaying a block of code for some time
#entrance game
print('                                               WELCOME TO AA GAME BOX                     ')
print('')
print('')
print('RULES: ')
print('')
print('TO PLAY THE GAMES YOU FIRST NEED TO WIN A 5 CONCEPTUAL QUESTION QUIZ BY ANSWERING EVERY QUESTION CORRECTLY \nTHEN YOU WILL BE ABLE TO ACCESS ALL THE GAMES!!!!!!!')
print('')
print('Welcome to PYTHON GAME BOX QUIZ')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=5
 
if answer.lower()=='yes':
    answer=input('Question 1: How is a code block indicated in Python? ')
    if answer.lower()=='indentation':
        score += 1
        print('CORRECT ANSWER!!')
        print('')

    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: Which of the following types of loops are not supported in Python?\n (a)While\n (b)For\n (c)do-while\n (d)NOT\n what is the option:  ')
    if answer.lower()=='c':
        score += 1
        print('CORRECT ANSWER!!')
        print('')

    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: Which of the following concepts is not a part of Python?\n (a)Pointers\n (b)Loops\n (c)Dynamic typing\n (d)all of these\n what is the option:  ')
    if answer.lower()=='a':
        score += 1
        print('CORRECT ANSWER!!')
        print('')

    else:
        print('Wrong Answer :(')

    answer=input('Question 4: In which language is Python written?\n (a)c++\n (b)c\n (c)java\n (d)NOT\n what is the option:  ')
    if answer.lower()=='b':
        score += 1
        print('CORRECT ANSWER!!')
        print('')

    else:
        print('Wrong Answer :(')

    answer=input('Question 5: Which of the following are valid string manipulation functions in Python?\n (a)count()\n (b)upper()\n (c)strip()\n (d)all of these\n what is the option:  ')
    if answer.lower()=='d':
        score += 1
        print('CORRECT ANSWER!!')
        print('')

    else:
        print('Wrong Answer:(')
 
print(' You attempted',score,"questions correctly!")
mark=(score/total_questions)*100

print('Marks obtained:',mark)
#user is able to play games only if he scores fully!

if score==5: # chex=cks whether the user has scored full or not
    asd = input('Which game do you want to play: \n press [T] for tic-tac-toe:  \n press [R] for rock paper scissor: \n press [H] for Hacker game:  \n press [X] for Snake game\n Type the corresponding initial:  ')
    # asd variables allows the user to choose from the provided 4 games
    if asd == "T":
        #if the user chooses to play the tic tac toe game the below code snippet will run 
        print('GET READY FOR SOME TIC TAC TOE FUN !!')
        board = [i for i in range(0, 9)]
    # taking input for table in for specified times
        player, computer = '', ''
    # here we design Corners, Center and Others, respectively
        moves = ((1, 7, 3, 9), (5,), (2, 4, 6, 8))
    # Winner combinations
        winners = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    # We create the standard Table for a tic tac toe game 
        tab = range(1, 10)

        def print_board():# def fuction is used so that there is no need of writting the code many times
        #each time the player makes a move anew table has to be created    
        #the function makes the standard table everytime the game is called out    
            x = 1
            for i in board:
                end = ' | '
                if x % 3 == 0:
                    end = ' \n'
                    if i != 1:
                        end += '---------\n'
                char = ' '
                if i in ('X', 'O'):
                    char = i
                x += 1
                print(char, end=end)

        def select_char():# Randomly assigns the user the symbol to play with. Sometimes it can be X or sometimes O
            chars = ('X', 'O')
            if random.randint(0, 1) == 0:
                return chars[::-1]
            return chars

        def can_move(brd, player, move):
            if move in tab and brd[move-1] == move-1:
                return True
            return False

        def can_win(brd, player, move):
            places = []
            x = 0
            for i in brd:
                if i == player:
                    places.append(x)
                x += 1
            win = True
            for tup in winners:
                win = True
                for ix in tup:
                    if brd[ix] != player:
                        win = False
                        break
                if win == True:
                    break
            return win

        def make_move(brd, player, move, undo=False):
            if can_move(brd, player, move):
                brd[move-1] = player
                win = can_win(brd, player, move)
                if undo:
                    brd[move-1] = move-1
                return (True, win)
            return (False, False)
        # AI goes here

        def computer_move():# use of os and re module for automation played by system
            move = -1
            
            for i in range(1, 10):
                if make_move(board, computer, i, True)[1]:
                    # after every move of the player the loop breaks for system to play
                    move = i
                    break
            if move == -1:
                # If player can win system tries to block the player 
                for i in range(1, 10):
                    if make_move(board, player, i, True)[1]:
                        move = i
                        break
            if move == -1:
                # Otherwise, try to take one of desired places.
                for tup in moves:
                    for mv in tup:
                        if move == -1 and can_move(board, computer, mv):
                            move = mv
                            break
            return make_move(board, computer, move)

        def space_exist():
            # count the moves of the player 
            return board.count('X') + board.count('O') != 9

        player, computer = select_char() 
        print('Player is [%s] and computer is [%s]' % (player, computer))# takes random symbol and assign to other
        result = '%%% Deuce ! %%%'
        while space_exist():
            print_board()
            print('#Make your move ! [1-9] : ', end='')
            move = int(input())
            moved, won = make_move(board, player, move)
            if not moved:
                print(' >> Invalid number ! Try again !')
                continue
            #
            if won:
                result = '*** Congratulations ! You won ! ***'
                break
            elif computer_move()[1]:
                result = '=== You lose ! =='
                break
        print_board()
        print(result)


    elif asd == "R":  # check if the user wants to play rock paper scissor 
        print('GET READY FOR SOME ROCK-PAPER-SCISSOR FUN !!')
        os.system('cls' if os.name=='nt' else 'clear') # again the use of os.system to automate 
        isk="y"
        while isk == 'y':# loop to enter or exit the game after each turn 
                print ("\n")
                print ("Rock, Paper, Scissors - Shoot!")
                
                userChoice = input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ")
                # the user choice variable to take user's input
                if not re.match("[SsRrPp]", userChoice):
                # it checks the user input and tries to match it with the defined objects namely ROCK PAPER SCISSOR
                # FOr some undesired input the the below code is printed
                    print ("Please choose a letter:")
                    print ("[R]ock, [S]cissors or [P]aper.")
                    continue
                # Echo the user's choice
                
                print ("You chose: " + userChoice)
                choices = ['R', 'P', 'S']
                opponenetChoice = random.choice(choices)
                print ("I chose: " + opponenetChoice)
                
                
                if opponenetChoice == str.upper(userChoice):
                    print ("Tie! ")
                #if opponenetChoice == str("R") and str.upper(userChoice) == "P"
                
                elif opponenetChoice == 'R' and userChoice.upper() == 'S':      
                    print ("Scissors beats rock, I win! ")
                    continue
                elif opponenetChoice == 'S' and userChoice.upper() == 'P':      
                    print ("Scissors beats paper! I win! ")
                    continue
                    
                elif opponenetChoice == 'P' and userChoice.upper() == 'R':      
                    print ("Paper beat rock, I win! ")
                    continue
                
                else:       
                    print ("You win!")
                isk = input("Press [y] to play [n] to exit after this round:  ")

        
    

    elif asd == 'H':# checks for user's input to run the hacker game 
        
        print("You are a RAW agent attempting to get the confidential information stolen by criminal mastermind Rumen")
        print("                                                                   ")
        input("                 press enter to continue")
        print("                                                                   ")
        print("               YOU HAVE ACCCESS TO HIS COMPUTER ")
        print("                                                                   ")
        print("    YOU HAVE FIVE ATTEMPTS TO CRACK THE CODE AND GAIN ACCESS TO THE SYSTEM    ")

        input("                 press enter to continue")
            
        print ("Welcome to Holland Security System")



        raw = input("Hello Mr Rumen \n Enter the Password:  ")  

        password=raw.lower()    # any input typed will become lower case 
                                # 'lower' is an in-built method 
        attempt=0

        while password != 'bob':    # When password is 'bob' this will break 
            print("Access denied")   # the while loop and then the next line 
            attempt+=1               # of code will play eg: print ("Access granted")
            

            if attempt == 1:
                print(" Tip(It has 3 letters)")

            if attempt == 2:
                print(" Tip(Begins with a 'B')")

            if attempt == 4:
                print(" Tip( Relates to his name)")

            if attempt == 5:
                print("Too many Attempts \n Alarm is OFF")
                input("press enter to quit")
                quit()

            raw = input("Enter the Password ")

            password=raw.lower()     
                
            
        print("Access granted")
            

        input("press enter to exit")
    elif asd=="X":
        delay = 0.1
        score = 0
        high_score = 0


# Complete use of python's turtle module to able to navigate a object over a screen
        # Creating a window screen
        # the following uses a window module in order to form the game window
        # wn. it is a graphics code for turtle module which allows us to create pixelated objects
        
        wn = turtle.Screen() 
        wn.title("Snake Game") # gives the title to screen 
        wn.bgcolor("blue")  
        # sets the color of the screen to blue  
        # the width and height can be put as user's choice
        wn.setup(width=600, height=600)
        wn.tracer(0)

        # head of the snake
        head = turtle.Turtle() # Creates a tutle which acts as the pixelated snake 
        head.shape("square") # here the turtle is square in shape 
        head.color("white") 
        head.penup() # there is no lines formed on the screen while snake is moving
        head.goto(0, 0)  #initial coordinates of the snake 
        head.direction = "Stop" #initially at stop

        # food in the game
        food = turtle.Turtle()   # we have used another turtle just as a food for the snake
        colors = random.choice(['red', 'green', 'black'])
        # food can spawn randomly out of these given colors
        shapes = random.choice(['square', 'triangle', 'circle'])
        #random shapes for food to distinguish it 
        food.speed(0)  # the food will remain stationary 
        food.shape(shapes)  
        #collects the value from the shape variable
        food.color(colors)
        #collects the color from shape module 
        food.penup() 
        # no tracing made by the food while spawning
        food.goto(0, 100) 
        # spawning location of food
        
        # as soon as the snake eats food another turtle joins on its back in order to lengthen the snake 
        pen = turtle.Turtle()  
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 250)
        pen.write("Score : 0 High Score : 0", align="center",
                font=("candara", 24, "bold"))



        # assigning key directions
        def group():
            if head.direction != "down":
                head.direction = "up"


        def godown():
            if head.direction != "up":
                head.direction = "down"


        def goleft():
            if head.direction != "right":
                head.direction = "left"


        def goright():
            if head.direction != "left":
                head.direction = "right"


        def move():
            if head.direction == "up":
                y = head.ycor()  # checks the y coordinate of the turtle 
                head.sety(y+20)
            if head.direction == "down":
                y = head.ycor()
                head.sety(y-20)
            if head.direction == "left":
                x = head.xcor()
                head.setx(x-20)
            if head.direction == "right":
                x = head.xcor()
                head.setx(x+20)
            
            #Checks the x coordinate of the snake 

                
        wn.listen() # asks the sytem to take commands during the play 
        wn.onkeypress(group, "w")  #use of w key to move forward 
        wn.onkeypress(godown, "s")  #use of s key to move backward 
        wn.onkeypress(goleft, "a")   #use of a key to move right 
        wn.onkeypress(goright, "d")   #use of d key to move left 

        segments = []



        # Main Gameplay
        while True:
            wn.update()
            if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
                time.sleep(1)  # the use of time module in order tio delay spawn of food for snake for is after each eat
                head.goto(0, 0)
                head.direction = "Stop"
                colors = random.choice(['red', 'blue', 'green'])
                shapes = random.choice(['square', 'circle'])
                for segment in segments:
                    segment.goto(1000, 1000)
                segments.clear()
                score = 0
                delay = 0.1
                pen.clear()
                pen.write("Score : {} High Score : {} ".format(
                    score, high_score), align="center", font=("candara", 24, "bold"))
            if head.distance(food) < 20: # spawns food anywhere between the given coordinates
                x = random.randint(-270, 270)
                y = random.randint(-270, 270)
                food.goto(x, y)  # assigns a random x and y coordinate from the given range 

                # Adding segment or lenthning of snake 
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("orange") # tail colour
                new_segment.penup()
                segments.append(new_segment) # a new segment gets added 
                delay -= 0.001   #delay of food 
                score += 10     # each food give s10 points
                if score > high_score:
                    #sets high score 
                    high_score = score
                pen.clear()
                pen.write("Score : {} High Score : {} ".format(
                    score, high_score), align="center", font=("candara", 24, "bold"))
            # Checking for head collisions with body segments
            for index in range(len(segments)-1, 0, -1):
                # the below code checks whether the x or y coordinate of snake and food match 
                x = segments[index-1].xcor()
                y = segments[index-1].ycor()
                segments[index].goto(x, y)
            if len(segments) > 0:
                x = head.xcor()
                y = head.ycor()
                segments[0].goto(x, y)
            move()
            for segment in segments:
                if segment.distance(head) < 20:
                    time.sleep(1)
                    head.goto(0, 0)
                    head.direction = "stop"
                    colors = random.choice(['red', 'blue', 'green'])
                    shapes = random.choice(['square', 'circle'])
                    for segment in segments:
                        segment.goto(1000, 1000)
                    segment.clear()

                    score = 0
                    delay = 0.1
                    pen.clear()#clears the code between delays 
                    pen.write("Score : {} High Score : {} ".format(
                        score, high_score), align="center", font=("candara", 24, "bold"))
            time.sleep(delay)


else:  
    # at last the game box exits if the score of the first quiz is insufficient 
    print('First Get Knowledge then Play Games')








    
            


