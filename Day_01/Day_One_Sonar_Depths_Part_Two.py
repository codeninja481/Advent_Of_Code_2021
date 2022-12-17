#Advent Day 1 Part 2
#depths = open("sonar_depths_input_data_1.txt").read().split('\n')
depths = open("Day_One_Sonar_Depths_Inputs.txt").read().split('\n')

print()
print("Part Two")
"""  PART TWO  """
lastWindow = int(depths[0]) + int(depths[1]) + int(depths[2])
#print(lastWindow)
count = 0
for idx, val in enumerate(depths):
    if idx+2 < len(depths):
        #print("LastWindow: " + str(lastWindow) + " - " + str(val) + " - " + str(depths[idx+1]) + " - " + str(depths[idx+2]) + " = " + str(int(val) + int(depths[idx+1]) + int(depths[idx+2])))
        if int(int(val) + int(depths[idx+1]) + int(depths[idx+2])) > int(lastWindow):
            count += 1
            #print("Increase.")
            lastWindow = int(val) + int(depths[idx+1]) + int(depths[idx+2])
        else:
            #print("Decrease.")
            lastWindow = int(val) + int(depths[idx+1]) + int(depths[idx+2])
        

print("Increases: " + str(count))