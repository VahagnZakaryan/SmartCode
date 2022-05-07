import json
from operator import xor
from posixpath import split
from urllib import request, response


# names = ['Ervand', 'Meliq', 'Vahagn']
# age = [19, 20, 21]
# myDick = dict(zip(names, age))
# # print(myDick)

# jsonString = [
#     ' Lets dont talk about my soul'
#     ' I just really want to walk away'
#     ' My happiness is stolen'
#     ' Can anybody show me way'
# ]
# with open('FirstJson.json', 'w') as outfile:
#     json.dump(jsonString, outfile)

# with open('FirstJson.json', 'r') as jsoneName:
#     x = json.load(jsoneName)

# print(x)

# num = int(input('Enter namber ---> '))
# sum = 0
# for i in range(num):
#     if i % 3 == 0 or i % 5 == 0:
#         print(i)
#         sum +=i
# with open('FirstJson.json', 'w') as outfile:
#     json.dump(sum, outfile)

# with open('FirstJson.json', 'r') as jsoneName:
#     x = json.load(jsoneName)

# print(x)

# string1 = input('Enter String---> ')
# vowels = ['e', 'u', 'i', 'o', 'a']

# res = str()

# for i in string1:
#     if i in vowels:
#         res += i

# with open('FirstJson.json', 'w') as outfile:
#     json.dump(res, outfile)

# with open('FirstJson.json', 'r') as jsoneName:
#     x = json.load(jsoneName)

# # print(len(x))

# with open('Text.txt') as word:
#     lines = str(word.readlines())

# wordLine = lines.split(' ')
# print(wordLine)
# wordDict = {'and': 0,'another' : 0}


# for i in wordLine:
#     if i == 'and' or i == 'And':
#         wordDict['and'] += 1
#     if i == 'Another' or  i == 'another':
#         wordDict['another'] += 1
    
# print(wordDict)4

# xndir 6
# my_list = ['a', 'b', 'a', 'a', 'c', 'b']

# newList = set(my_list)

# print(newList)

# xndir 7

def qualityUD ():
    fileName = input('Enter file name---> ')
    uper = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
        'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
        'Z', 'X', 'C', 'V', 'B', 'N', 'M'
    ]
    qualityUP = 0

    down = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
        'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
        'z', 'x', 'c', 'v', 'b', 'n', 'm'
    ]
    qualityDown = 0

    with open(fileName) as word:
        lines = str(word.readlines())

    letter = list(lines)

    for i in letter:
        if i in uper:
            qualityUP+=1
        if i in down:
            qualityDown+=1  

    print('Uppercase letters ----> ', qualityUP)
    print('lowercase letters ----> ', qualityDown)

qualityUD()