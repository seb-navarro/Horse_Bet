import random
from time import sleep

wallet = 200


class horse():
    def __init__(self, name, time, lapTime, lapComplete, finish):
        self.name = name
        self.time = time
        self.lapTime = lapTime
        self.lapComplete = lapComplete
        self.finish = finish


    def runL1 (self):
        while not self.lapComplete:
            self.lapComplete = random.choice([True, False])
            if self.lapComplete:
                self.time += 20
                self.lapTime += 20
                print (f"{self.name} completed the first lap in {self.lapTime} seconds")
                self.lapTime = 0
                self.lapComplete = False
                break
            else:
                self.time += 1
                self.lapTime += 1

    def runL2 (self):
        while not self.lapComplete:
            self.lapComplete = random.choice([True, False])
            if self.lapComplete:
                self.time += 20
                self.lapTime += 20
                print (f"{self.name} completed the second lap in {self.lapTime} seconds")
                self.lapTime = 0
                self.lapComplete = False
                break
            else:
                self.time += 1
                self.lapTime += 1

    def runL3 (self):
        while not self.lapComplete:
            self.lapComplete = random.choice([True, False])
            if self.lapComplete:
                self.time += 20
                self.lapTime += 20
                print (f"{self.name} completed the third lap in {self.lapTime} seconds")
                self.lapTime = 0
                self.lapComplete = False
                break
            else:
                self.time += 1
                self.lapTime += 1

    def runL4 (self):
        while not self.lapComplete:
            self.lapComplete = random.choice([True, False])
            if self.lapComplete:
                self.time += 20
                self.lapTime += 20
                print (f"{self.name} completed the fourth lap in {self.lapTime} seconds")
                self.lapTime = 0
                self.lapComplete = False
                break
            else:
                self.time += 1
                self.lapTime += 1

    def runL5 (self):
        while not self.lapComplete:
            self.lapComplete = random.choice([True, False])
            if self.lapComplete:
                self.time += 20
                self.lapTime += 20
                print (f"{self.name} completed the fith lap in {self.lapTime} seconds")
                self.lapTime = 0
                self.lapComplete = False
                break
            else:
                self.time += 1
                self.lapTime += 1

    def runL6 (self):
        while not self.lapComplete:
            self.lapComplete = random.choice([True, False])
            if self.lapComplete:
                self.time += 20
                self.lapTime += 20
                print (f"{self.name} completed the final lap in {self.lapTime} seconds")
                self.lapTime = 0
                self.lapComplete = False
                self.finish = True
                break
            else:
                self.time += 1
                self.lapTime += 1


Choc = horse("Choc", 0, 0, False, False)
Moose = horse("Moose", 0, 0, False, False)
Reggie = horse("Reggie", 0, 0, False, False)
Sol = horse("Sol", 0, 0, False, False)


def bet():
    global wallet
    global stake
    global hbName

    hb = input("Which horse would you like to bet on:\n A) Choc \n B) Moose \n C) Reggie \n D) Sol \n")
    while hb != "a" and hb != "A" and hb != "b" and hb != "B" and hb != "c" and hb != "C" and hb != "d" and hb != "D":
        hb = input("Please choose either A, B, C or D \n")
        if hb == "a" and hb == "A" and hb == "b" and hb == "B" and hb == "c" and hb == "C" and hb == "d" and hb == "D":
            break 

    if hb == "a" or hb == "A":
        hbName = "Choc"
    elif hb == "b" or hb == "B":
        hbName = "Moose"
    elif hb == "c" or hb == "C":
        hbName = "Reggie"
    elif hb == "d" or hb == "D":
        hbName = "Sol"

    while True:
        try:
            stake = int(input ("How much would you like to bet in GBP? \n"))
            while stake > wallet:
                stake = int(input(f"You do not have enough money to bet that ammount, your current balance is {wallet} \nPlease try again \n"))
                if stake <= wallet:
                    break
            break
        except ValueError:
            print("Please enter a whole number")

        
    wallet -= stake
    sleep(1)
    print("-----")
    print(f"You have placed a bet of £{stake} on {hbName}")
    sleep(1)
    print(f"Your current balance is £{wallet}")


