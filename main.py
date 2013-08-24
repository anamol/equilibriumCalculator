import classdef
import globalvars
import FileReader
import sys

with open(sys.argv[1], "r") as input_file:
	globalvars.Temperature = FileReader.Returns_Temperature(sys.argv[1])
	globalvars.Pressure = FileReader.Returns_Pressure(sys.argv[1])
	b_Matrix = FileReader.Returns_b_Matrix(input_file)
	all_species = FileReader.Reads_Chemkin_Format(input_file)