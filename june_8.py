import  os
os.chdir("H:\dir")
for i in range (200 ):
    os.mkdir("tryl_directories"+str(i+1))

    f=open("tryl_folders.txt"+str(i+1),"w")