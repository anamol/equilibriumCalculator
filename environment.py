""" Defines all environment variables used"""

class Environment():
	Temperature = 298.0  # Kelvin --> Final temperature at equilibrium. Given.
	Pressure = 101.325   # kPa --> Final pressure at equilibrium. Given.
	Patm = 101.325 # kPa --> atmospheric pressure. MUST BE IN SAME UNITS AS PRESSURE.
	kcal_to_kJ = 4.186 # self-explanatory conversion
	R = 1.986   # kcal / (K * kmole)  --> This is the Universal Gas Constant.
	TotalN = 0.1 # kmoles --> This is the total number of kmoles in the system at equilibrium. Initially just a guess.
	NS = 0 # total number of species in the system
	NE = 4 # total number of elements in the system
	