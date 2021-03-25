import random;

choice = ["paper","scissor","rock","lizard","spock"];

com_choice = choice[random.randint(0,4)];
win = False;
tie = False;

print("Lets play Rock Paper Scissors Lizard Spock\n");
print("Computer choose : "+com_choice.upper());
usr_choice = input("Your Choice : ").lower();


# rock win
if((usr_choice == "rock" and com_choice == "scissor") or (usr_choice == "rock" and com_choice == "lizard")):
    win = True;
# rock lost
elif((usr_choice == "rock" and com_choice == "paper") or (usr_choice == "rock" and com_choice == "spock")):
    win = False;
# paper win
elif((usr_choice == "paper" and com_choice == "rock") or (usr_choice == "paper" and com_choice == "spock")):
    win = True;
# paper lost
elif((usr_choice == "paper" and com_choice == "scissor") or (usr_choice == "paper" and com_choice == "lizard")):
    win = False;
# scissor win
elif((usr_choice == "scissor" and com_choice == "paper") or (usr_choice == "scissor" and com_choice == "lizard")):
    win = True;
# scissor lost
elif((usr_choice == "scissor" and com_choice == "rock") or (usr_choice == "scissor" and com_choice == "spock")):
    win = False;
# spock win
elif((usr_choice == "spock" and com_choice == "scissor") or (usr_choice == "spock" and com_choice == "scissor")):
    win = True;
# spock lost
elif((usr_choice == "spock" and com_choice == "lizard") or (usr_choice == "spock" and com_choice == "paper")):
    win = False;
# lizard win
elif((usr_choice == "lizard" and com_choice == "spock") or (usr_choice == "lizard" and com_choice == "paper")):
    win = True;
# lizard lost
elif((usr_choice == "lizard" and com_choice == "rock") or (usr_choice == "lizard" and com_choice == "scissor")):
    win = False;

else:
    print("We're tie");
    tie = True;

if(tie == False):
    if(win):
        print("You Win !");
    else:
        print("You Lose !");