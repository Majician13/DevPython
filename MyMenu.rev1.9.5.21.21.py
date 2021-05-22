# Rev1.8 --- Implemented Dictionaries and Exceptions.  Removed Lists.

import math

class MenuCommand:
    # Class to manage menu commands
    def __init__(self, fnCmdHandler, dictMenu, strCmd, bShouldExit = False):
        self.fnCmdHandler = fnCmdHandler
        self.strCmd = strCmd
        dictMenu[strCmd] = self
        self.bShouldExit = bShouldExit
    # end def __init__

    def compareCmd(self, strCmd):
        return strCmd == self.strCmd
    # end def

    def Execute(self):
        self.fnCmdHandler()
    # end def

    def ShouldExit(self):
        return self.bShouldExit
    # end def
# end class

def PromptCommand():
    # Prompts the console user, and returns the string of typed text
    strIn=input("Enter command: ")
    return strIn
# end def

def Cmd_CalculateSine():
    # Prompts the user for a degrees parameter, then calculates
    # the sine and prints the result to the console.
    while True:
        strIn = input("Enter angle in degrees > ")
        try:
            fDegrees = float(strIn)
            break
        except ValueError:
            print(strIn, ' is not a valid sine parameter in degrees')
        # end try
    # end while
    fSine = math.sin(math.radians(fDegrees))
    print("sin(", fDegrees, ") =", fSine)
    Menu()
# end def

def Cmd_CalculateCosine():
    # Prompts the user for a degrees parameter, then calculates
    # the cosine and prints the result to the console.
    while True:
        strIn = input("Enter angle in degrees > ")
        try:
            fDegrees = float(strIn)
            break
        except ValueError:
            print(strIn, ' is not a valid cosine parameter in degrees')
        # end try
    # end while
    fCosine = math.cos(math.radians(fDegrees))
    print("cos(", fDegrees, ") =", fCosine)
    Menu()
# end def

def Cmd_CalculateSquareRoot():
    # Prompts the user for a parameter, then calculates
    # the square root and prints the result to the console.
    while True:
        strIn = input("Enter squared value > ")
        try:
            fSquared = float(strIn)
            if fSquared < 0.0:
                print('Negative numbers are not allowed')
                continue
            # end if
            break
        except ValueError:
            print(strIn, ' is not a valid square-root parameter')
        # end try
    # end while
    fSquareRoot = math.sqrt(fSquared)
    print("Square root of", fSquared, " =", fSquareRoot)
# end def

def Cmd_DisplayMenu():
    # Displays the program menu
    print("")
    print("Available commands")
    print("? - display this menu")
    print("c - cosine of angle in degrees")
    print("q - square root")
    print("s - sine of angle in degrees")
    print("x to exit")
    print("")
# end def

def Cmd_Exit():
    # Exits the program
    print("Bye!")
    quit()
# end def
    
def Menu():
    while True:
        strIn = PromptCommand()
        objCmd = GetMenuCommand(strIn)
        if None == objCmd: continue
        objCmd.Execute()
        if objCmd.ShouldExit(): break                
    # end while

def GetMenuCommand(strIn):
    try:
        return m_dictCmds[strIn]
    except KeyError:
        print('Command [' + strIn + '] not recognized')
        return None
    # end try  
# end def

m_dictCmds = {}
m_objCmdCalculateSine = MenuCommand(Cmd_CalculateSine, m_dictCmds, 's')
m_objCmdDisplayMenu = MenuCommand(Cmd_DisplayMenu, m_dictCmds, '?')
m_objCmdCalculateCosine = MenuCommand(Cmd_CalculateCosine, m_dictCmds, 'c')
m_objCmdCalculateSquareRoot = MenuCommand(Cmd_CalculateSquareRoot, m_dictCmds, 'q')
m_objCmdExit = MenuCommand(Cmd_Exit, m_dictCmds, 'x', True)

MenuCommand(Cmd_DisplayMenu, m_dictCmds, '?'),
MenuCommand(Cmd_CalculateCosine, m_dictCmds, 'c'),
MenuCommand(Cmd_CalculateSquareRoot, m_dictCmds, 'q'),
MenuCommand(Cmd_CalculateSine, m_dictCmds, 's'),
MenuCommand(Cmd_Exit, m_dictCmds, 'x', True)

Menu()