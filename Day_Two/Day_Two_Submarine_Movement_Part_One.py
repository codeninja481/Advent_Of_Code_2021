#Submarine Movement Advent Day 2
#directions = open("Day_Two_Submarine_Movement_Data_1.txt").read().split('\n')
directions = open("Day_Two_Submarine_Movement_Data.txt").read().split('\n')

"""  PART ONE  """
print("Part One")
def directionsP1():
    hpos = 0
    dpos = 0
    for d in directions:
        direction = d.split(' ')
        #print(direction[0] + " - " + direction[1])
        if direction[0] == "forward":
            #print("forward")
            hpos += int(direction[1])
        elif direction[0] == "up":
            #print("up")
            dpos -= int(direction[1])
        elif direction[0] == "down":
            #print("down")
            dpos += int(direction[1])
        else:
            print("Error")
    
    print("hpos: " + str(hpos) + " - dpos: " + str(dpos) + " - total: " + str((hpos * dpos)))
    
directionsP1()    