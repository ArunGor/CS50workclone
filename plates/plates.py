def main():
    plate = input("Plate: ")
    if is_valid(plate)== True:
        print("Valid")
    else:
        print("Invalid")
flag=True
setup=True
punctuation=[',',"'","/",".",":",";"," "]
def is_valid(s):
    global setup
    global flag
    global intflag
    intflag=0
    if len(s)<=6 and len(s)>=2:
        flag=True
    else:
        return (False)
    for i in range (0,2):
        if s[i]>="A" and s[i]<="Z":
            flag=True
        else:
            return (False)
    for c in s:
        if c>="A" and c<="Z":
            flag=True
            if intflag==True:
                return False
        elif c in punctuation:
            return (False)
        elif int(c)>0 and int(c)<=9:
            flag=True
            intflag=intflag+1
        elif intflag>=1 and int(c)>=0 and int(c)<=9:
            flag=True
        else:
            return (False)
    if flag==True:
        return (True)



main()