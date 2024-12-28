// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    int16_t header[HEADER_SIZE];
    int16_t samples[2];
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file
    if(fread(header, sizeof(int16_t), HEADER_SIZE/sizeof(int16_t), input)==HEADER_SIZE/sizeof(int16_t)){
        fwrite(header, sizeof(int16_t), HEADER_SIZE/sizeof(int16_t), output);
    }
    // TODO: Read samples from input file and write updated data to output file
    while(fread(samples, sizeof(int16_t), 1, input)==1){
        samples[0]= samples[0]*factor;
        samples[1]= samples[1]*factor;
        fwrite(samples, sizeof(int16_t), 1, output);
    }
    // Close files
    fclose(input);
    fclose(output);
}
