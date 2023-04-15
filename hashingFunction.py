# make a function that accepts a string inut, and then hashes it returning a unique input

class HashMap:
    
    def __init__(self):
        self.hash = []
        
        #Please teach me list comp cuz I tried and didnt know how
        for x in range(10000):
            self.hash.append(0)

        

    def mapAdd(self, key, value):
        numVal = 0
 
        for car in key:
            numVal += ord(car) + len(key)

            while self.hash[numVal]:
                numVal += 1        
        
            self.hash[numVal] = value

        return self.hash
    

    def mapFind(self, key):
        numVal = 0

        #car is short for character lmao
        for car in key:
            # ord returns the ASCII value of the char
            numVal += ord(car) + len(key)

        return self.hash[numVal] if self.hash[numVal] else "None"


    def mapDraw(self):
        print(self.hash)



hashmap1 = HashMap()
hashmap1.mapAdd("A", "Yoyoyoyoyoyoyoyoyo")
hashmap1.mapDraw()





# yoyoyoyo don't be mad at me for this code below, I just wanted to preserve it
# This was the original before making it into a class


def hashing(sLlist):
    hashList = []
    numVal = 0
    numValList = []
    check = False
    slist = []

    for x1 in sLlist:
        slist.append(x1[0])


    for x in range(10000):
        hashList.append(0)


    for i, car in enumerate(slist):
        for nerd in car:
            print(i)
            numVal += ord(nerd) + len(car)
       

        #havent implemented checking this yet
        while hashList[numVal]:
            numValList.append(numVal)
            hashList[numVal] = slist[i]
            numVal = 0
        #

        if not check:
            numValList.append(numVal)
            hashList[numVal] = slist[i]
            numVal = 0

#Need to check if the current hashList index is 0

    return hashList



