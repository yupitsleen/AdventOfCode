def inventory():
    lines=open('input2.txt').readlines()
    lines2=[]
    for line in lines:
        lines2.append(line.strip('\n'))
    twoCount=0
    threeCount=0
    letterDict={}

    for line in lines2:
        while letter in line not in letterDict:
            if letter not in letterDict:
                letterDict[letter]=1
            else:
                letterDict[letter]+=1
                
    for letter in letterDict:
        if letter == 3:
            twoCount+=1
            threeCount+=1
        elif letter ==3:
            threeCount+=1           
    
                
    print( twoCount*threeCount)
    
inventory()      
