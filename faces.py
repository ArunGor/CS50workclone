def convert():
    for i in range (0,len(sen)):
        if sen [i]==":":
            if sen[i+1]== ")":
                print ("🙂", end="")
            if sen[i+1]== "(":
                print ("🙁", end="")
        elif sen[i] == ")":
            print ("", end = "")
        elif sen[i] == "(":
            print ("", end = "")
        else:
            print (sen[i], end="")
sen = input ("face: ")
convert()