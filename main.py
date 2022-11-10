import random
def writeToTest(numbers):
    temp = getNumbers(numbers)
    for i in temp:
        print(i,end='')
    print('\n******************************')
    with open('test.txt', 'w') as f:
        f.write(getNumbers(numbers))
def writeToPrime(list):

    with open('prime,txt','w') as f:
        tempStr=''
        counter=0
        for i in list:
            counter+=1
            print(i,end=' ')
            tempStr+=str(i) + ' '
        print(f'\n{counter} prime numbers found in this file')
        f.write(tempStr)

def readTestFile():

    with open('test.txt','r') as f:
        for line in f:
            temp = line.strip().split(' ')
            #data.append(temp)

    return temp

def getPrimes(output):
    list = []
    nl=[]
    for i in output:
        list.append(int(i))

    for k in list:
        if k > 1:
            for j in range(2, k):
                if (k % j) == 0:
                    break
            else:
                nl.append(k)
    return nl
def getNumbers(numbers):
    random.seed(1)
    returnString=''
    for i in range(numbers):
        temp = random.randint(1,100)
        returnString+=str(temp) + ' '
    return returnString

def main():
    numbers = int(input("How many numbers are needed to write to the file: "))
    writeToTest(numbers)
    writeToPrime(getPrimes(readTestFile()))
    extraCredit()


def extraCredit():
    tempList = readTestFile()
    tempSum = 0
    tempNum = 0
    for i in tempList:
        temp = str(i)
        sum=0
        for i in range(len(temp)):
            sum+=int(temp[i])
        if sum > tempSum:
            tempSum = sum
            tempNum = temp
    print('\n******************************')
    print(f'{tempNum} has a maximum sum of digits = {tempSum}')

main()
