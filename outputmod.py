import globalvars
import system
import classdef

class OutputModule():
	OutputSpecies = []

	def __init__(self, filename, system):
		self. filename = filename
		self.system = system

	def WriteOutput(self):
		#self.OutputSpecies = self.__SpecificSpecies()
		with open(self.filename, "w") as OutputFile:
			OutputFile.write('Temperature: ' + str(self.system.env.Temperature) + "\n")
			OutputFile.write("Pressure   : " + str(self.system.env.Pressure) + "\n\n")
			OutputFile.write('Species at equilibrium :' + '\n\n')
			OutputFile.write('Species' + "\t\t" + "Kmoles" + "\t\t\t" + "Mole Fraction" + "\n")
			for i in range(self.system.env.NS):
				OutputFile.write(self.system.AllSpecies[i].name + '\t\t' + str("%.4e" % self.system.N[i]) + "\t\t" + str("%.4e" % self.system.MoleFraction[i]) + "\n")
			

	def __SpecificSpecies(self):
		YorN = raw_input('Do you want to write output for specific species only (Y or N)?:')
		if YorN.lower() == 'n':
			sys.exit()
		elif YorN.lower() == 'y':
			String = raw_input('Enter species, space delimited: \n')
			counter = 0


