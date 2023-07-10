class BeginnerExample:

    def varTypeCheck(self):
        x = input("Write an appropiate variable value:\n")
        a = self.interpret(x)
        if a == "error":
            input('Unrecognized data type, try again! (press "Enter" to continue)')
            startProgram()
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
                        
exampleObject = BeginnerExample()

def startProgram():
    chooseVar = input('Do you want to test a variable type in Python? (y/n)\n')
    if chooseVar == "y":
        exampleObject.varTypeCheck()
    elif chooseVar == "n":
        input("Exiting program...")
    else:
        input('Please input a valid answer and try again! (press "Enter" to continue)')        
        startProgram()

if __name__ == __name__:
    startProgram()    

