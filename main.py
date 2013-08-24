import classdef
import globalvars
import FileReader
import sys

with open(sys.argv[1], "r") as input_file:
	globalvars.Temperature = FileReader.Returns_Temperature(sys.argv[1])
	"""globalvars.Pressure = FileReader.Returns_Pressure(input_file)
	b_Matrix = FileReader.Returns_b_Matrix(input_file)"""
	all_species = FileReader.Reads_Chemkin_Format(input_file)






"""all_species = []
all_constants = []
temp = ""
thermo_check = False
reactants_check  = False
parameters_check = False

#filename_1 = raw_input('Enter name of input file (case sensitive): ')
system = new System(new NasaFormatReader(inputFile))
system.init()
system.simulate()
system.getResults()

with open(sys.argv[1], "r") as input_file:
	for line in input_file:
		if line == 'PARAMETERS\n':
			parameters_check = True

		if line == 'REACTANTS\n':
			reactants_check = True

		if line == 'THERMO\n':		
			thermo_check = True		  		
									
		if line == '$\n':
			parameters_check = False
			thermo_check = False
			reactants_check = False

		if line == 'END\n':			
			break					

		if reactants_check == True:
			for i in range(8,)

		if line[-2] == '1' and thermo_check == True:
			globalvars.NS += 1  # increments number of species every time it finds '1' at the end of a line
			current_specie = classdef.Specie()
			
			for i in line:						# 
				if i != ' ':					#  
					current_specie.name += i    #  Stores name of specie in current_specie.name
				elif i == ' ':					#
					break						#
			if current_specie.name == 'AR':		#  Skips Argon cause it stays Argon
				globalvars.NS -= 1 				#
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
				line = input_file.next()							#
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

for i in range(0,globalvars.NS):									#  Adds constants from all_constants to high_constants and 
	all_species[i].high_constants = tuple(all_constants[i][:7])		#  low_constants for each specie in all_species
	all_species[i].low_constants = tuple(all_constants[i][7:14])	#

for i in all_species:
	i.prints_all()"""