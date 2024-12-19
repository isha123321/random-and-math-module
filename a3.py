import random
options =["rock","paper","scissors"]
user_choice=input("choose rock ,paper or scissors:")
computer_choice=random.choice(options)
print("you choose:",user_choice)
print("computer choose:",computer_choice)
if user_choice==computer_choice:
    print ("its a TIE!")
elif user_choice=="rock" and computer_choice=="scissors":
    print("rock smashes the sciorrs .YOU WON!!")
elif user_choice=="scissors" and computer_choice=="rock":
    print("rock smashes the scissors.COMPUTER WON!!")
elif user_choice=="paper" and computer_choice=="scissors":
    print("scissors cuts the paper.COMPUTER WON!!")
elif user_choice=="scissors"and computer_choice=="paper":
    print("scissors cuts the paper .YOU WON!!")
elif user_choice=="rock" and computer_choice=="paper":
    print("paper wraps up the rock.COMPUTER WON!!")
elif user_choice=="paper" and computer_choice=="rock":
    print("paper wraps the rock.YOU WON!!")

