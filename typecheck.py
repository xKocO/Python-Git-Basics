import time
import cmd

class ValueInterpreter(cmd.Cmd):
     
    def __init__(self):
        super().__init__()
        self.doc_header = "Hello there, what do you want to do? (type help <command>)"
     
    def do_TypeCheck(self, val):                    
        try:
            print("Variable: ", val, type(eval(val)))
        except:
            print("Unrecognized data type, try again!")
    
    def help_TypeCheck(self):
        print("Type 'TypeCheck <value>' with an apropiate Python value and it will return the data type")
    
    def do_Exit(self, line):
        print("Exiting program...")
        time.sleep(1)
        return True
        
    def help_Exit(self):
        print("Exits the program")
        
    def preloop(self):
        self.do_help('')
        
if __name__ == '__main__':
    ValueInterpreter().cmdloop()

