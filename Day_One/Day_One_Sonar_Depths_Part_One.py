#Advent Day 1 Part 1
#depths = open("sonar_depths_input_data_1.txt").read().split('\n')
depths = open("Day_One_Sonar_Depths_Part_One_Inputs.txt").read().split('\n')

"""  PART ONE  """
lastdepth = depths[0]
count = 0
count2 = 0
tcount = 0
for d in depths:
    if (int(d) > int(lastdepth)):
        print(d + " Increase.")
        lastdepth = d
        count += 1
        tcount += 1
    else:
        print(lastdepth + " - " + d + " - Decrease")
        lastdepth = d
        count2 += 1
        tcount += 1
        
print("Total Inputs: " + str(tcount))
print("Increases: " + str(count))
print("Decreases: " + str(count2))
#not 1476 too low

"""
199
200
208
210
200
207
240
269
260
263
"""