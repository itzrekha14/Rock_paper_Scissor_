import random
print("\t\tROCK PAPER SCISSOR")
user_wins=0
computer_wins=0
tied=0
chance=10
while chance>0:
    chance-=1
    user_choice=input("Rock/paper/Scissor: ")
    choice=["rock","paper","scissor"]
    random_num=random.randint(0,2)
    computer_choice=choice[random_num]
    print("Computer chose:",computer_choice)
    if user_choice=="rock" and computer_choice=="scissor":
        print("you win!!")
        user_wins+=1
    elif user_choice=="paper" and computer_choice=="rock":
        print("You win!!")
        user_wins+=1

    elif user_choice=="scissor" and computer_choice=="paper":
        print("you win!")
        user_wins+=1
    elif user_choice==computer_choice:
        print("You both are tied")
        tied+=1
    else:
        print("Computer wins")
        computer_wins+=1
print("##################################################")
if user_wins>computer_wins:
    print("You won the game!!!")
else:
    print("Computer won the game!!")
print("You won",user_wins,"times/10")
print("Computer won",computer_wins,"times/10")
print("You both got tied at",tied,"times/10")
print("##################################################")



    






