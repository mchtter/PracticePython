import random
import time


class Character:

    def __init__(self, characterName="Enemy", characterHealth=100, characterPower=5, characterBullet=10):
        self.characterName = characterName
        self.characterHealth = characterHealth
        self.characterPower = characterPower
        self.characterBullet = characterBullet

    def attackerChar(self):
        print(f"The {self.characterName} is attacked..........")
        usingBullet = random.randint(1, 5)
        print(f"The {self.characterName} was attacked for " +
              str(usingBullet) + " Bullet")
        self.characterBullet -= usingBullet
        return (usingBullet, self.characterPower)

    def defenderChar(self, usingBullet, characterPower):
        print(f"The {self.characterName} is defending..........")
        topDamage = (self.characterPower * usingBullet)
        self.characterHealth -= (self.characterPower * usingBullet)
        print(f"The {self.characterName} has {topDamage} damaged.")

    def overBullet(self):
        if (self.characterBullet <= 0):
            print(f"{self.characterName}'s Bullet is over.")
            if (len(characterList) == 1):
                return
            characterList.remove(self)
            return True
        return False

    def isDead(self):
        if (self.characterHealth <= 0):
            print(f"{self.characterName} is dead.")
            characterList.remove(self)
            return True
        return False

    def winner(self):
        return self.characterName

    def createCharacter(self):
        print(f"""
        Name   : {self.characterName}
        Health : {self.characterHealth}
        Power  : {self.characterPower}
        Bullet : {self.characterBullet}
        """)


characterList = []

char = 0
while char < 10:
    randomName = "Character" + str(char+1)
    randomHealth = random.randint(100, 300)
    randomPower = random.randint(1, 10)
    randomBullet = random.randint(1, 20)

    characterProperties = Character(
        randomName, randomHealth, randomPower, randomBullet)
    characterList.append(characterProperties)

    char += 1

for charList in characterList:
    charList.createCharacter()
    time.sleep(0.25)


