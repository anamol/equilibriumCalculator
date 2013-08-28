import system
import inputmod
import outputmod
import globalvars
import sys

environmentvariable = globalvars.Environment()
system = system.System(environmentvariable)
inputmodule = inputmod.InputModule(sys.argv[1], system)

inputmodule.ReadInput()
system.CalculateEquilibrium()

outputfile = raw_input('Enter output filename: ')

outputmodule = outputmod.OutputModule(outputfile, system)
outputmodule.WriteOutput()



