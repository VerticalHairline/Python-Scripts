import random

def arrayIt(length):
    newArray = [random.randint(1, 10) for i in range(length)]
    return newArray

newList = arrayIt(5)

class array:

    instances = []
    
    def __init__(self, length):
        arrayee = arrayIt(length)
        self.ar = arrayee
        array.instances.append(self)

    def reRoll(self):
        array = arrayIt(len(self.ar))
        self.ar = array

    def match(self, otherArray):
        altArray = otherArray.copy()
        array = self.ar.copy()
        diff = abs(len(array)-len(altArray))
        if diff != 0:
            if len(array) > len(altArray):
                while diff > 0:
                    array.pop()
                    diff = diff - 1
            else:
                while diff > 0:
                    altArray.pop()
                    diff = diff - 1

        matchedArray = [(array[z], altArray[z]) for z in range(len(array))]
        self.matchedAr = matchedArray
        return matchedArray

    def add(self, *otherArrays):

        other = list(otherArrays)
        otherArray = [x.copy() for x in other]
        overArray = [x.copy() for x in otherArray]
        overArray.append(self.ar)
        
        lengthArray = [len(x) for x in overArray]
        length = max(lengthArray)

        baseArray = self.ar.copy()
        if len(self.ar) < length:
            for x in range(length - len(self.ar)):
                baseArray.append(0)

        for x in otherArray:
            if len(x) < length:
                for e in range(length - len(x)):
                    x.append(0)

        otherArray.append(baseArray)
        sumArray = []
        for x in range(length):
            sum = 0
            for y in otherArray:
                sum = sum + y[x]
            sumArray.append(sum)
        self.sumAr = sumArray
        return sumArray
        

array1 = array(5)
array2 = array(10)
array3 = array(15)
array4 = array(3)

array1.add(array2.ar, array3.ar, array4.ar)
