from random import randint;
import os;

"""
value = randint(1,10);
print("one day...");
role = input("what type of role are your character?");
bornAge = input("what year are you born ? ");
print(value/10);
"""


textlogo = """
    _____________________________________________________
    |                                                   |
    |                 Colossal Cave                     |
    |                                                   |
    |                The First Adventure                |
    |                _____________________              |
    |                                                   |
    |    Copyright (c) 1990,1991,1992 ImageIllusions    |
    |                                                   |
    |___________________________________________________|

    adapted by david gasior -- based on the game by woods and crowther
    """;

textinfo = """


        Created using: The Adventure Game Toolkit 1.3
            COpyright 1990 -- All Right Reserved
           by David R. Malmberg and Mark J.

                    Distributed by
""";


print(textlogo+textinfo);

input("Press enter to continue  . . .");
os.system("cls");
print("Colossal Cave");
print("The First Adventure ");
name = input("What is your name ? ");
role = input("What is your role? [ Wizard,Warrior,Monk,Mage ] ? ");
passcheck = False;
if(role=="wizard"):
    passcheck = True;
if(role=="warrior"):
    passcheck = True;
if(role=="monk"):
    passcheck = True;
if(role=="mage"):
    passcheck = True;
if(passcheck):
        
    age = input("Your Age ? ");
    status = "";
    if(int(age)<=20):
        status = "young";
    else:
        status = "old";
    print("Welcome adventurer "+name+". Your assigned role is "+role+". You are "+status+". ");
    playerHealth = randint(50,100);
    monsterHealth = randint(50,100);

    print("Your Health : "+str(playerHealth) + "\t Monster Health : "+ str(monsterHealth));
    if(playerHealth< monsterHealth):
        print("Your in danger !");
    elif(playerHealth==monsterHealth):
        print("You will make it!");
    else:
        print("Your victory has been assured !");


    monsterHealthPoint = [50,40,20,10];

    for health in monsterHealthPoint:

        print("Monster is bleeding . Monster health is "+str(health));
else:
    print("Wrong role !");
