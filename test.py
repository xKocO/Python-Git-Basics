import sys
import keyboard

class BeginnerExample:

    def varTypeCheck(self):
        x = input("Write an apropiate variable value:\n")
        a = self.interpret(x)
        if a == "error":
            print("Unrecognized data type, try again! (press any key to continue)")
            wait()
            self.startProgram()
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
                return range(int(val[6:]))
            except:
                return "error"
        elif val.startswith("'") and val.endswith("'") or val.startswith('"') and val.endswith('"'):
            try:
                return str(val)
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

def wait():
    keyboard.read_key()
    
exampleObject = BeginnerExample()

def startProgram():
    chooseVar = input('Do you want to test a variable type on Python? (y/n)\n')
    if chooseVar == "y":
        exampleObject.varTypeCheck()
    elif chooseVar == "n":
        print("Exiting program...")
    else:
        print('Please input a valid answer and try again! (press any key to continue)')
        wait()
        startProgram()

if __name__ == __name__:
    startProgram()    

