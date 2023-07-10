import time

class ValueInterpreter:

    def varTypeCheck(self):
        x = input("Write an appropiate variable value:\n")
        a = self.interpret(x)
        if a == "error":
            input('Unrecognized data type, try again! (press "Enter" to continue)')
            self.startProgram()
        else:
            print("Variable:", x, type(a))
            time.sleep(1)
            self.startProgram()
    
    def interpret(self, val):                    
        try:
            return eval(val)
        except:
            return "error"
              
    def startProgram(self):
        chooseVar = input('Do you want to test a variable type in Python? (y/n)\n')
        if chooseVar == "y":
            self.varTypeCheck()
        elif chooseVar == "n":
            input("Exiting program...")
        else:
            input('Please input a valid answer and try again! (press "Enter" to continue)')        
            self.startProgram()
        
exampleObject = ValueInterpreter()

if __name__ == __name__:
    exampleObject.startProgram()    

