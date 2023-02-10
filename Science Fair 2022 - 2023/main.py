import statistics, time, algorithms

linear = open("linear.txt", "w")
binary = open("binary.txt", "w")
fibonacci = open("fibonacci.txt", "w")

testList = []
for i in range(1, 1001):
  testList.append(i)

for i in range(1, 26):

  linearTimes = []
  for looking in testList:
    startTime = time.time()
    print()
    a = algorithms.linearSearch(testList, looking)
    elapsedTime = time.time() - startTime
    linearTimes.append(elapsedTime)

  linear.write(str(round(statistics.mean(linearTimes) * 100, 5)) + "\n")

  binaryTimes = []
  for looking in testList:
    startTime = time.time()
    print()
    a = algorithms.binarySearch(testList, looking)
    elapsedTime = time.time() - startTime
    binaryTimes.append(elapsedTime)

  binary.write(str(round(statistics.mean(binaryTimes) * 100, 5)) + "\n")

  fibonacciTimes = []
  for looking in testList:
    startTime = time.time()
    print()
    a = algorithms.fibonacciSearch(testList, looking)
    elapsedTime = time.time() - startTime
    fibonacciTimes.append(elapsedTime)

  fibonacci.write(str(round(statistics.mean(fibonacciTimes) * 100, 5)) + "\n")

linear.close()
binary.close()
fibonacci.close()