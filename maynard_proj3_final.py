################################################################################
#
# Jason Maynard, U30503758
# Project 3, Algorithms Fall '13
# 
# Using NetworkX directed graphs to model mazes
# www.networkx.com
#
################################################################################

import networkx as nx                   # Network modeling and analysis
import matplotlib.pyplot as plt         # Graph plotting
import numpy as np                      # Numerical Python for matrix

# Create a new networkX graph object
# DiGraph() indicates that it is a directed graph
G = nx.DiGraph()

# Open files -------------------------------------------------------------------
print 'Opening files'

# Error checking on opening file
# Exit gracefully
try:
    fileIn = open('input.txt', 'r')
    fileOut = open('maynard.txt', 'w')
except IOError:
    print 'Could not open file'
    sys.exit()


# GET DATA ---------------------------------------------------------------------
# From the given input file the following mazes are provided for analysis

data = [] # The array to put the data

for lines in fileIn:
    lines = lines.strip().split()
    data.append(lines)

num_mazes = int(data[0][0])
print 'Number of mazes is: ', num_mazes

dataset_index = 2 # starts at first maze (i.e., 3rd line of file)

# OUTER LOOP - Walk through 'm' mazes in file ----------------------------------
for m in range(num_mazes):
    print '\n\n************************************************************'
    print 'Maze number: ', m+1


    # MIDDLE LOOP - Process each maze ------------------------------------------

    # BUILD GRAPH --------------------------------------------------------------
    # Assume directed edges as Jim can only move from one square to the next
    # based on the number.  Once on a new square, he can not move backwards but
    # only forward based on the new number. 

    # Get the dimension from the file for the specific maze
    dimension = int(data[dataset_index][0])

    # Array to hold values read from file
    maze = np.zeros([dimension,dimension], dtype=int)

    # Populate array with values from data
    for row in range(dimension):
        for col in range(dimension):
            maze[row][col] = data[row + dataset_index + 1][col]

    # Array to hold index numbers
    index_array = np.zeros([dimension, dimension], dtype = int)

    # Populate array with indexes
    index = 1
    for row in range(dimension):
        for col in range(dimension):
            index_array[row][col] = index
            index += 1

    # Add edges to build NetworkX graph ----------------------------------------
    for row in range(dimension):
        for col in range(dimension):
            # Get value from maze
            value = maze[row,col]
            # Calculate potential destination cells and see if they are on maze
            # Ignore edges that would lead to Jim falling off maze

            # Look North
            if (row-value >= 0):
                G.add_edge(index_array[row,col], index_array[row-value,col])

            # Look South
            if (row+value < dimension):
                G.add_edge(index_array[row,col], index_array[row+value,col])        

            # Look East
            if (col+value < dimension):
                G.add_edge(index_array[row,col], index_array[row,col+value])  

            # Look West
            if (col-value >= 0):
                G.add_edge(index_array[row,col], index_array[row,col-value])

    print maze

    # Maze data read for analysis.  Update index to move to the next maze
    dataset_index = dataset_index + dimension + 2

    #### Draw graph ####
    ## nx.draw(G)
    ## plt.show()

    # ANALYZE GRAPH ------------------------------------------------------------
    start = 1
    end = dimension * dimension

    print '\nAnalyzing graph wiht NetworkX'

    if nx.has_path(G,start,end):
        path = nx.shortest_path(G,start,end)
        length = nx.shortest_path_length(G, start, end)


        # RESULTS ------------------------------------------------------------------
        # print "\nThe shortest path by number is: ", path      
        # print "The length of shortest path is: ", length
        
        # To find all shortest paths
        # print([p for p in nx.all_shortest_paths(G,start,end)])

        print 'Follow these directions to get out of the maze... \n'

        # Now translate numbers into directions N,S,E,W
        for i in range(1,len(path)):
            if path[i] > path[i-1]:        
                if (path[i] - path[i-1]) % dimension == 0:
                    print 'S',
                    fileOut.write('S ')
                else:
                    print 'E',
                    fileOut.write('E ')
            else:        
                if (path[i] - path[i-1]) % dimension == 0:
                    print 'N',
                    fileOut.write('N ')
                else:
                    print 'W',
                    fileOut.write('W ')
        fileOut.write('\n\n')

    else:
        print 'No path!!'

    # Clear the graph for next maze
    G.clear()

# End outer loop ---------------------------------------------------------------

# Close files ------------------------------------------------------------------
print '\n\nClosing files'
fileIn.close()
fileOut.close()
