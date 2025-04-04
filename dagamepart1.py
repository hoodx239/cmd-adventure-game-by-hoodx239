import os
import time
import random
import tkinter
from tkinter import messagebox
import tkinter.messagebox

def mathpart():
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)
    answer = num1 + num2

    print(f"SOLVE IN UNDER 5 SECONDS TO KEEP YOUR SCREAMING BACK")
    print(f"{num1} + {num2} = ?") 
    start_time = time.time()
    userans = input("> ")
    elapsedtime = time.time() - start_time

    if elapsedtime > 5:
        input("Too slow. You screamed and died, you tried to keep it back though.")
    elif userans == str(answer):
        input("Phew, close call. Almost lost there. But you held it back and the entity left.")
    else:
        input("Wrong. You screamed and the entity skinned you. What a great time to be alive myes?")
def math2():
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)
    answer = num1 + num2

    print(f"SOLVE IN UNDER 5 SECONDS TO KEEP CLIMBING")
    print(f"{num1} + {num2} = ?") 
    start_time = time.time()
    userans = input("> ")
    elapsedtime = time.time() - start_time

    if elapsedtime > 5:
        input("aww mann. u rlly was close but you didnt solve it. ju ded")
    elif userans == str(answer):
        input("Phew, close call. Almost lost there. but you successfully climbed out .")
    else:
        input("Wrong. You fell and the entity skinned you. What a great time to be alive myes?")


def fight_entity():
    os.system("color 4")
    print("THE ENTITY GRABS YOU! SPAM ENTER TO FIGHT IT OFF!!")
    input("Press ENTER to start spamming!!")

    presses = 0
    time_limit = 5
    start_time = time.time()

    print(f"Start spamming ENTER! You have {time_limit} seconds!")

    while time.time() - start_time < time_limit:
        input()  
        presses += 1
        os.system("cls")
        print(presses)

    print("\nTIME'S UP!")
    time.sleep(1.5)  
    print(f"\nYou pressed ENTER {presses} times!")

    if presses >= 20:
        print("YOU FOUGHT THE ENTITY OFF! YOU'RE SAFE... FOR NOW.")
    else:
        print("NOT FAST ENOUGH... THE ENTITY OVERPOWERED YOU... goodnight ")
        input()

    input("\nPress ENTER to continue...")

def main():
    print("welcome to my adventure game!! ")
    woke = input("you woke up in a strange abandoned house. what do you do? \n (1) LOOK AROUND       (2) SCREAM FOR HELP ")





def scream():
    os.system("cls")
    foot = input("now you hear footsteps. a cold sweat rans down your face. what do you do? \n (1) RUN IMMEDIATELY(FAST ENTITY)      (2) KEEP SCREAMING       (3) HIDE INTO THAT RUSTY BOX ON YOUR RIGHT")
    if foot == "1":
        input("you were running for your life but the entity was faster. atleast u tried :/ ")
    elif foot == "2":
        input("wtf are you doing? why are you still screaming? entity is stronger. ur dead. gg :/ ")
    elif foot == "3":
        quiet = input("you barely hid in time. the entity is in front of you and he cant see you because you kept quiet. what do you do now? \n (1) START SCREAMING      (2) HOLD YOUR SCREAMING BACK")
        if quiet == "1":
            input("do i even need to explain? back to lobby :/ ")
        elif quiet == "2":
            input("HOLD YOUR SCREAMS BACK")
            print(mathpart())
    else:
        input("bruh u fr rn? u aint tricking me")
    wyd = input("what you doing now?   \n (1) KEEP YOURSELF IN THE BOX    (2)  GET OUT  ")
    if wyd == "1":
        input("you waited, and waited, and waited, and waited but eventually you starved to death. next time, bring food with you :'D ")
    elif wyd == "2":
        input("you got out, and now the monster isnt there")

print(main())


print(scream())

os.system("cls")
yummy = input("you are really hungry and you found some food, the thing is that it seems a lil bit weird. there is a 50% chance that you will get infected and die, still eat it?  \n    (1)  yes    (2)  no")

if yummy == "2":
    input("unfortunately you threw up and starved. not so happy anymore, myes?")
elif yummy == "1":
    number = random.randint(1, 2)
    if number == 2:
        input("you got poisoned. bad luck maybe?")
    elif number == 1:
        nextz = input("lucky dude. got lucky this time but im not sure about the rest. \n  ")

esc = input("now its your time to escape. what do you do? \n     (1) ATTACK THE ENTITY      (2) HIDE ON TOP OF THE CEILING TO CLIMB OUT")

if esc == "1":
    input("bruh u serious? the entity is locked in remember? ts pmo sm rn r u fr rn ")
elif esc == "2":
    input("climbing is hard for you as you're weak. SOLVE THIS MATH PROBLEMS IN UNDER 5 SECONDS TO SOLVE")
    print(())

ent = input("NOO THE CEILING BROKE AND U FELL BACK AND NOW THE ENTITY IS TRYING TO KILL YOU WYD \n  (1) FIGHT IT OFF   (2) ACCEPT UR FATE ")
if ent == "2":
    input("you accepted your fate like a dumbass. gn lil bro ")
elif ent == "1":
    fight_entity()
os.system("color 7")

input("you absolutely KILLED the entity. now you can exit. ")

tkinter.messagebox.showinfo("ILL BE BACK", "ILL BE BACK IN A PART 2 ;)")
tkinter.messagebox.showinfo("UR NOT SAFE HAHA", "THERE WILL BE A REMATCH ON https://github.com/hoodx239")
tkinter.messagebox.showinfo("UR NOT SAFE", "UR NOT SAFEUR NOT SAFEUR NOT SAFEUR NOT SAFEUR NOT SAFEUR NOT SAFEUR NOT SAFEUR NOT SAFE")

input("Press ENTER to exit.")
