import globalvars
from math import log


class Specie():
	"""
	Defining Class 'Specie' which contains :

	Attributes:
	Name of Specie
	Number of Carbon, Nitrogen, Oxygen and Hydrogen atoms in Specie
	Moles of Specie in final mixture
	Low temp and high temp constants from reaction mechanism to calculate enthalpy, entropy, Gibbs energy
	
	Methods():
	Calculate enthlapy
	Calculate entropy
	Calculate Gibbs Energy
	"""

	name = ""
	carbon = 0
	nitrogen = 0
	hydrogen = 0
	oxygen = 0
	Nj = 0.1 # --> Number of kmoles of Specie at equilibrium. Initially just a guess.
	high_constants = tuple([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
	low_constants = tuple([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
	lower_limit = 200.0  # Kelvin
	higher_limit = 3500.0  # Kelvin
	middle_limit = 1000.0  # Kelvin

	def __init__(self):
		self.enthalpy = 0.0  # kJ/kmole
		self.entropy = 0.0  # kJ/kmole
		self.gibbs_energy = 0.0  # kJ/kmole

	def prints_all(self):
		print "\n" + self.name,
		print "\t" + str(self.Nj) + " kmoles"
		print "N  " + str(self.nitrogen),
		print "O  " + str(self.oxygen),
		print "H  " + str(self.hydrogen),
		print "C  " + str(self.carbon),
		print "\t" + str(self.lower_limit),
		print "\t" + str(self.higher_limit),
		print "\t" + str(self.middle_limit)
		print self.high_constants
		print self.low_constants

	def calculates_enthalpy_difference(self):
		if (globalvars.Temperature >= self.lower_limit and globalvars.Temperature <= self.middle_limit):
			self.enthalpy = self.low_constants[5] * globalvars.R
			for i in range(5):
				self.enthalpy = self.enthalpy + (self.low_constants[i] * globalvars.R * (globalvars.Temperature ** (i + 1)))/(i + 1)
			self.enthalpy = self.enthalpy * globalvars.kcal_to_kJ  # converts from kcal/kmole to kJ/kmole	
			return self.enthalpy	

		elif (globalvars.Temperature > self.middle_limit and globalvars.Temperature <= self.higher_limit):
			self.enthalpy = self.high_constants[5] * globalvars.Temperature * globalvars.R
			for i in range(5):
				self.enthalpy = self.enthalpy + (self.high_constants[i] * globalvars.R * (globalvars.Temperature ** (i + 1)))/(i + 1)
			self.enthalpy = self.enthalpy * globalvars.kcal_to_kJ     # converts from kcal/kmole to kJ/kmole	
			return self.enthalpy	

		else :
			print "Temperature out of range. Try again with Temperature between " + str(self.lower_limit) + " and " + str(self.higher_limit)

	def calculates_entropy(self):
		if (globalvars.Temperature >= self.lower_limit and globalvars.Temperature <= self.middle_limit):
			self.entropy = self.low_constants[0] * globalvars.R * log(globalvars.Temperature) + self.low_constants[6] * globalvars.R
			for i in range(1, 5):
				self.entropy = self.entropy + (self.low_constants[i] * (globalvars.Temperature ** i))/i
			self.entropy = self.entropy * globalvars.kcal_to_kJ  # converts from kcal/(K * kmole) to kJ/(K * kmole)
			return self.entropy

		elif (globalvars.Temperature > self.middle_limit and globalvars.Temperature <= self.higher_limit):
			self.entropy = self.high_constants[0] * globalvars.R * log(globalvars.Temperature) + self.high_constants[6] * globalvars.R
			for i in range(1, 5):
				self.entropy = self.entropy + (self.high_constants[i] * (globalvars.Temperature ** i))/i
			self.entropy = self.entropy * globalvars.kcal_to_kJ   # converts from kcal/(K * kmole) to kJ/(K * kmole)
			return self.entropy

		else :
			print "Temperature out of range. Try again with Temperature between " + str(self.lower_limit) + " and " + str(self.higher_limit)

	def calculates_gibbs_energy(self):
		self.calculates_entropy()
		self.calculates_enthalpy_difference()
		self.gibbs_energy = self.enthalpy - globalvars.Temperature * self.entropy + globalvars.R * globalvars.kcal_to_kJ * globalvars.Temperature * (log(self.Nj/globalvars.N) + log(globalvars.Pressure/globalvars.Patm))
		return self.gibbs_energy




