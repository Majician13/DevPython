# DevPython
# Various programs from Software Development I: Python Book
# Testing following a github guide.
# Inserted Lesson 33: An Exceptional Dictionary - By Software Development 1: With Python by Tom Baugh
# Rev1.7 --- Changed while loop to for loop. 

import math

class MenuCommand:
    # Class to manage menu commands
    def __init__(self, fnCmdHandler, strCmd, bShouldExit = False):
        self.fnCmdHandler = fnCmdHandler
        self.strCmd = strCmd
        self.bShouldExit = bShouldExit
    # end def __init))

    def CompareCmd(self, strCmd):
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

def Cmd_CalculateSine():
    # Prompts the user for a degrees parameter, then calculates
    # the sine and prints the result to the console.
    strIn = input("Enter angle in degrees > ")
    fDegrees = float(strIn)
    fSine = math.sin(math.radians(fDegrees))
    print("sin(", fDegrees, ") =", fSine)
    Menu()

def Cmd_CalculateCosine():
    # Prompts the user for a degrees parameter, then calculates
    # the cosine and prints the result to the console.
    strIn = input("Enter angle in degrees > ")
    fDegrees = float(strIn)
    fCosine = math.cos(math.radians(fDegrees))
    print("cos(", fDegrees, ") =", fCosine)
    Menu()

def Cmd_CalculateSquareRoot():
    # Prompts the user for a parameter, then calculates
    # the square root and prints the result to the console.
    strIn = input("Enter squared value > ")
    fSquared = float(strIn)
    fSquareRoot = math.sqrt(fSquared)
    print("Square root of", fSquared, " =", fSquareRoot)

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
    # nLength = len(m_lstCmds)
    # nIndex = 0

    # while nIndex < nLength:
        # objCmd = m_lstCmds[nIndex]
    for objCmd in m_lstCmds:
        if objCmd.CompareCmd(strIn):
            return objCmd
        # nIndex += 1
    # end for/while
    else:
        print("Command [" + strIn + "] not recognized")
        return None
    # end if      
# end def

m_objCmdCalculateSine = MenuCommand(Cmd_CalculateSine, 's')
m_objCmdDisplayMenu = MenuCommand(Cmd_DisplayMenu, '?')
m_objCmdCalculateCosine = MenuCommand(Cmd_CalculateCosine, 'c')
m_objCmdCalculateSquareRoot = MenuCommand(Cmd_CalculateSquareRoot, 'q')
m_objCmdExit = MenuCommand(Cmd_Exit, 'x', True)

m_lstCmds = [MenuCommand(Cmd_DisplayMenu, '?'),
             MenuCommand(Cmd_CalculateCosine, 'c'),
             MenuCommand(Cmd_CalculateSquareRoot, 'q'),
             MenuCommand(Cmd_CalculateSine, 's'),
             MenuCommand(Cmd_Exit, 'x', True)]

Menu()
