from List import *
import copy
import os

clear = lambda: os.system('cls')

class Game:
  data = ""
  def __init__(self,playerData):
    self.data = playerData
    self.pot = 0
    self.currentBet = 0
    self.folded = 0
    self.winner = ""
    RoundOff(self.data)

  def getData(self):
    a = copy.deepcopy(self.data)
    return a

  def addPot(self,value):
    self.pot += value

  def assignPot(self,player):
    player = addChips(getLastOne(player), self.pot)
    self.pot = 0
    self.currentBet = 0
    return player


  def checkEmpty(self):
    self.data = checkEmpty(self.data)

  def defaultPrint(self, currentPlayer):
    if currentPlayer.isEmpty:
      defaultPrint(currentPlayer.tail)
    else:
      print("Current Turn: " + currentPlayer.value[0])
      print("Pot: " + str(self.pot))
      print("Current Bet: " + str(self.currentBet))
      print("Your bet: " + str(currentPlayer.value[2]))
      print("Your chips: " + str(currentPlayer.value[1]))
      print("------------")

  def fold(self,currentPlayer):
    self.pot += currentPlayer.value[2]
    currentPlayer.value[2] = 0
    self.folded += 1
    self.data = saveCurrentValues(currentPlayer, self.data)
    return removePlayer(currentPlayer)

  def bet(self,currentPlayer,chips):
    currentPlayer.value[2] += chips
    currentPlayer.value[1] -= chips
    if currentPlayer.value[2] > self.currentBet:
      reorder(currentPlayer)
      self.currentBet = currentPlayer.value[2]
    return currentPlayer

  def call(self,currentPlayer):
    betValue = self.currentBet - currentPlayer.value[2]
    currentPlayer.value[1] -= betValue
    currentPlayer.value[2] += betValue
    return currentPlayer

  def actualBet(self, currentPlayer):
    message = ""
    while True:
      clear()
      self.defaultPrint(currentPlayer)
      if message != "": print(message)
      message = ""
      choice = input("How much do you want to bet? [fold]")
      if tryParse(choice) != None:
        if tryParse(choice) > currentPlayer.value[1]:
          message = "You don't have that much"
        elif tryParse(choice) < 0:
          message = "You can't bet less than 0"
        elif tryParse(choice) + currentPlayer.value[2] < self.currentBet:
          message = "Bet too little to call"
        else:
          if tryParse(choice) == 0:
            return currentPlayer
          else:
            return self.bet(currentPlayer,tryParse(choice))
      elif str.lower(choice) == "fold":
        return self.fold(currentPlayer)

  def checkFold(self):
    if objectiveCount(self.getData()) - self.folded == 1:
      return True
    else:
      return False

  def checkEnd(self,currentPlayer):
    if objectiveCount(currentPlayer) <= 1:
      return True
    else:
      return False
  
  def endRound(self,currentPlayer):
    self.addPot(roundUpPot(currentPlayer))
    self.currentBet = 0
    return self.checkEnd(currentPlayer)

  def askBet(self, currentPlayer):
    message = ""
    while True:
      clear()
      self.defaultPrint(currentPlayer)
      if message != "":
        print(message)
        message = ""
      if self.currentBet == currentPlayer.value[2]:
        choice = str.lower(input("What do you want to do? [check/bet/fold]"))
        if choice == "check":
          return currentPlayer
        elif choice == "bet":
          return self.actualBet(currentPlayer)
        elif choice == "fold":
          return self.fold(currentPlayer)
      else:
        choice = str.lower(input("What do you want to do? [call/raise/fold]"))
        if choice == "call":
          if (self.currentBet - currentPlayer.value[2]) > currentPlayer.value[1]:
            message = "Can't call, you lack the chips"
          else:
            return self.call(currentPlayer)
        elif choice == "raise":
          return self.actualBet(currentPlayer)
        elif choice == "fold":
          return self.fold(currentPlayer)
        

  def Game(self):
    while True:
      round = 0
      gameData = self.getData()
      done = 0
      self.folded = 0
      while True:
        done = 0
        while True:

          clear()

          self.defaultPrint(gameData)
          gameData = self.askBet(gameData)
          print(round)

          if self.checkFold():
            done = 1
            break
          

          if (gameData.tail.isEmpty):
            if not self.endRound(gameData.tail.tail):
              gameData = gameData.tail.tail
              break
            else:
              done = 1
              break
          else:
            gameData = gameData.tail
        if done == 1:
          if gameData.isEmpty:
            gameData = gameData.tail
          gameData = self.assignPot(gameData)
          pushSavings(gameData, self.data)
          break
