import sys
#Basic functions meant for easy testing on cmd while checking the script   

def interpret(val):
    try:
        return int(val)
    except ValueError:
        try:
            return float(val)
        except ValueError:
            try:
                return list(val)
            except:
                try:
                    return tuple(val)
                except:
                    return val
                           
def varTypeCheck(x):
    #x = input("Write a variable Float, Int, String, List or Touple: ")
    a = interpret(x)
    print("Variable: ", x, type(a))
  
def variableConversion(x,y,a,b):   
    print("From: ", "\n", a , type(a), "\n", b, type(b))
    a = int(x)
    b = float(y)
    print("To: ", "\n", a , type(a), "\n", b , type(b))
    
def stringArrayCheck(x):
    strArrayVar = "012345"
    print("The character on the array position is: " ,strArrayVar[x])
 
#Allows calling any global function on the file, only for testing purposes!
if __name__ == '__main__':
    indice = sys.argv
    globals()[indice[1]](*indice[2:]) 
    
input("Press anything to close the window")
#print(sys.version)
