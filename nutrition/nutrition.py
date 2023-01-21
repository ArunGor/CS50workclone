Fruits=['Apple','Avocado','Banana','Cantaloupe','Grapefruit','Grapes','Honeydew Melon','Kiwifruit','Lemon','Lime','Nectarine','Orange','Peach','Pear','Pineapple','Plums','Strawberries','Sweet Cherries','Tangerine','Watermelon']
Cals=[130,50,110,50,60,90,50,90,15,20,60,80,60,100,50,70,50,100,50,80]
F=input("Input Fruit here:").title()
if F in Fruits:
    for i in range (0,21):
        if Fruits[i]==F:
            break
    print (Cals[i])
else:
    print ("")