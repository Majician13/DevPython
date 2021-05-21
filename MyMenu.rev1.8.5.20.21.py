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

    def dictMenu(self, strCmd):
        return strCmd == self.strCmd
    # end def

    def Execute(self):
        self.fnCmdHandler()
    # end def

    def ShouldExit(self):
        return self.bShouldExit
    # end def
#end class

def PromptCommand():
    # Prompts the console user, and returns the string of typed text
    strIn=input("Enter command: ")
    return strIn
# end def

def Cmd_CalculateSine():
    # Prompts the user for a degrees parameter, then calculates
    # the sine and prints the result to the console.
    strIn = input("Enter angle in degrees > ")
    fDegrees = float(strIn)
    fSine = math.sin(math.radians(fDegrees))
    print("sin(", fDegrees, ") =", fSine)
    Menu()
# end def

def Cmd_CalculateCosine():
    # Prompts the user for a degrees parameter, then calculates
    # the cosine and prints the result to the console.
    strIn = input("Enter angle in degrees > ")
    fDegrees = float(strIn)
    fCosine = math.cos(math.radians(fDegrees))
    print("cos(", fDegrees, ") =", fCosine)
    Menu()
# end def

def Cmd_CalculateSquareRoot():
    # Prompts the user for a parameter, then calculates
    # the square root and prints the result to the console.
    strIn = input("Enter squared value > ")
    fSquared = float(strIn)
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
    return m_dictCmds[strIn]     
# end def

m_objCmdCalculateSine = MenuCommand(Cmd_CalculateSine, 's')
m_objCmdDisplayMenu = MenuCommand(Cmd_DisplayMenu, '?')
m_objCmdCalculateCosine = MenuCommand(Cmd_CalculateCosine, 'c')
m_objCmdCalculateSquareRoot = MenuCommand(Cmd_CalculateSquareRoot, 'q')
m_objCmdExit = MenuCommand(Cmd_Exit, 'x', True)

m_dictCmds = {}
MenuCommand(Cmd_DisplayMenu, m_dictCmds, '?'),
MenuCommand(Cmd_CalculateCosine, m_dictCmds, 'c'),
MenuCommand(Cmd_CalculateSquareRoot, m_dictCmds, 'q'),
MenuCommand(Cmd_CalculateSine, m_dictCmds, 's'),
MenuCommand(Cmd_Exit, m_dictCmds, 'x', True)

Menu()