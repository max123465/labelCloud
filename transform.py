import numpy
import glob, os

files = glob.glob("c:/Users/hands/OneDrive/桌面/Label/labelCloud/labels/Lian/*.txt")
savePath = "c:/Users/hands/OneDrive/桌面/Label/labelCloud/gt/"
#print(files)
i = 0
for path in (files):
    f = open(path, 'r')
    Lines = f.readlines()
    outlist = []
    
    
    for line in Lines:   
        tmp = []     
        splitlist = line.split(' ')
        tmp.append(splitlist[11])
        tmp.append(splitlist[12])
        tmp.append(splitlist[13])
        tmp.append(splitlist[8])
        tmp.append(splitlist[9])
        tmp.append(splitlist[10])
        tmp.append(splitlist[14][:-1])
        tmp.append(splitlist[0])
        outlist.append(tmp)
    p = savePath + str(i).zfill(6) + ".txt"
    with open(p, "w", encoding="utf-8") as wf:
        wf.write('\n'.join([' '.join(t) for t in outlist]))
    wf.close()
    f.close()   
    i+=1 
    
    