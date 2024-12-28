numDigits=0
num=0
i=0
creditnum=[]
Numorg = int(input("Number: "))
while(numDigits<13 or numDigits>16):
    i=0
    numDigits = 0
    num = Numorg
    while (num != 0):
        creditnum.append(num % 10)
        num = num // 10
        numDigits += 1
        i += 1
    if(numDigits<13 or numDigits>16):
        break
firstDigit = creditnum[numDigits-1]
secDigit = creditnum[numDigits-2]
sum=0
a=0
b=0
for i in range(1,numDigits,2):
    creditnum[i] = creditnum[i]*2
    if(creditnum[i]>9):
        a = creditnum[i] % 10
        creditnum[i] //= 10
        b = creditnum[i] % 10
        sum+=a+b
    else:
        sum+=creditnum[i]
for i in range(0,numDigits,2):
    sum+=creditnum[i]
if (firstDigit == 4 and sum%10 == 0 and (numDigits == 13 or numDigits == 16)):
    print("VISA")
elif (firstDigit == 3 and (secDigit == 7 or secDigit == 4) and sum%10 == 0 and numDigits == 15):
    print("AMEX")
elif (firstDigit == 5 and (secDigit >= 1 and secDigit <= 5) and sum%10 == 0 and numDigits == 16):
    print("MASTERCARD")
else:
    print("INVALID")
