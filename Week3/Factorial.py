class factorialDemo:

    def __init__(self):
        self.x = 0

    def getInput(self):
        self.x = input('Input a number to find factorial: ')
        self.x = int(self.x)

    def findFactorial(self):
        if self.x >= 0:
            factorial = 1  
            for i in range(1, self.x + 1):
                factorial *= i
            self.printValidFactorial(self.x,factorial)
        else:
            self.printInvalidFactorial()

    def printInvalidFactorial(self):
        print('Unable to find the factorial of a negative number.')

    def printValidFactorial(self,x,factorial):
        print('Factorial of', x, 'is:', factorial)
    
    def checkInputPrimeOrNot(self):
        for i in range(2,self.x):
            if(self.x % i == 0):
                print(self.x,'is not a prime number')
                break
            else:
                print(self.x,'is a prime number')
                break


demo = factorialDemo()
demo.getInput()
demo.findFactorial()
demo.checkInputPrimeOrNot()