while (True):
    if (len(characterList) == 10):
        randomCharacterOne = random.randint(0, 9)
        randomCharacterTwo = random.randint(0, 9)
        if (randomCharacterOne == randomCharacterTwo) or ((randomCharacterTwo > randomCharacterOne) and (randomCharacterTwo == 9)):
            continue
        else:
            print("\n\n")
            returnedValue = characterList[randomCharacterOne].attackerChar()
            characterList[randomCharacterTwo].defenderChar(
                returnedValue[0], returnedValue[1])
            time.sleep(0.25)
            characterList[randomCharacterOne].overBullet()
            characterList[randomCharacterTwo].isDead()
            time.sleep(0.5)

    elif (len(characterList) == 9):
        randomCharacterOne = random.randint(0, 8)
        randomCharacterTwo = random.randint(0, 8)
        if (randomCharacterOne == randomCharacterTwo) or ((randomCharacterTwo > randomCharacterOne) and (randomCharacterTwo == 8)):
            continue
        else:
            print("\n\n")
            returnedValue = characterList[randomCharacterOne].attackerChar()
            characterList[randomCharacterTwo].defenderChar(
                returnedValue[0], returnedValue[1])
            time.sleep(0.25)
            characterList[randomCharacterOne].overBullet()
            characterList[randomCharacterTwo].isDead()
            time.sleep(0.5)

    elif (len(characterList) == 8):
        randomCharacterOne = random.randint(0, 7)
        randomCharacterTwo = random.randint(0, 7)
        if (randomCharacterOne == randomCharacterTwo) or ((randomCharacterTwo > randomCharacterOne) and (randomCharacterTwo == 7)):
            continue
        else:
            print("\n\n")
            returnedValue = characterList[randomCharacterOne].attackerChar()
            characterList[randomCharacterTwo].defenderChar(
                returnedValue[0], returnedValue[1])
            time.sleep(0.25)
            characterList[randomCharacterOne].overBullet()
            characterList[randomCharacterTwo].isDead()
            time.sleep(0.5)

    elif (len(characterList) == 7):
        randomCharacterOne = random.randint(0, 6)
        randomCharacterTwo = random.randint(0, 6)
        if (randomCharacterOne == randomCharacterTwo) or ((randomCharacterTwo > randomCharacterOne) and (randomCharacterTwo == 6)):
            continue
        else:
            print("\n\n")
            returnedValue = characterList[randomCharacterOne].attackerChar()
            characterList[randomCharacterTwo].defenderChar(
                returnedValue[0], returnedValue[1])
            time.sleep(0.25)
            characterList[randomCharacterOne].overBullet()
            characterList[randomCharacterTwo].isDead()
            time.sleep(0.5)

    elif (len(characterList) == 6):
        randomCharacterOne = random.randint(0, 5)
        randomCharacterTwo = random.randint(0, 5)
        if (randomCharacterOne == randomCharacterTwo) or ((randomCharacterTwo > randomCharacterOne) and (randomCharacterTwo == 5)):
            continue
        else:
            print("\n\n")
            returnedValue = characterList[randomCharacterOne].attackerChar()
            characterList[randomCharacterTwo].defenderChar(
                returnedValue[0], returnedValue[1])
            time.sleep(0.25)
            characterList[randomCharacterOne].overBullet()
            characterList[randomCharacterTwo].isDead()
            time.sleep(0.5)

    elif (len(characterList) == 5):
        randomCharacterOne = random.randint(0, 4)
        randomCharacterTwo = random.randint(0, 4)
        if (randomCharacterOne == randomCharacterTwo) or ((randomCharacterTwo > randomCharacterOne) and (randomCharacterTwo == 4)):
            continue
        else:
            print("\n\n")
            returnedValue = characterList[randomCharacterOne].attackerChar()
            characterList[randomCharacterTwo].defenderChar(
                returnedValue[0], returnedValue[1])
            time.sleep(0.25)
            characterList[randomCharacterOne].overBullet()
            characterList[randomCharacterTwo].isDead()
            time.sleep(0.5)

    elif (len(characterList) == 4):
        randomCharacterOne = random.randint(0, 3)
        randomCharacterTwo = random.randint(0, 3)
        if (randomCharacterOne == randomCharacterTwo) or ((randomCharacterTwo > randomCharacterOne) and (randomCharacterTwo == 3)):
            continue
        else:
            print("\n\n")
            returnedValue = characterList[randomCharacterOne].attackerChar()
            characterList[randomCharacterTwo].defenderChar(
                returnedValue[0], returnedValue[1])
            time.sleep(0.25)
            characterList[randomCharacterOne].overBullet()
            characterList[randomCharacterTwo].isDead()
            time.sleep(0.5)

    elif (len(characterList) == 3):
        randomCharacterOne = random.randint(0, 2)
        randomCharacterTwo = random.randint(0, 2)
        if (randomCharacterOne == randomCharacterTwo) or ((randomCharacterTwo > randomCharacterOne) and (randomCharacterTwo == 2)):
            continue
        else:
            print("\n\n")
            returnedValue = characterList[randomCharacterOne].attackerChar()
            characterList[randomCharacterTwo].defenderChar(
                returnedValue[0], returnedValue[1])
            time.sleep(0.25)
            characterList[randomCharacterOne].overBullet()
            characterList[randomCharacterTwo].isDead()
            time.sleep(0.5)

    elif (len(characterList) == 2):
        randomCharacterOne = random.randint(0, 1)
        randomCharacterTwo = random.randint(0, 1)
        if (randomCharacterOne == randomCharacterTwo) or (randomCharacterTwo == 0):
            continue
        else:
            print("\n\n")
            returnedValue = characterList[randomCharacterOne].attackerChar()
            characterList[randomCharacterTwo].defenderChar(
                returnedValue[0], returnedValue[1])
            time.sleep(0.25)
            characterList[randomCharacterTwo].isDead()
            characterList[randomCharacterOne].overBullet()
            time.sleep(0.5)

            if (len(characterList) == 1):
                winnerOne = characterList[0].winner()
                print("\nMATCH is OVER!")
                print(f"Winner : {winnerOne}")
                input()
                break

    elif (len(characterList) == 1):
        winnerTwo = characterList[0].winner()
        print("\nMATCH is OVER!")
        print(f"Winner: {winnerTwo}")
        input()
        break

    else:
        print("All character is dead. Not winner!")
        input()
        break
