def mean(listT):
    total = 0
    times = 0
    for i in listT:
      total += i
      times += 1
      if times >= len(listT):
        return total / len(listT)
    return total / len(listT)

def linearSearch(listToSearch, looking):
  v = 0
  for i in listToSearch:
    if i == looking:
      return v
    v += 1
  return -1

def binarySearch(listToSearch, looking):
  listLength = len(listToSearch)
  eliminationPointMin = 0
  eliminationPointMax = listLength
  
  while True:
    numCheckingIndex = int((eliminationPointMax + eliminationPointMin) / 2)
    numChecking = listToSearch[numCheckingIndex]

    if looking == numChecking:
      return numCheckingIndex
    elif looking > numChecking:
      eliminationPointMin = numChecking
    elif looking < numChecking:
      eliminationPointMax = numChecking - 1
    # else:
    #   return numCheckingIndex

def fibonacciSearch(listToSearch, looking):
  size = len(listToSearch)
  start = -1
   
  f0 = 0
  f1 = 1
  f2 = 1
  while(f2 < size):
      f0 = f1
      f1 = f2
      f2 = f1 + f0
  while(f2 > 1):
      index = min(start + f0, size - 1)
      if listToSearch[index] < looking:
          f2 = f1
          f1 = f0
          f0 = f2 - f1
          start = index
          print(listToSearch[index])
      elif listToSearch[index] > looking:
          f2 = f0
          f1 = f1 - f0
          f0 = f2 - f1
      else:
          return index
      print(listToSearch[index])
  if (f1) and (listToSearch[size - 1] == looking):
      return size - 1
  return None