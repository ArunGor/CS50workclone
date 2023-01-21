fuelfraction=(input("input the level of fuel"))
fuelnum=(fuelfraction.split("/"))
if float(fuelnum[0])>=0 and float(fuelnum[1])>0:
    fuelpercent=((int(fuelnum[0]))/(int(fuelnum[1])))*100
    if fuelpercent>100:
        print("invalid input")
    elif fuelpercent>=99:
        print ("F")
    elif fuelpercent<=1:
        print("E")
    elif ValueError==True:
        print ("")
    else:
        fuelpercent=str(fuelpercent)
        for i in range (0,2):
            print ((fuelpercent[i]),end="")
        print("%")
else:
    print ("")