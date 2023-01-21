q=input("whats the anser to life?: ")
ans=q.strip().capitalize()
if ans == "42":
    print ("Yes")
elif ans == "Forty two":
    print ("Yes")
elif ans == "Forty-two":
    print ("Yes")
else:
    print ("No")