def resultLap():
    lapR = [Reggie.time, Sol.time, Choc.time, Moose.time]
    lapR.sort()


    if lapR[0] == lapR[1] and lapR[0] != lapR[2] and lapR[2] != lapR[3]:
        tieTop = True
    else:
        tieTop = False

    if lapR[0] == lapR[1] and lapR[0] == lapR[2] and lapR[0] != lapR[3]:
        tie3Top = True
    else:
        tie3Top = False

    if lapR[0] == lapR[1] and lapR[0] == lapR[2] and lapR[0] == lapR[3]:
        tieFull = True
    else:
        tieFull = False

    if lapR[3] == lapR[2] and lapR[3] != lapR[1] and lapR[1] != lapR[0]:
        tieLast = True
    else:
        tieLast = False

    if lapR[3] == lapR[2] and lapR[3] == lapR[1] and lapR[3] != lapR[0]:
        tie3Last = True
    else:
        tie3Last = False

    if lapR[1] == lapR[2] and lapR[1] != lapR[0] and lapR[2] != lapR[3]:
        tieSecond = True
    else:
        tieSecond = False

    if lapR[0] == lapR[1] and lapR[2] == lapR[3] and lapR[0] != lapR[3]:
        tieDouble = True
    else:
        tieDouble = False


    c1 = lapR.index(Choc.time)
    lapR[c1] = Choc.name

    m1 = lapR.index(Moose.time)
    lapR[m1] = Moose.name

    r1 = lapR.index(Reggie.time)
    lapR[r1] = Reggie.name

    s1 = lapR.index(Sol.time)
    lapR[s1] = Sol.name

    print(" ")

    if Choc.finish and Moose.finish and Reggie.finish and Sol.finish:
        if tieTop:
            print(f"{lapR[0]} and {lapR[1]} finished the race joint at 1st place")
            sleep(1)
            print(f"{lapR[2]} finished the race in 3rd place")
            sleep(1)
            print(f"{lapR[3]} finished the race in last place")
            sleep(1)
        elif tie3Top:
            print(f"{lapR[0]}, {lapR[1]}, and {lapR[2]} finished the race joint at 1st place")
            sleep(1)
            print(f"{lapR[3]} finished the race in last place")
            sleep(1)
        elif tieFull:
            print(f"All horses finished the race tied")
            sleep(1)
        elif tieLast:
            print(f"{lapR[0]} finished the race in 1st place")
            sleep(1)
            print(f"{lapR[1]} finished the race in 2nd place")
            sleep(1)
            print(f"{lapR[2]} and {lapR[3]} finished the race joint at 3rd place")
            sleep(1)
        elif tie3Last:
            print(f"{lapR[0]} finished the race in 1st place")
            sleep(1)
            print(f"{lapR[1]}, {lapR[2]}, and {lapR[3]} finished the race joint at 2nd place")
            sleep(1)
        elif tieSecond:
            print(f"{lapR[0]} finished the race in 1st place")
            sleep(1)
            print(f"{lapR[1]} and {lapR[2]} finished the race joint at 2nd place")
            sleep(1)
            print(f"{lapR[3]} finished the race in last place")
            sleep(1)
        elif tieDouble:
            print(f"{lapR[0]} and {lapR[1]} finished the race joint at 1st place")
            sleep(1)
            print(f"{lapR[2]} and {lapR[3]} finished the race joint at 2nd place")
            sleep(1)
        else:
            print(f"{lapR[0]} finished the race in 1st place")
            sleep(1)
            print(f"{lapR[1]} finished the race in 2nd place")
            sleep(1)
            print(f"{lapR[2]} finished the race in 3rd place")
            sleep(1)
            print(f"{lapR[3]} finished the race in last place")
            sleep(1)

    if not Choc.finish or not Moose.finish or not Reggie.finish or not Sol.finish:
        if tieTop:
            print(f"{lapR[0]} and {lapR[1]} are currently joint at 1st place")
            sleep(1)
            print(f"{lapR[2]} is currently in 3rd place")
            sleep(1)
            print(f"{lapR[3]} is currently in last place")
            sleep(1)
        elif tie3Top:
            print(f"{lapR[0]}, {lapR[1]}, and {lapR[2]} are currently joint at 1st place")
            sleep(1)
            print(f"{lapR[3]} is currently in last place")
            sleep(1)
        elif tieFull:
            print(f"All horses are currently tied")
            sleep(1)
        elif tieLast:
            print(f"{lapR[0]} is currently in 1st place")
            sleep(1)
            print(f"{lapR[1]} is currently in 2nd place")
            sleep(1)
            print(f"{lapR[2]} and {lapR[3]} are currently joint at 3rd place")
            sleep(1)
        elif tie3Last:
            print(f"{lapR[0]} is currently in 1st place")
            sleep(1)
            print(f"{lapR[1]}, {lapR[2]}, and {lapR[3]} are currently joint at 2nd place")
            sleep(1)
        elif tieSecond:
            print(f"{lapR[0]} is currently in 1st place")
            sleep(1)
            print(f"{lapR[1]} and {lapR[2]} are currently joint at 2nd place")
            sleep(1)
            print(f"{lapR[3]} is currently in last place")
            sleep(1)
        elif tieDouble:
            print(f"{lapR[0]} and {lapR[1]} are currently joint at 1st place")
            sleep(1)
            print(f"{lapR[2]} and {lapR[3]} are currently joint at 2nd place")
            sleep(1)
        else:
            print(f"{lapR[0]} is currently in 1st place")
            sleep(1)
            print(f"{lapR[1]} is currently in 2nd place")
            sleep(1)
            print(f"{lapR[2]} is currently in 3rd place")
            sleep(1)
            print(f"{lapR[3]} is currently in last place")
            sleep(1)

        print("-----")
        print("Press enter to continue")
        input("-----")
        sleep(1)


