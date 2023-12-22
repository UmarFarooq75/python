#in this we are going to handle file input or output

s="\nUmar is a good boy"
p="\nHe is a good programer"

#writing in file it erase all old data and enter new data 
# with open("./testingfiles/test.txt","w") as f:
#     f.write(s)
#other method 

fp=open("./testingfiles/test.txt","a") #apending file
fp.write(p)
fp.write(s)
fp.close()