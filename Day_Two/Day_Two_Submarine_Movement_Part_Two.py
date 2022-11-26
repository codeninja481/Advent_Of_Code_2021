#Submarine Movement Advent Day 2
#directions = open("Day_Two_Submarine_Movement_Data_1.txt").read().split('\n')
directions = open("Day_Two_Submarine_Movement_Data.txt").read().split('\n')


print("Part Two")
def directionsP2():
    hpos = 0
    dpos = 0
    apos = 0
    #print("hpos: " + str(hpos) + " - dpos: " + str(dpos) + " - apos: " + str(apos))
    for d in directions:
        direction = d.split(' ')
        #print(direction[0] + " - " + direction[1])
        if direction[0] == "forward":
            #print("forward")
            hpos += int(direction[1])
            if apos != 0:
                dpos += (int(direction[1]) * apos)
        elif direction[0] == "up":
            #print("up")
            apos -= int(direction[1])
        elif direction[0] == "down":
            #print("down")
            apos += int(direction[1])
        else:
            print("Error")
        #print("hpos: " + str(hpos) + " - dpos: " + str(dpos) + " - apos: " + str(apos))
        
    print("hpos: " + str(hpos) + " - dpos: " + str(dpos) + " - apos: " + str(apos) + " - total: " + str((hpos * dpos)))

directionsP2()
#1813664422