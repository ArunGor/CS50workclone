prefix=""
g=0
mime=input("here: ").strip().capitalize()
files=[".gif",".pdf",".jpeg",".jpg",".png",".txt",".zip"]
outs=["image/gif","application/pdf","image/jpeg","image/jpeg","image/png","text/plain","application/zip"]
r=len(mime)
for i in range (0,r):
    if mime[i]==".":
        g=i
if g==0:
    prefix=""
else:
    for m in range (g,r):
        prefix=prefix+mime[m]
if prefix not in files or prefix == "":
    print ("application/octet-stream")
else:
    for f in range(0,7):
        if prefix==files[f]:
            print (outs[f])