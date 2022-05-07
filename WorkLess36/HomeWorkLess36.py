import math
import random
from signal import valid_signals
# 
# !COVID - 19  

class Covid19:
    def __init__(self, name, surname, temp = float):
        self.name = name 
        self.surname = surname
        self.temp = temp
    
    def analiz(self):
        res = self.temp * math.pi
        if res % 1 < 0.5:
            res = res - (res%1)
        else:
            res = res - (res%1) + 1

        if res > 120 and res < 128:
            return f'{self.name} {self.surname}, You have coronavirus'
        else:
            return f'{self.name} {self.surname}, Everything is ok'


# # person = Covid19(name = input('Enter name ---> '),
#                    surname = input('Enter surname ---> '),
#                    temp = float(input('Enter temperature ---> ')))

# print(person.analiz())

# !Find your name number

class FindNameNumber:
    def __init__(self, name):
        self.name = name
    
    
    def widespread(self):
        numDickt = {'a' : 1, 'j' : 1, 's' : 1,
             'b' : 2, 'k' : 2, 't' : 2,
             'c' : 3, 'l' : 3, 'u' : 3,
             'd' : 4, 'm' : 4, 'v' : 4,
             'e' : 5, 'n' : 5, 'w' : 5,
             'f' : 6, 'o' : 6, 'x' : 6, 
             'g' : 7, 'p' : 7, 'y' : 7,
             'h' : 8, 'q' : 8, 'z' : 8,
             'i' : 9, 'r' : 9}
        self.name = self.name.lower()
        arrName = []
        res = 0
        
        for i in self.name:
            arrName.append(i) 

        for i in arrName:
            for j in numDickt.keys():
                if i == j:
                    res = res + numDickt.get(j)

        if math.sqrt(res)< 5:
            return f'{res}, Yes'
        else:
            return f'{res}, No'
# firstName = FindNameNumber(name = str(input('Enter name -->')))

# print(firstName.widespread())

# !Harry Potter

class HarryPotter:
    def __init__(self, word1, word2, word3):
        self.word1 = word1
        self.word2 = word2
        self.word3 = word3
    
    def magicGame(self):
        magicLisit = ['Avada Kedavra', 'Crucio', 'Imperio']
        voldemortList = []
        res = 0
        for i in range(3):
            n = random.randint(0,2)
            voldemortList.append(magicLisit[n])
        
        print(voldemortList)

        if self.word1 == voldemortList[0]:
            res += 1
        if self.word2 == voldemortList[1]:
            res += 1
        if self .word3 == voldemortList[2]:
            res += 1
        if res >= 2:
            return f' You win'
        else:
            return f' you lose'

player1 = HarryPotter(word1=input(), word2=input(), word3=input())

print(player1.magicGame())