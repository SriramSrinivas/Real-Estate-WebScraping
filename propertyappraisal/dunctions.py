import random
randomNumberArray=[]


totalSum=0.00
average=0.00

def generateRandomNumbers():
	for x in range(10):
		randomNumberArray.append(random.randint(0,10))


def test():
    print (hello)

def sum1():
    # print(sum(randomNumberArray)) 
    sumValue=0.00
    for x in randomNumberArray:
        sumValue=sumValue+x
        print(sumValue)

def avg():
    average=(sum(randomNumberArray))/len(randomNumberArray)  
    print(average)


def multiple():
    multiply=1
    for x in randomNumberArray:
      multiply=x*multiply
    #   print(multiply)
    #  print(multiply)

# print (randomNumberArray)
generateRandomNumbers()
# print (randomNumberArray)
sum1()
avg()
test()
# multiple()
# print(average)
