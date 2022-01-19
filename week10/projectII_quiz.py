#define the questions you want with the answers

questions = {
    "What is the latest version of Microsoft Windows": "Windows 11",
    "Who created Microsoft Windows": "Bill Gates"
}

#get the names of the players

player1 = input("Who is player 1? ")
player2 = input("Who is player 2? ")

print("No cheating allowed :) ")

#initial score of each player

score1 = 0
score2 = 0

#begin the quiz for player 1
for ans in questions:
    
    tries1 = 3
    
    while tries1 > 0:
        print(ans)
        print(player1)
        user1_ans = input("Please input your answer: ")
        if user1_ans.upper() == questions[ans].upper():
            print("Hurray you are right")
            score1 += 1
            break
        
        else:
            tries1 -=1
            print("You have", tries1, " tries left")

#To clear the screen           
import click

def clrscr():
    click.clear()
    
    print("Screen Cleared to prevent cheating")
    
clrscr()
    
print("Player 2 it is now your turn")  

#begin the quiz for player 2
for ans in questions:
    
    tries2 = 3
    
    while tries2 >0:
        print(ans)
        print(player2)
        user2_ans = input("Please input your answer: ")
        if user2_ans.lower() == questions[ans].lower():
            print("Hurray you are right")
            score2 += 1
            break
        
        else:
            tries2 -=1
            print("You have", tries2, " tries left")
    

print("The answers are ", questions)
                   
#display each player's score
  
print("Player 1, ",player1, " has a score of ", score1)
print("Player 2, ",player2, " has a score of ", score2)

#display the winner
            
if score1 > score2:
    print(player1,  " wins")
   
elif score1 == score2:
    print("It's a draw")
     
else:
    print(player2, " wins")   
        