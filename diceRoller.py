import random
import os
import csv
#D4, D6, D8, D10, D12, and D20

def rollD4() -> int:
    rollAmount = random.randint(1,4)
    return rollAmount

def rollD6()->int:
    rollAmount = random.randint(1,6)
    return rollAmount

def rollD8()->int:
    rollAmount = random.randint(1,8)
    return rollAmount

def rollD10()->int:
    rollAmount = random.randint(1,10)
    return rollAmount

def rollD12()->int:
    rollAmount = random.randint(1,12)
    return rollAmount

def rollD20()->int:
    rollAmount=random.randint(1,20)
    return rollAmount    

def roll(dice:str,num_dice:int)->int:
    value = []
    
    if dice == "D4":
        for i in range(num_dice):
            value.append(rollD4())
    elif dice == "D6":
        for i in range(num_dice):
            value.append(rollD6())
    elif dice == "D10":
        for i in range(num_dice):
            value.append(rollD10())
    elif dice == "D12":
        for i in range(num_dice):
            value.append(rollD12())
    elif dice == "D20":
        for i in range(num_dice):
            value.append(rollD20())
    print(value)
    return value
def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
response = ['y','yes']
player_name = ''
samePlayer = ''
player = dict()
dices = ["D4","D6","D10","D12","D20"]
if __name__ == "__main__":
    print("\tDice Roller\n\tBy Rafay Ahmad Raza")
    SessionNumber = input("Enter the Session Number\n> ")

    while True:
        if SessionNumber.isdecimal():
            break
        else:
            SessionNumber = input("Invalid Input, Write Only Numbers\n> ")

    SessionNumber= int(SessionNumber)
    while True:

        Dice = input("Enter The Dice Type\n D4 D6 D10 D12 D20\n> ")
        while True:
            if Dice not in dices:
                Dice = input("Invalid Input > ")
            else:
                break
        
        player_name = input("Who is Rolling? Type 0 if same person is rolling\n> ")
        if player_name == '0':
            player_name = samePlayer
        else:
            samePlayer = player_name

        Num_Dice = input("Enter the Number of dice to be rolled > ")
        while True:
            if Num_Dice.isnumeric():
                break
            else:
                Num_Dice = input("Enter Only Numbers\n> ")

     
       
        rollValue = roll(Dice,int(Num_Dice))


        player[player_name+" "+Num_Dice+" "+Dice] = rollValue
        print(f"The Value of Roll For {Num_Dice} {Dice} is {rollValue}")

        if input('Do you want to roll again?\n> ').lower() in response:
            clearScreen()
                 
            continue
        else:
            print(player)
            break

    csvFile = open(f"PlayerDataSessionNumber{SessionNumber}.csv",'a',newline='')
    writer = csv.writer(csvFile)

    file_exists = os.path.isfile(f"PlayerDataSessionNumber{SessionNumber}.csv") and os.path.getsize(f"PlayerDataSessionNumber{SessionNumber}.csv") > 0
    if file_exists:
        print("file opened")
    else:
        print("file created")
        writer.writerow(['NNT','Roll Value'])
    playerInfos= list(player.keys())
    rolls = list(player.values())
    
    for name,roll in zip(playerInfos,rolls):
        writer.writerow([name.strip(),str(roll).strip()])

     




