#!/home/ondrej/anaconda3/bin/python

import numpy as np

instructions = []

with open('input.txt','r') as f:
    for line in f:
        instructions.append(line.strip())

#Problem 1

numPad = np.arange(1,10).reshape(3,3)

moves = {'U': np.array([-1,0]),
         'D': np.array([1,0]),
         'L': np.array([0,-1]),
         'R': np.array([0,1])}

position = np.array([1,1])
code = []

for inst in instructions:
    for move in inst:
        position += moves[move]
        if not (0 <= position[0] <= 2) or not (0 <= position[1] <= 2):
            position -= moves[move]

    code.append(str(numPad[position[0],position[1]]))

print('The code in problem 1 is {0}.'.format(''.join(code)))

#Problem 2

numPad = [['0', '0', '1', '0', '0'],
          ['0', '2', '3', '4', '0'],
          ['5', '6', '7', '8', '9'],
          ['0', 'A', 'B', 'C', '0'],
          ['0', '0', 'D', '0', '0']]

position = np.array([2,0])
code = []

for inst in instructions:
    for move in inst:
        position += moves[move]
        if not (0 <= position[0] <= 4) or not (0 <= position[1] <= 4):
            position -= moves[move]
            continue
        if numPad[position[0]][position[1]] == '0':
            position -= moves[move]
            continue

    code.append(numPad[position[0]][position[1]])

print('The code in problem 2 is {0}.'.format(''.join(code)))
