Chemical Equilibrium Calculator
=====================

This program calculates the equilibrium  concentration of chemical species through Gibbs energy minimization, given thermodynamic data in the NASA polynomial format. The process is detailed in  S. Gordon, B. J.McBride; Computer Program for Calculation of Complex Chemical Equilibrium Compositions and Applications. A shorter summary is included in J. C. Kramlich; General Gibbs Minimization as an Approach to Equilibrium. The latter is included in the repo, "gibbs_min.pdf".

The program reads the input filename as a command line argument. The input file needs to contain the temperature and pressure at which the equilibrium concentration is desired, as well as thermodynamic data in the NASA polynomial format. The sample input file is "Input.txt", which contains thermodynamic data from the GRI 3.0 chemical kinetic mechanism.