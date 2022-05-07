# 
# !Exercises for Nikoli 
from re import T


class Nikola:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def chekeName(self):
        if self.name == 'Nikolai':
            return f'{self.name}, my age is {self.age}'
        else:
            return f'i not {self.name}, i am Nikola. My age is {self.age}'

vahagn = Nikola('Vahagn', 21)

# print(vahagn.chekeName())

# !Exercises for Ann

class RealString:
    def __init__(self, obj1 = str(None), obj2 = str(None)):
        self.obj1 = obj1
        self.obj2 = obj2
           
    # def lenght(self):
    #     len1 = len(self.obj1)
    #     len2 = len(self.obj2)

    def measure(name1, name2):
        if len(name1) > len(name2):
            return f'{name1} is bigger'
        elif len(name1) < len(name2):
            return f'{name2} is bigger'
        else:
            return f'{name1} ang {name2} are equal'

appel = RealString('Apple')
narinj = RealString('Narinj')
# print(RealString.measure(appel.obj1, narinj.obj1))

# !Exercises a CenTury 

class CenTury:
    def __init__(self, year):
        self.year = year
    
    def findOut(self):
        if self.year % 100 != 0:
            return f'{self.year //100 + 1}'
        else:
            return f'{self.year / 100}'

year = CenTury(1977)
# print(year.findOut())

# !Exercises a PALindrOme

class PALindrOme:
    def __init__(self, text):
        self.text = text
    
    def chekPALindrOme(self):
        if self.text == self.text[::-1]:
            return True
        else:
            return False

text = PALindrOme('aahaa')

# print(text.chekPALindrOme())

# ! LARGesT

class LARGesT:
    def __init__(self, myList):
        self.myList = myList
    
    def neighborMax(self):
        array = []
        for item in range(len(self.myList)-1):
            x = self.myList[item]*self.myList[item + 1]
            array.append(x)
        return max(array)
firstList = LARGesT([3, 6, -2, -5, 7, 3])

# print(firstList.neighborMax())

# !Exercises a find HiGHesT wORd

class Highest:
    def __init__(self, myList = list):
        self.myList = myList
    
    def findeHighestWord(self):
        maxIndex = len(self.myList[0]) 
        arr = []

        for i in self.myList:
            if maxIndex < len(i):
                maxIndex = len(i)

        for i in self.myList:
            if len(i) == maxIndex:
                arr.append(i)

        return arr

arr1 = Highest(['aba', 'aa', 'ad', 'vcd', 'aba'])

# print(arr1.findeHighestWord())

# !Exercises a Lucky Ticket

class LuckyTicket:
    def __init__(self, ticket):
        self.ticket = ticket

    def checkTicket(self):
        x = len(str(self.ticket))
        value1text = str(int(self.ticket / pow(10, x/2)))
        value2text = str(int(self.ticket % pow(10, x/2)))
        value1 = 0
        value2 = 0

        for i in value1text:
            value1 += int(i) 
        for i in value2text:
            value2 += int(i)
        
        if value1 == value2:
            return f'{self.ticket} is Lucky ticket'
        else:
            return f'{self.ticket} is not Lucky ticket'

ticket = LuckyTicket(120300)

# print(ticket.checkTicket())

# !Exercises a List Sort 

class ListSort:
    def __init__(self, listIn = [None]):
        self.listIn = listIn
    
    def sortTree(self):
        outOf = []
        for i in self.listIn:
            if i == -1:
                continue
            else:
                outOf.append(i)
        outOf.sort()
        t = 0
        for i in range(len(self.listIn)):
            if self.listIn[i] == -1:
                continue
            else:
                self.listIn[i] = outOf[t]
                t += 1
            if t == len(outOf):
                return self.listIn

list1 = ListSort([-1, 150, 190, 170, -1, -1, 160, 180])

# print(list1.sortTree())

# class WeiGHT: