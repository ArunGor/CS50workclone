sen = input ("input a sentence here: ")
n= len(sen)
for i in range (0,n):
    if sen[i] == " ":
        print ("...", end = "")
    else:
        print (sen[i], end = "")
