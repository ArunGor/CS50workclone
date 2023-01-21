snakename=""
camelname=input("input your camelcase name: ")
for c in camelname:
    if c<"a":
        snakename=snakename+"_"
        snakename=snakename+c.swapcase()
    else:
        snakename=snakename+c
print (snakename)