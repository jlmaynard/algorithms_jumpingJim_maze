# algorithms_jumpingJim_maze
Python implementation of jumping Jim maze problem using NetworkX. Check out the PDF for the report and overview. 

This program was developed on Python 2.7.6.

It is assumed that a graphing program called NetworkX has been installed which allows for the import of a networkx object.  

www.networkx.com

The imports used for this project are:
import networkx as nx                   # Network modeling and analysis
import matplotlib.pyplot as plt         # Graph plotting
import numpy as np                      # Numerical Python for matrix

To run this program:
Add the “python maynard_proj3_final.py” to a working unix directory along with an input file names “input.txt”

At a unix command simply type “python maynard_proj3_final.py” 

The program currently displays status of the individual graphs and analysis to the python shell while running.  This can be turned off by commenting out any print statements if needed. 

An output file named “maynard.txt” is produced in the working directory with the required resutls.  

Many test cases were run but the scope of the user’s input file is unknown so a test of all inputs was not possible. 

The program is designed to ignore graphs that do not have a shortest path.


