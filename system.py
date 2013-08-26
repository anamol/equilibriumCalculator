import globalvars

class System():

	bMatrix = []
	aMatrix = []
	AllSpecies = []
	AMatrix = []
	RMatrix = []
	CMatrix = []
	DeltaNj = []
	NewN = []

	def __init__(self, env):
		self.env = env

	def CalculateEquilibrium(self):
		self.aMatrix = self.__CalculateaMatrix()
		self.__CalculateEntropyEnthalpyGibbsE()
		

	def __CalculateaMatrix(self):
		self.aMatrix = [[0 for x in xrange(self.env.NS)] for x in xrange(4)]
		for i in range(0, self.env.NS):
			self.aMatrix[0][i] = self.AllSpecies[i].nitrogen
			self.aMatrix[1][i] = self.AllSpecies[i].hydrogen
			self.aMatrix[2][i] = self.AllSpecies[i].oxygen
			self.aMatrix[3][i] = self.AllSpecies[i].carbon
		return self.aMatrix

	def __CalculateEntropyEnthalpyGibbsE(self):
		for i in self.AllSpecies:
			i.enthalpy = i.calculates_enthalpy_difference()
			i.calculates_entropy()
			i.calculates_gibbs_energy()	

	