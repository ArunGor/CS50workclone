count=0
tweet=input("Input: ")
lcvowels=['a','e','i','o','u']
ucvowels=['A','E','I','O','U']
print ("Ouput: ", end="")
for i in range (0, len(tweet)):
    if (tweet[i]) not in lcvowels and (tweet[i]) not in ucvowels:
        print (tweet[i], end="")