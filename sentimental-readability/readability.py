# TODO
import math
str = str(input("Text: "))
i =0
wordCount =1.00
letterCount = 0
sentenceCount=0.00
while (i<len(str)):
    if(str[i].isalpha()):
        letterCount+=1
    elif(str[i]==' '):
        wordCount+=1
    elif(str[i]=='.' or str[i]=='!' or str[i]=='?'):
        sentenceCount+=1
    i+=1
L = (letterCount*100/wordCount)*100
S = (sentenceCount*100/wordCount)*100
L=math.floor(L)
S =math.floor(S)
indexs = 0.0588*L/100 - 0.296*S/100 - 15.8
index = round(indexs)
if(index<1):
    print("Before Grade 1")
elif(index>=16):
    print("Grade 16+")
else:
    print(f"Grade {index}")
