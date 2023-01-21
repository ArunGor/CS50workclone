alphabetu= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabetl= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

sen = input ("write a sentence with all capitalized letters")
n=111
sen = sen.capitalize()
for i in range (0,25):
    if sen[0] == alphabetu[i]:
        n=i

count = len(sen)

for j in range (1,count):
    if n==111:
        print (sen[0],end='')
    elif j==1 :
        print (alphabetl[n], end='')
    print (sen[j], end= '')
    count=count-1