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
	TotalN = 0.1
	N = []
	UnderRelaxParameter = 0.0

	def __init__(self, env):
		self.env = env

	def CalculateEquilibrium(self):
		self.N = [(self.TotalN/self.env.NS + 0.001) for x in xrange(self.env.NS)]
		self.aMatrix = self.__CalculateaMatrix()
		self.__CalculateEntropyEnthalpyGibbsE()
		self.AMatrix = self.__CalculateAMatrix()

	def __CalculateaMatrix(self):
		self.aMatrix = [[0.0 for x in xrange(self.env.NS)] for x in xrange(4)]
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
	
	def __CalculateAMatrix(self):
		self.AMatrix = [[0.0 for x in xrange(self.env.NE + 1)] for x in xrange(self.env.NE + 1)]
		self.AMatrix[4][4] = -self.TotalN
		for i in range(0, self.env.NE):
			for j in range(0, self.env.NS):
				self.AMatrix[i][0] = self.AMatrix[i][0] + self.aMatrix[0][j] * self.aMatrix[i][j] * self.N[j]
				self.AMatrix[i][1] = self.AMatrix[i][1] + self.aMatrix[1][j] * self.aMatrix[i][j] * self.N[j]
				self.AMatrix[i][2] = self.AMatrix[i][2] + self.aMatrix[2][j] * self.aMatrix[i][j] * self.N[j]
				self.AMatrix[i][3] = self.AMatrix[i][3] + self.aMatrix[3][j] * self.aMatrix[i][j] * self.N[j]
				self.AMatrix[i][4] = self.AMatrix[i][4] + self.aMatrix[i][j] * self.N[j]
		
		for i in range(0, self.env.NE):
			for j in range(0, self.env.NS):
				self.AMatrix[4][i] = self.AMatrix[4][i] + self.aMatrix[i][j] * self.N[j]

		for j in range(self.env.NS):
			self.AMatrix[4][4] = self.AMatrix[4][4] + self.N[j]

		return self.AMatrix


	def __CalculateCMatrix(self):
		pass

	def __CalculateRMatrix(self):
		pass

	def __CalculateNewN(self):
		pass




	