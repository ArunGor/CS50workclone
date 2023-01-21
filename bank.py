greet=input("greet the customer: ").strip().capitalize()
f=""
if greet == "Hello":
    print ("$0")
elif greet[0]!= "H":
    print ("$100")
elif greet[0]=="H":
    for i in range (0,5):
        f=f+greet[i]
    if f=="Hello":
        print ("$0")
    else:
        print ("$20")