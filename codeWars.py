def escape(carpark): 
    directions = [] # Holds the directions
    x, y = getPosition(carpark) # Starting position of the 2 in carpark as a list[x, y]
    carpark_length = len(carpark)
    while x < carpark_length:
        direct = LeftorRight(x, y, carpark[x], carpark_length - 1) # Gets the direction to the nearest exit in list form[Dir, Moves, ExitIndex]
        if direct[0]: # If a direction is needed
            directions.append(direct[0] + str(direct[1]))
            y = direct[2]
            # break # If not the solution was found
        if x == carpark_length - 1 and y == len(carpark[x]) - 1: # If position is at the end break
            break
        direct = GetDown(x, y, carpark) # Gets how many downs
        directions.append(direct[0]+ str(direct[1]))
        x = x + direct[1]
    return directions

def getPosition(carpark): # Finds the position of the 2 in carpark (Will find it on every level not just the 1st)
    for x in range(len(carpark)): # Iterate through carpark, return the position when 2 is found
        for i in range(len(carpark[x])):
            if carpark[x][i] == 2:
                return x, i

def LeftorRight(x, person, floor, maxLevel): # Finds the desired position on the floor, and if it is R or L
    if x != maxLevel: # Check if current position is not on the bottom floor
        exit = 0
        for exit in range(len(floor)): # Finds the index of the exit
            if floor[exit] == 1:
                break
        return ["R", (exit - person), exit] if person - exit < 0 else ["L", (person - exit), exit]
    if person == len(floor) - 1: # If current position IS on the bottom floor check if it is already all the way on the right
        return [None]
    return ["R", (len(floor) - person - 1), len(floor) - 1] # Otherwise give the final Right direction

def GetDown(x, y, carpark): # Checks if multiple downs can be done 
    downs = 1 # This function running implies a 1 was found. There is at least 1 down
    more_downs = True
    while more_downs:
        if(carpark[x + 1][y] == 1): # Check next floor for 1s on the same position
            x += 1
            downs += 1
        else: # If none found return the downs
            more_downs = False
    return ["D", downs]