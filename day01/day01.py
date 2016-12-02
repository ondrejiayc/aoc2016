#!/home/ondrej/anaconda3/bin/python

with open('input.txt','r') as f:
    ride = f.read()

ride = ride.strip().split(', ')

#Problem 1

position = [0,0]

switch = 1 #which index in position to update
direction = 0

for instruction in ride:
    switch = 1-switch
    if instruction[0] == 'R':
        direction += 1
    else:
        direction -= 1

    if direction == 4:
        direction = 0

    if direction == -1:
        direction = 3

    position[switch] += int(instruction[1:])*((direction < 2)*1+(direction>=2)*(-1))

print('Final position: {0}'.format(position))
print('Distance to the HW is {0}.'.format(abs(position[0])+abs(position[1])))

#Problem 2

visited = ['0, 0']
position = [0,0]
found = False

switch = 1 #which index in position to update
direction = 0

for instruction in ride:
    switch = 1-switch
    if instruction[0] == 'R':
        direction += 1
    else:
        direction -= 1

    if direction == 4:
        direction = 0

    if direction == -1:
        direction = 3

    for _ in range(int(instruction[1:])):
        position[switch] += (direction < 2)*1+(direction>=2)*(-1)
        if str(position).strip('[').strip(']') in visited:
            found = True
            break
        else:
            visited.append(str(position).strip(']').strip('['))

    if found: break

print('HQ is at {0}, whose distance is {1}.'.format(position,abs(position[0])+abs(position[1])))
