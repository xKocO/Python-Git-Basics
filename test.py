def variableTypeCheck():
    varTesting = {2, "esta", 6.5, "prueba" : 30}
    print("Variable: ", varTesting, ", Tipo: ", type(varTesting))
    
def variableConversion():
    x = 2.5
    y = 3
    z = 8j    
    print("Unconverted Numbers: ", "\n", "x: ", x ,type(x), "\n", "y: ", y , type(y), "\n", "z: ", z, type(z), "\n")    
    
    x = 2
    y = 3.5
    print("Converted Numbers: ", "\n", "x: ", x ,type(x), "\n", "y: ", y , type(y), "\n", "z: ", z, type(z), "Can't convert complex numbers", "\n")
    
    #a = int(x)
    #b = float(y)
    #print("Converted using other variables: ", "\n", a , type(a), "\n", b , type(b))
    
def stringTesting():
    string_var = str(5.4)
    print("Testing python string function with other variable types: " ,string_var)

def stringArrayCheck(x):
    strArrayVar = "012345"
    print("The character on the array position is: " ,strArrayVar[x])
    


