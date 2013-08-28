import globalvars
import matrix
import math

class System():

	bMatrix = []
	aMatrix = []
	AllSpecies = []
	AMatrix = []
	RMatrix = []
	CMatrix = []
	DeltaNj = []
	DeltaN = 0.0
	NewN = []
	NewTotalN = 0.0
	N = []
	MoleFraction = []
	MassFraction = []
	UnderRelaxParameter = 0.0
	diff = 1.0
	Iterations = 0
	MinimumDiff = 10**(-8)

	def __init__(self, env):
		self.env = env

	def CalculateEquilibrium(self):
		self.N = [(self.env.TotalN/self.env.NS + 0.001) for x in xrange(self.env.NS)]
		self.aMatrix = self.__CalculateaMatrix()
		while abs(self.diff) > self.MinimumDiff:
			for i in range(self.env.NS):
				self.AllSpecies[i].Nj = self.N[i]
			self.__CalculateEntropyEnthalpyGibbsE()
			self.AMatrix = self.__CalculateAMatrix()
			self.RMatrix = self.__CalculateRMatrix()
			self.CMatrix = self.__CalculateCMatrix()
			self.DeltaNj = self.__CalculateDeltaNj()
			self.UnderRelaxParameter = self.__CalculateUnderRelaxParameter()
			self.NewN = self.__CalculateNewN()
			self.diff = self.NewTotalN - self.env.TotalN
			self.N = self.NewN
			self.env.TotalN = self.NewTotalN
			self.Iterations += 1
		self.MoleFraction = self.__CalculateMoleFraction()	

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
		self.AMatrix[4][4] = -self.env.TotalN
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

	def __CalculateRMatrix(self):
		self.RMatrix = [0.0 for x in xrange(self.env.NE + 1)]
		self.RMatrix[4] = self.env.TotalN
		for i in range(self.env.NE):
			for j in range(self.env.NS):
				self.RMatrix[i] = self.RMatrix[i] - self.aMatrix[i][j] * self.N[j] + self.aMatrix[i][j] * self.N[j] * self.AllSpecies[j].gibbs_energy/(self.env.R * self.env.kcal_to_kJ * self.env.Temperature)
		for i in range(self.env.NE):
			self.RMatrix[i] = self.RMatrix[i] + self.bMatrix[i]
		for i in range(self.env.NS):
			self.RMatrix[4] = self.RMatrix[4] - self.N[i] + self.N[i] * self.AllSpecies[i].gibbs_energy/(self.env.R * self.env.kcal_to_kJ * self.env.Temperature)

		return self.RMatrix

	def __CalculateCMatrix(self):
		self.CMatrix = [0.0 for x in xrange(self.env.NE + 1)]
		C = matrix.gj_Solve(self.AMatrix, self.RMatrix)
		for i in range(self.env.NE + 1):
			self.CMatrix[i] = C[i][5]
		self.DeltaN = self.CMatrix[4]
		return self.CMatrix

	def __CalculateDeltaNj(self):
		self.DeltaNj = [self.DeltaN for x in xrange(self.env.NS)]
		for j in range(self.env.NS):
			self.DeltaNj[j] = self.DeltaNj[j] - self.AllSpecies[j].gibbs_energy/(self.env.R * self.env.kcal_to_kJ * self.env.Temperature)
			for i in range(self.env.NE):
				self.DeltaNj[j] = self.DeltaNj[j] + self.CMatrix[i] * self.aMatrix[i][j]
		return self.DeltaNj

	def __CalculateUnderRelaxParameter(self):
		SIZE = - math.log(10**(-8))
		e1 = 1.0
		e2 = 1.0
		temp = 0.0
		for i in range(self.env.NS):
				if abs(self.DeltaNj[i]) >= temp:
					temp = abs(self.DeltaNj[i])
				#if math.log(self.N[i]/self.env.TotalN) <= -SIZE and self.DeltaNj[i] >= 0:
				#	e2 = min(abs((-math.log(self.N/self.env.TotalN) - 9.2103404)/(self.DeltaNj[i] - self.DeltaN)))
		e1 = 2 / max(5 * abs(self.DeltaN), temp)
		return min(1, e1,e2)

	def __CalculateNewN(self):
		self.NewN = [0.0 for x in xrange(self.env.NS)]
		for i in range(self.env.NS):
			self.NewN[i] = math.exp(self.UnderRelaxParameter * self.DeltaNj[i] + math.log(self.N[i]))
		self.NewTotalN = math.exp(self.UnderRelaxParameter * self.DeltaN + math.log(self.env.TotalN))
		return self.NewN

	def __CalculateMoleFraction(self):
		self.MoleFraction = [self.N[x]/self.env.TotalN for x in xrange(self.env.NS)]
		return self.MoleFraction






	