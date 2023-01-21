def main():
    m=convert(b)
    if m>=7.0 and m<=8.0:
        print ("breakfast time")
    elif m>=12.0 and m<=13.0:
        print ("lunch time")
    elif m>=18.0 and m<=19.0:
        print ("dinner time")
    else:
        print ("")

def convert(time):
    hour=""
    mins=""
    for i in range (0,len(time)):
        if time[i] == ":":
            e=i
    for k in range (0,e):
        hour=hour+time[k]
    for j in range (e+1, len(time)):
        mins=mins+time[j]
    min=int(mins)/60
    hours=int(hour)
    timing= hours+min
    return(timing)

b=input("here:")

main()