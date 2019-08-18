print ("Staircase")

stair = ""
space = ""
steps = 4

def space_count(count):
    step_gap = ""
    for x in range(int(count)):
        step_gap  += " "
    return step_gap

for x in range(steps):
    step_space = (space_count(str((steps - 1) - x)))
    stair += "#"
    step_space += stair
    print (step_space)