def resultBet():
    global stake
    global wallet
    global win

    if hbName == "Choc" and Choc.time < Moose.time and Choc.time < Reggie.time and Choc.time < Sol.time:
        win = (stake * 4) + stake
        wallet += win
        print(f"Congratulations, your horse won! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Choc" and Choc.time == Moose.time and Choc.time < Reggie.time and Choc.time < Sol.time:
        win = round((stake * 4)/2) + stake
        wallet += win
        print(f"Congratulations, your horse finished joint 1st with another horse! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Choc" and Choc.time < Moose.time and Choc.time == Reggie.time and Choc.time < Sol.time:
        win = round((stake * 4)/2) + stake
        wallet += win
        print(f"Your horse finished joint 1st with another horse! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Choc" and Choc.time < Moose.time and Choc.time < Reggie.time and Choc.time == Sol.time:
        win = round((stake * 4)/2) + stake
        wallet += win
        print(f"Congratulations, your horse finished joint 1st with another horse! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Choc" and Choc.time == Moose.time and Choc.time == Reggie.time and Choc.time < Sol.time:
        win = round((stake * 4)/3) + stake
        wallet += win
        print (f"Congratulations, your horse finished joint 1st with two other horses! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Choc" and Choc.time == Moose.time and Choc.time < Reggie.time and Choc.time == Sol.time:
        win = round((stake * 4)/3) + stake
        wallet += win
        print (f"Congratulations, your horse finished joint 1st with two other horses! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Choc" and Choc.time < Moose.time and Choc.time == Reggie.time and Choc.time == Sol.time:
        win = round((stake * 4)/3) + stake
        wallet += win
        print (f"Congratulations, your horse finished joint 1st with two other horses! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Choc" and Choc.time == Moose.time and Choc.time == Reggie.time and Choc.time == Sol.time:
        wallet += stake
        print(f"The race was a draw between all horses! You have recieved your initial bet of £{stake} back. Your current balance is £{wallet}")
    elif hbName == "Choc":
        print(f"Unfortunately Your horse failed to win. You have lost your initial bet of £{stake}. Your current balance is £{wallet}")


    if hbName == "Moose" and Moose.time < Choc.time and Moose.time < Reggie.time and Moose.time < Sol.time:
        win = (stake * 4) + stake
        wallet += win
        print(f"Congratulations, your horse won! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Moose" and Moose.time == Choc.time and Moose.time < Reggie.time and Moose.time < Sol.time:
        win = round((stake * 4)/2) + stake
        wallet += win
        print(f"Congratulations, your horse finished joint 1st with another horse! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Moose" and Moose.time < Choc.time and Moose.time == Reggie.time and Moose.time < Sol.time:
        win = round((stake * 4)/2) + stake
        wallet += win
        print(f"Your horse finished joint 1st with another horse! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Moose" and Moose.time < Choc.time and Moose.time < Reggie.time and Moose.time == Sol.time:
        win = round((stake * 4)/2) + stake
        wallet += win
        print(f"Congratulations, your horse finished joint 1st with another horse! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Moose" and Moose.time == Choc.time and Moose.time == Reggie.time and Moose.time < Sol.time:
        win = round((stake * 4)/3) + stake
        wallet += win
        print (f"Congratulations, your horse finished joint 1st with two other horses! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Moose" and Moose.time == Choc.time and Moose.time < Reggie.time and Moose.time == Sol.time:
        win = round((stake * 4)/3) + stake
        wallet += win
        print (f"Congratulations, your horse finished joint 1st with two other horses! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Moose" and Moose.time < Choc.time and Moose.time == Reggie.time and Moose.time == Sol.time:
        win = round((stake * 4)/3) + stake
        wallet += win
        print (f"Congratulations, your horse finished joint 1st with two other horses! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Moose" and Moose.time == Choc.time and Moose.time == Reggie.time and Moose.time == Sol.time:
        wallet += stake
        print(f"The race was a draw between all horses! You have recieved your initial bet of £{stake} back. Your current balance is £{wallet}")
    elif hbName == "Moose":
        print(f"Unfortunately Your horse failed to win. You have lost your initial bet of £{stake}. Your current balance is £{wallet}")


    if hbName == "Reggie" and Reggie.time < Choc.time and Reggie.time < Moose.time and Reggie.time < Sol.time:
        win = (stake * 4) + stake
        wallet += win
        print(f"Congratulations, your horse won! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Reggie" and Reggie.time == Choc.time and Reggie.time < Moose.time and Reggie.time < Sol.time:
        win = round((stake * 4)/2) + stake
        wallet += win
        print(f"Congratulations, your horse finished joint 1st with another horse! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Reggie" and Reggie.time < Choc.time and Reggie.time == Moose.time and Reggie.time < Sol.time:
        win = round((stake * 4)/2) + stake
        wallet += win
        print(f"Your horse finished joint 1st with another horse! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Reggie" and Reggie.time < Choc.time and Reggie.time < Moose.time and Reggie.time == Sol.time:
        win = round((stake * 4)/2) + stake
        wallet += win
        print(f"Congratulations, your horse finished joint 1st with another horse! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Reggie" and Reggie.time == Choc.time and Reggie.time == Moose.time and Reggie.time < Sol.time:
        win = round((stake * 4)/3) + stake
        wallet += win
        print (f"Congratulations, your horse finished joint 1st with two other horses! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Reggie" and Reggie.time == Choc.time and Reggie.time < Moose.time and Reggie.time == Sol.time:
        win = round((stake * 4)/3) + stake
        wallet += win
        print (f"Congratulations, your horse finished joint 1st with two other horses! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Reggie" and Reggie.time < Choc.time and Reggie.time == Moose.time and Reggie.time == Sol.time:
        win = round((stake * 4)/3) + stake
        wallet += win
        print (f"Congratulations, your horse finished joint 1st with two other horses! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Reggie" and Reggie.time == Choc.time and Reggie.time == Moose.time and Reggie.time == Sol.time:
        wallet += stake
        print(f"The race was a draw between all horses! You have recieved your initial bet of £{stake} back. Your current balance is £{wallet}")
    elif hbName == "Reggie":
        print(f"Unfortunately Your horse failed to win. You have lost your initial bet of £{stake}. Your current balance is £{wallet}")


    if hbName == "Sol" and Sol.time < Choc.time and Sol.time < Moose.time and Sol.time < Reggie.time:
        win = (stake * 4) + stake
        wallet += win
        print(f"Congratulations, your horse won! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Sol" and Sol.time == Choc.time and Sol.time < Moose.time and Sol.time < Reggie.time:
        win = round((stake * 4)/2) + stake
        wallet += win
        print(f"Congratulations, your horse finished joint 1st with another horse! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Sol" and Sol.time < Choc.time and Sol.time == Moose.time and Sol.time < Reggie.time:
        win = round((stake * 4)/2) + stake
        wallet += win
        print(f"Your horse finished joint 1st with another horse! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Sol" and Sol.time < Choc.time and Sol.time < Moose.time and Sol.time == Reggie.time:
        win = round((stake * 4)/2) + stake
        wallet += win
        print(f"Congratulations, your horse finished joint 1st with another horse! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Sol" and Sol.time == Choc.time and Sol.time == Moose.time and Sol.time < Reggie.time:
        win = round((stake * 4)/3) + stake
        wallet += win
        print (f"Congratulations, your horse finished joint 1st with two other horses! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Sol" and Sol.time == Choc.time and Sol.time < Moose.time and Sol.time == Reggie.time:
        win = round((stake * 4)/3) + stake
        wallet += win
        print (f"Congratulations, your horse finished joint 1st with two other horses! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Sol" and Sol.time < Choc.time and Sol.time == Moose.time and Sol.time == Reggie.time:
        win = round((stake * 4)/3) + stake
        wallet += win
        print (f"Congratulations, your horse finished joint 1st with two other horses! You have won £{win}! Your current balance is £{wallet}")
    elif hbName == "Sol" and Sol.time == Choc.time and Sol.time == Moose.time and Sol.time == Reggie.time:
        wallet += stake
        print(f"The race was a draw between all horses! You have recieved your initial bet of £{stake} back. Your current balance is £{wallet}")
    elif hbName == "Sol":
        print(f"Unfortunately Your horse failed to win. You have lost your initial bet of £{stake}. Your current balance is £{wallet}")


def runRace():
    print(f"Your balance is £{wallet}")
    sleep(1)

    bet()

    print("-----")
    print("Press enter to begin the race")
    input("-----")

    print("BANG!")
    sleep(1)
    print("The horses are off!")
    sleep(1)

    print("-----")
    print("Press enter to continue")
    input("-----")
    sleep(1)

    print("LAP 1")
    print(" ")
    sleep(1)
    Choc.runL1()
    sleep(1)
    Moose.runL1()
    sleep(1)
    Reggie.runL1()
    sleep(1)
    Sol.runL1()
    sleep(1)

    resultLap()

    print("LAP 2")
    print(" ")
    sleep(1)
    Choc.runL2()
    sleep(1)
    Moose.runL2()
    sleep(1)
    Reggie.runL2()
    sleep(1)
    Sol.runL2()
    sleep(1)

    resultLap()

    print("LAP 3")
    print(" ")
    sleep(1)
    Choc.runL3()
    sleep(1)
    Moose.runL3()
    sleep(1)
    Reggie.runL3()
    sleep(1)
    Sol.runL3()
    sleep(1)

    resultLap()

    print("LAP 4")
    print(" ")
    sleep(1)
    Choc.runL4()
    sleep(1)
    Moose.runL4()
    sleep(1)
    Reggie.runL4()
    sleep(1)
    Sol.runL4()
    sleep(1)

    resultLap()

    print("LAP 5")
    print(" ")
    sleep(1)
    Choc.runL5()
    sleep(1)
    Moose.runL5()
    sleep(1)
    Reggie.runL5()
    sleep(1)
    Sol.runL5()
    sleep(1)

    resultLap()

    print("FINAL LAP")
    print(" ")
    sleep(1)
    Choc.runL6()
    sleep(1)
    Moose.runL6()
    sleep(1)
    Reggie.runL6()
    sleep(1)
    Sol.runL6()
    sleep(1)

    resultLap()

    print("-----")
    print("Press enter to continue")
    input("-----")
    sleep(1)

    print("BET RESULTS")
    print(" ")
    sleep(1)
    resultBet()
    print ("-----")
    sleep(1)

    Choc.finish = False
    Moose.finish = False
    Reggie.finish = False
    Sol.finish = False

    Choc.time = 0
    Moose.time = 0
    Reggie.time = 0
    Sol.time = 0

    if wallet > 0:
        decision = input("Would you like to try your luck on another race? (Y/N) \n")
        while decision != "Y" and decision != "y" and decision != "N" and decision != "n":
            decision = input("Please type either Y for yes, or N for no. \n")
            if decision == "Y" and decision == "y" and decision == "N" and decision == "n":
                break

        if decision == "N" or decision == "n":
            sleep(1)
            print(" ")
            print("********************")
            print(f"Congratulations! You have walked away with £{wallet}.")
            print("********************")
            print(" ")
            sleep(1)
            print("Thank you for visiting the racecourse. Goodbye!")
            input(" ")
        elif decision == "Y" or decision == "y":
            sleep(1)
            print(" ")
            print("********************")
            print("Welcome Back to Race Day")
            print("********************")
            print(" ")
            sleep(1)
            runRace()
                

    else:
        sleep(1)
        print("You have gambled all your money away and cannot continue.")
        print(" ")
        sleep(1)
        print("Thank you for visiting the racecourse. Goodbye!")
        print(" ")
        sleep(1)


print(" ")
print("********************")
print("Welcome to Race Day!")
print("********************")

print("-----")
print("Press enter to see the rules")
input("-----")

print("RACECOURSE RULES")
sleep(1)
print(" ")
print("1. All horses have 4/1 odds - Example: £10 bet on the winning horse will return £50 (£40 winnings + £10 stake).")
sleep(1)
print ("2. We only accept bets to the nearest pound.")
sleep(1)
print ("3. If your returns include pennies then the final value will be rounded to the nearest pound.")
sleep(1)
print("4. If the race finishes in a draw between your horse and another horse, you will recieve half of the expected winnings plus your stake.")
sleep(1)
print("5. If the race finishes in a draw between your horse and two other horses you will recieve a third of the expected winnings plus your stake.")
sleep(1)
print("6. If all horses finish the race in a draw then you will only recieve your stake back.")
sleep(1)
print("7. One race runs for six laps.")
sleep(1)

print("-----")
print("Press enter to acknowledge the rules")
input("-----")

runRace()



