import classdef
import globalvars

def Returns_a_Matrix(all_species):
	a_Matrix = []
	for i in range(globalvars.NS):
		a_Matrix[0][i] = all_species[i].nitrogen
		a_Matrix[1][i] = all_species[i].hydrogen
		a_Matrix[2][i] = all_species[i].oxygen
		a_Matrix[3][i] = all_species[i].carbon
	print a_Matrix
	return a_Matrix