class Node:
  def __init__(self,value,tail):
    self.isEmpty = False
    self.value = value
    self.tail = tail

class Empty:
  tail = None
  prev = None
  def __init__(self):
    self.isEmpty = True
  def setTail(self, tail):
    self.tail = tail
  def setPrev(self, node):
    self.prev = node

def pushSavings(actualValues, saveTo):
  if actualValues.isEmpty:
    return pushSavings(actualValues.tail)
  else:
    if saveTo.isEmpty:
      return pushSavings(actualValues, saveTo.tail)
    elif actualValues.value[0] == saveTo.value[0]:
      tempSave = saveTo
      tempSave.value[1] = actualValues.value[1]
      return tempSave
    else:
      return pushSavings(actualValues, saveTo.tail)


def RoundOff(list,firstItem=None):
  tempFirst = firstItem
  if firstItem == None:
    tempFirst = list

  if list.isEmpty:
    list.setTail(tempFirst)
  else:
    RoundOff(list.tail,tempFirst)

def removePlayer(list, firstItem=None):
  tempFirst = firstItem
  if firstItem == None:
    if list.isEmpty == True:
      return
    tempFirst = list

  if list.isEmpty == True:
      list.prev.tail = list.tail
      return removePlayer(list.tail,tempFirst)

  else:
    if list.tail == firstItem:
      listStorage = firstItem.tail
      list.tail = Empty()
      list.tail.setTail(listStorage)
      list.tail.setPrev(list)
      print("test")
      return list
    else:
      return removePlayer(list.tail,tempFirst)

def getLastOne(currentPlayer):
  if currentPlayer.isEmpty:
    return currentPlayer.tail
  else:
    return currentPlayer


def addChips(currentPlayer, chips):
  intermediateValue = currentPlayer.value[1] + chips
  tempPlayer = currentPlayer
  tempPlayer.value[1] = intermediateValue
  return tempPlayer

def reorder(list, firstItem=None):
  tempFirst = firstItem
  if firstItem == None:
    if list.isEmpty == True:
      return
    tempFirst = list

  if list.isEmpty == True:
    if list.tail != tempFirst:
      list.prev.tail = list.tail
      reorder(list.tail,tempFirst)
    else:
      pass #No action required, as thing is in right order

  else:
    if list.tail == firstItem:
      tempStorage = list.tail
      list.tail = Empty()
      list.tail.setTail(tempStorage)
      list.tail.setPrev(list)
    else:
      reorder(list.tail,tempFirst)
    


      #Haal empty weg
    #Plaats empty voor same node
  #Reordering van Raise -> die moet eerst staan

def objectiveCount(list,hasEmpty=False):
  tempHasEmpty = hasEmpty
  if list.isEmpty == True and hasEmpty == False:
    return objectiveCount(list.tail,True)
  elif tempHasEmpty == True:
    if list.isEmpty:
      return 0
    else:
      return 1 + objectiveCount(list.tail, True)
  else:
    return objectiveCount(list.tail, False)
  

def count(list):
  if list.isEmpty == True:
    return 0
  else:
    return count(list.tail) + 1

def tryParse(inp):
  try:
    result = int(inp) 
    return result
  except:
    return None

def roundUpPot(list):
  if list.isEmpty == True:
    return 0
  else:
    value = list.value[2]
    list.value[2] = 0
    return roundUpPot(list.tail) + value

def checkEmpty(list):
  if list.isEmpty == True:
    return list
  else:
    if list.value[1] <= 0:
      return checkEmpty(list.tail)
    else:
      return Node(list.value, checkEmpty(list.tail))
