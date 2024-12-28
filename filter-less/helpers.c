#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int color=round((image[i][j].rgbtRed+image[i][j].rgbtGreen+image[i][j].rgbtBlue)/3.000);
            image[i][j].rgbtRed=color;
            image[i][j].rgbtGreen=color;
            image[i][j].rgbtBlue=color;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int colorR=round(0.393*image[i][j].rgbtRed+0.769*image[i][j].rgbtGreen+0.189*image[i][j].rgbtBlue);
            if(colorR>255){
                colorR=255;
            }
            int colorG=round(0.349*image[i][j].rgbtRed+0.686*image[i][j].rgbtGreen+0.168*image[i][j].rgbtBlue);
            if(colorG>255){
                colorG=255;
            }
            int colorB=round(0.272*image[i][j].rgbtRed+0.534*image[i][j].rgbtGreen+0.131*image[i][j].rgbtBlue);
            if(colorB>255){
                colorB=255;
            }
            image[i][j].rgbtRed=colorR;
            image[i][j].rgbtGreen=colorG;
            image[i][j].rgbtBlue=colorB;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < round(width/2); j++)
        {
            RGBTRIPLE temp=image[i][j];
            image[i][j]=image[i][width-1-j];
            image[i][width-1-j]=temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE newImage[height][width];
    int colorR=0, colorG=0, colorB=0;
    float totalPixels=0.000;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            colorR=0, colorG=0, colorB=0, totalPixels=0;
            for(int k=i-1;k<i+2;k++){
                if(k==-1||k==height){
                        continue;
                }
                for(int a=j-1;a<j+2;a++){
                    if(a==-1||a==width){
                        continue;
                    }
                    colorR+=image[k][a].rgbtRed;
                    colorG+=image[k][a].rgbtGreen;
                    colorB+=image[k][a].rgbtBlue;
                    totalPixels+=1.000;
                }
            }
            newImage[i][j].rgbtRed=round(colorR/totalPixels);
            newImage[i][j].rgbtGreen=round(colorG/totalPixels);
            newImage[i][j].rgbtBlue=round(colorB/totalPixels);
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed=newImage[i][j].rgbtRed;
            image[i][j].rgbtGreen=newImage[i][j].rgbtGreen;
            image[i][j].rgbtBlue=newImage[i][j].rgbtBlue;
        }
    }
    return;
}
