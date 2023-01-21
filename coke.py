due=50
mgiven=0
while due>0:
    print ("Amount Due: ",due)
    change = int(input("Insert Coin:"))
    if change==10:
        due=due-change
        mgiven=mgiven+change
    elif change==25:
        due=due-change
        mgiven=mgiven+change
    elif change==5:
        due=due-change
        mgiven=mgiven+change
    else:
        print ("Amount Due: ",due)
        change = int(input("Insert Coin:"))
if due<0:
    mreturn=mgiven-50
    print ("Change Owed: ",mreturn)
elif due==0:
    print ("Change Owed: ",due)