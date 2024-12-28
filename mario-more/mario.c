#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height=0;
    do
    {
        height=get_int("Height: ");
    }
    while(height<1 || height>8);

    for(int index = 0; index<height;index++){
        for(int i = height; i>index+1;i--){
            printf(" ");
        }
        for(int i = 0; i<index+1;i++){
            printf("#");
        }
        printf("  ");
        for(int i = 0; i<index+1;i++){
            printf("#");
        }
        printf("\n");
    }
}