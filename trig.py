# Class for trigonometry
# Written by: Justin Blacksher
#
#
class Trig():
    def __init__(self, opposite, adjacent, hypotenuse):
        '''Creates a right angled triangle object.'''

        # Create the sides
        self.opposite = opposite
        self.adjacent = adjacent
        self.hypotenuse = hypotenuse

        # Evaluation Variables
        '''Variables will be set to true after evaluation of the input text
           After evaluated the program will then decide which functions it 
           Needs to execute to aquire all the information about a triangle.'''
        self.hasOpp = False     # Sets to true if it exists in evaluation
        self.hasAdj = False     # Sets to true if it exists in evaluation
        self.hasHyp = False     # Sets to true if it exists in evaluation
        self.hasSin = False     # Sets to true if it exists in evaluation
        self.hasCos = False     # Sets to true if it exists in evaluation
        self.hasTan = False     # Sets to true if it exists in evaluation
        self.hasCsc = False     # Sets to true if it exists in evaluation
        self.hasSec = False     # Sets to true if it exists in evaluation
        self.hasCot = False     # Sets to true if it exists in evaluation

        # Create the sin,cos,tan variables
        self.sin = 0        # Is found by opposite/hypotenuse
        self.cos = 0        # Is found by adjacent/hypotenuse
        self.tan = 0        # Is found by opposite/adjacent
        self.csc = 0        # Is found by hypotenuse/opposite
        self.sec = 0        # Is found by hypotenuse/adjacent
        self.cot = 0        # Is found by adjacent/opposite

    def getOpposite(self):
        '''Returns the opposite side of the triangle'''
        return self.opposite

    def getAdjacent(self):
        '''Returns the adjacent side of the triangle'''
        return self.adjacent

    def getHypotenuse(self):
        '''Returns the hypotenuse side of the triangle'''
        return self.hypotenuse

    def getCosecant(self):
        '''Returns the CoSecant of the triangle'''
        return self.csc

    def getSecant(self):
        '''Returns the Secant of the Triangle'''
        return self.sec

    def getCotangent(self):
        '''Returns the Cosecant of the Triangle'''
        return self.cot

    def getCos(self):
        '''Returns the value of Cos'''
        return self.cos

    def getTan(self):
        '''Returns the value of Tan'''
        return self.tan

    def getSin(self):
        '''Returns the value of Sin'''
        return self.sin

    def setSin(self):
        '''Function to set the Sin'''
        self.sin = self.opposite / self.hypotenuse

    def setCos(self):
        '''Function to set the Cos'''
        self.cos = self.adjacent / self.hypotenuse

    def setTan(self):
        '''Function to set the Tan'''
        self.tan = self.opposite / self.adjacent

    def setCsc(self):
        '''Function to set the Cosecant'''
        self.csc = self.hypotenuse / self.opposite

    def setSec(self):
        '''Function to set the Secant'''
        self.csc = self.hypotenuse / self.adjacent

    def setCot(self):
        '''Function to set the Cotangent'''
        self.cot = self.adjacent / self.opposite

    def setCalc(self):
        '''Calulate the Sin Cos and Tan'''
        self.setSin()
        self.setCos()
        self.setTan()
        self.setCsc()
        self.setSec()
        self.setCot()

