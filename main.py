import system
import inputmod
import globalvars
import sys

environmentvariable = globalvars.Environment()
system = system.System(environmentvariable)
inputmodule = inputmod.InputModule(sys.argv[1], system)

inputmodule.ReadInput()

system.CalculateEquilibrium()





