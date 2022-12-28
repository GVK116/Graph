#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def Graph(cities):
    d = {}
    for i in cities:
        d[i[0]] = []
        d[i[1]] = []
    for i in cities:
        d[i[0]].append(i[1])
        d[i[1]].append(i[0])
    return d

def explore(graph,i,visited):


def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    visited = []
    graph = Graph(cities)
    for i in graph:
        explore(graph,i,visited)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        print(result)

        # fptr.write(str(result) + '\n')

    # fptr.close()
