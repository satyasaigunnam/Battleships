def sat(getFirstName):
    l=len(getFirstName)
    temp=getFirstName[7: ]+" "+getFirstName[0:7]
    return temp
print(sat("Donald knuth"))