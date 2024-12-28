#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
int main(void)
{
    string str = get_string("Text: ");
    int i =0;
    float wordCount =1.00;
    int letterCount = 0;
    float sentenceCount=0.00;
    while (i<strlen(str)) {
        if((str[i]>64&&str[i]<91)||(str[i]>96&&str[i]<123)){
            letterCount++;
        }
        else if(str[i]==' '){
            wordCount++;
        }
        else if(str[i]=='.'||str[i]=='!'||str[i]=='?'){
            sentenceCount++;
        }
        i++;
    }
    float L = (letterCount*100/wordCount)*100;
    float S = (sentenceCount*100/wordCount)*100;

    L=floor(L);
    S =floor(S);

    float indexs = 0.0588*L/100 - 0.296*S/100 - 15.8;
    int index = round(indexs);
    if(index<1){
        printf("Before Grade 1\n");
    }
    else if(index>=16){
        printf("Grade 16+\n");
    }
    else{printf("Grade %i\n", index);}
}