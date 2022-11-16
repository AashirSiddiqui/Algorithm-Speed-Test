import algorithms, time, statistics

file = open("stats.txt", "w")

testList = []
for i in range(1, 101):
  testList.append(i)

linearTimes = []
for looking in testList:
  startTime = time.time()
  print()
  a = algorithms.linearSearch(testList, looking)
  elapsedTime = time.time() - startTime
  linearTimes.append(elapsedTime)

file.write("Linear Search: " + str(round(statistics.mean(linearTimes) * 100, 5)) + "\n")

binaryTimes = []
for looking in testList:
  startTime = time.time()
  print()
  a = algorithms.binarySearch(testList, looking)
  elapsedTime = time.time() - startTime
  binaryTimes.append(elapsedTime)

file.write("Binary Search: " + str(round(statistics.mean(binaryTimes) * 100, 5)) + "\n")

fibonacciTimes = []
for looking in testList:
  startTime = time.time()
  print()
  a = algorithms.fibonacciSearch(testList, looking)
  elapsedTime = time.time() - startTime
  fibonacciTimes.append(elapsedTime)

file.write("Fibonacci Search: " + str(round(statistics.mean(fibonacciTimes) * 100, 5)) + "\n")
file.close()