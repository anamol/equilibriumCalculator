import classdef
import globalvars

def Returns_a_Matrix(all_species):
	a_Matrix = [[0 for x in xrange(globalvars.NS)] for x in xrange(4)]
	for i in range(0, globalvars.NS):
		a_Matrix[0][i] = all_species[i].nitrogen
		a_Matrix[1][i] = all_species[i].hydrogen
		a_Matrix[2][i] = all_species[i].oxygen
		a_Matrix[3][i] = all_species[i].carbon
	return a_Matrix