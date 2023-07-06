"""
import sys
import msvcrt as m

class BegginerExample:

    def varTypeCheck(self):
        x = input("Write a variable Float, Int, String, List, or Tuple: ")
        a = self.interpret(x)
        if a == "error":
            print("Wrong variable format!")
        else:
            print("Variable:", x, type(a))
    
    def interpret(self, val):
        try:
            return int(val)
        except ValueError:
            try:
                return float(val)
            except ValueError:
                try:
                    return list(val)
                except ValueError:
                    try:
                        return tuple(val)
                    except ValueError:
                        return "error"
                        
    def variableConversion(self, x, y, a, b):
        print("From:\n", a, type(a), "\n", b, type(b))
        a = int(x)
        b = float(y)
        print("To:\n", a, type(a), "\n", b, type(b))
        
    def stringArrayCheck(self, x, arrayVar):
        strArrayVar = arrayVar
        print("The array is:", strArrayVar, "The character at the array position is:", strArrayVar[x])


exampleObject = BegginerExample()

def wait():
    m.getch()
    
def startProgram():
    chooseVar = input('Do you want to do a "Variable type check" (vtc), do a "Variable conversion" (vc) or do a "String array check"? (sac)  ')
    if chooseVar == "vct":
        BegginerExample.varTypeCheck()
    elif chooseVar == "vc":
        BegginerExample.variableConversion89
    elif chooseVar == "sac":
        BegginerExample.stringArrayCheck()
    else:
        print('Please input a valid answer and try again! (press any key to continue)')
        wait()
        startProgram()

if __name__ == __name__:
    startProgram()
    
input("Press anything to close the window")
"""

class BegginerExample:

    def varTypeCheck(self):
        x = input("Write a variable Float, Int, String, List, or Tuple: ")
        a = self.interpret(x)
        if a == "error":
            print("Wrong variable format!")
        else:
            print("Variable:", x, type(a))
   
    def interpret(self, val):

        if val.startswith("[") and val.endswith("]"):
            try:
                return list(eval(val))
            except:
                return "error"
        elif val.startswith("(") and val.endswith(")"):
            try:
                return tuple(eval(val))
            except:
                return "error"
        elif 'range' in val:
            try:
                return range(int(val[6]))
            except:
                return "error"
        else:
            try:
                return int(val)
            except ValueError:
                try:
                    return float(val)
                except ValueError:
                    try:
                        return complex(val)
                    except ValueError:
                        return "error"

    def variableConversion(self, x, y, a, b):
        print("From:\n", a, type(a), "\n", b, type(b))
        a = int(x)
        b = float(y)
        print("To:\n", a, type(a), "\n", b, type(b))
        
    def stringArrayCheck(self, x, arrayVar):
        strArrayVar = arrayVar
        print("The array is:", strArrayVar, "The character at the array position is:", strArrayVar[x])

def wait():
    m.getch()


exampleObject = BegginerExample()
exampleObject.varTypeCheck()
print("Press anything to close the window")
wait()