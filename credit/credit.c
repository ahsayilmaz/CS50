#include <cs50.h>
#include <stdio.h>


int main(void)
{
    int numDigits;
    long num;
    int i=0;
    int creditnum[16];
    long Numorg = get_long_long("Number: ");
    do
    {
        i=0;
        numDigits = 0;
        num = Numorg;
        while (num != 0) {
            creditnum[i] = num % 10;
            num = num / 10;
            numDigits++;
            i += 1;
        }
        if(numDigits<13 || numDigits>16){
            break;
        }
    }while(numDigits<13 || numDigits>16);
    int firstDigit = creditnum[numDigits-1];
    int secDigit = creditnum[numDigits-2];
    int sum=0;
    int a;
    int b;
    for(i = 1; i<numDigits;i+=2){
        creditnum[i] = creditnum[i]*2;
        if(creditnum[i]>9){
            a = creditnum[i] % 10;
            creditnum[i] /= 10;
            b = creditnum[i] % 10;
            sum+=a+b;
        }else{
            sum+=creditnum[i];
        }
    }
    for( i = 0; i<numDigits;i+=2){
        sum+=creditnum[i];
    }
    //bool isValid = sum%10 == 0;
    if (firstDigit == 4 && sum%10 == 0 && (numDigits == 13 || numDigits == 16))
    {
        printf("VISA\n");
    }
    else if (firstDigit == 3 && (secDigit == 7 || secDigit == 4) && sum%10 == 0 && numDigits == 15)
    {
        printf("AMEX\n");
    }
    else if (firstDigit == 5 && (secDigit >= 1 && secDigit <= 5) && sum%10 == 0 && numDigits == 16)
    {
        printf("MASTERCARD\n");
    }
    else{printf("INVALID\n");}
}