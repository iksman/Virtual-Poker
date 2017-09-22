from List import Empty, Node, tryParse
import Game

class InitData:
  players = 0
  chips = 0
  def __init__(self):
    pass
  def setPlayer(self, players):
    self.players = players
  def setChips(self, chips):
    self.chips = chips

initData = InitData()

def checkPlayers(data):
  if type(data) == InitData:
    while True:
      players = input("Players: ")
      result = tryParse(players)
      if result != None:
        data.setPlayer(result)
        break

def checkChips(data):
  if type(data) == InitData:
    while True:
      chips = input("Chips: ")
      result = tryParse(chips)
      if result != None:
        data.setChips(result)
        break

def buildData(initData):
  dataArray = Empty()
  for i in range (0,initData.players):
    playername = input("Player " + str(i + 1) + " name (12 chars max): ")[:12]
    dataArray = Node([playername, initData.chips, 0], dataArray)
    if dataArray.tail.isEmpty:
      dataArray.tail.setPrev(dataArray)
  return dataArray

while True:
  checkPlayers(initData)
  checkChips(initData)
  PlayerData = buildData(initData)
  game = Game.Game(PlayerData)
  game.Game()


  


