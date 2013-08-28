import environment
import system
import linecache
import classdef

class InputModule():
	def __init__(self, filename, system):
		self.filename = filename
		self.system = system
	
	def ReadInput(self):
		with open(self.filename, "r") as InputFile:
			self.system.env.Temperature = self.__GetTemperature()
			self.system.env.Pressure = self.__GetPressure()
			self.system.bMatrix = self.__GetbMatrix(InputFile)
			self.system.AllSpecies = self.__ReadChemkinFormat(InputFile)

	def __GetTemperature(self):
		temp = ""
		line = linecache.getline(self.filename,2)
		i = 17
		while line[i] != '\n':
			temp = temp + line[i]
			i += 1
		self.system.env.Temperature = float(temp)
		return self.system.env.Temperature
	
	def __GetPressure(self):
		temp = ""
		line = linecache.getline(self.filename,3)
		i = 17
		while line[i] != '\n':
			temp = temp + line[i]
			i += 1
		self.system.env.Pressure = float(temp)
		return self.system.env.Pressure

	def __GetbMatrix(self, InputFile):
		nitrogen = 0.0
		oxygen = 0.0
		carbon = 0.0
		hydrogen = 0.0
		kmoles = 0.0
		reactants_check = False

		for line in InputFile:
			if line == 'REACTANTS\n':
				reactants_check = True
			if line == '$\n':
				break
			if reactants_check == True and len(line) >= 50 :
				kmoles = float(line[56:67:])
				nitrogen += kmoles * float(line[10 : 13])
				hydrogen += kmoles * float(line[22 : 25])
				oxygen += kmoles * float(line[34 : 37])
				carbon += kmoles * float(line[46 : 49])
		self.system.bMatrix = [nitrogen, hydrogen, oxygen, carbon]
		return self.system.bMatrix

	def __ReadChemkinFormat(self, InputFile):
		all_species = []
		all_constants = []
		temp = ""
		thermo_check = False 

		for line in InputFile:
			if line == 'THERMO\n':		
				thermo_check = True		  		
										
			if line == 'END\n':			
				break					

			if line[-2] == '1' and thermo_check == True:
				self.system.env.NS += 1  # increments number of species every time it finds '1' at the end of a line
				current_specie = classdef.Specie(self.system.env)
				
				for i in line:						# 
					if i != ' ':					#  
						current_specie.name += i    #  Stores name of specie in current_specie.name
					elif i == ' ':					#
						break						#
				if current_specie.name == 'AR':		#  Skips Argon cause it stays Argon
					self.system.env.NS -= 1 				#
					continue						#
				
				for i in range(48, 54):	 # magic numbers	#
					temp += line[i]							#  Stores lower limit from reaction mechanism in current_specie.lower_limit
				current_specie.lower_limit = float(temp)    #
				temp = ""									#
				
				for i in range(57, 64):						#
					temp += line[i]							#  Stores higher limit from reaction mechanism in current_specie.higher_limit
				current_specie.higher_limit = float(temp)	#
				temp = ""									#

				for i in range(67, 74):						#
					temp += line[i]							#  Stores middle limit from reaction mechanism in current_specie.middle_limit
				current_specie.middle_limit = float(temp)	#
				temp = ""									#

				for i in range(24,40, 5):								#
					if line[i] == 'O':									#
						current_specie.oxygen = int(line[i + 4])		#
					elif line[i] == 'H':								#
						current_specie.hydrogen = int(line[i + 4])		#
					elif line[i] == 'C':								#  Figures out no. of H, C, O and N atoms in each specie
						current_specie.carbon = int(line[i + 4])		#              and stores in current.specie
					elif line[i] == 'N':								#
						current_specie.nitrogen = int(line[i + 4])		#
					else:												#
						break											#

				list_of_constants = []									
				for line_counter in range(3):							#
					line = InputFile.next()								#
																		#
					for i in range(0, 61, 15):							#  Figures out all constants and stores in list_of_constants
						for j in range(15):								#				
							temp += line[i + j]							#
																		#
						if i == 60 and line_counter == 2:				#
							break										#
																		#
						list_of_constants.append(float(temp))			#
						temp = ""										#
																		
				all_species.append(current_specie)						#  Appends current_specie to a list of objects, all_species
				all_constants.append(list_of_constants)					#  Appends list_of_constants to a list, all_constants

		for i in range(0,self.system.env.NS):								#  Adds constants from all_constants to high_constants and 
			all_species[i].high_constants = tuple(all_constants[i][:7])		#  low_constants for each specie in all_species
			all_species[i].low_constants = tuple(all_constants[i][7:14])	#

		self.system.AllSpecies = all_species
		return all_species
