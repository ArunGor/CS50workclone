statement=input("here:").strip()
x=""
y=""
r = len(statement)
n=0
function=["+","-","/","*"]
for i in range (0,r):
    if statement[i] in function:
        n=i
for j in range(0,n):
    x= x+ statement[j]

for o in range (n+1,r):
    y=y+statement[o]

if statement[n]=="+":
    q=int(x)+int(y)

elif statement[n]== "-":
    q=int(x)-int(y)

elif statement[n]== "*":
    q=int(x)*int(y)

elif statement[n]== "/":
    q=int(x)/int(y)
q=q+0.0
print (q)