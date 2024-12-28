#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>
#include <unistd.h>
#include <sys/stat.h>

int main(int argc, char *argv[]) {
    char imgName[8];
    uint8_t list[512];
    int a = 0;

    FILE *f = fopen(argv[1], "r");
    if (f == NULL) {
        fprintf(stderr, "Failed to open input file\n");
        return 1;
    }

    FILE *img = NULL;
    while (fread(list, 1, 512, f) == 512) {
        if (list[0] == 0xff && list[1] == 0xd8 && list[2] == 0xff && (list[3] & 0xf0) == 0xe0) {
            if (img != NULL) {
                fclose(img);
            }

            sprintf(imgName, "%03i.jpg", a);

            if (access(imgName, F_OK) != -1) {
                printf("%03i.jpg already exists...\n", a);
            } else {
                img = fopen(imgName, "w");
                if (img == NULL) {
                    fprintf(stderr, "Failed to create output file\n");
                    fclose(f);
                    return 1;
                }

            }
            a++;
        }
        if (img != NULL) {
            fwrite(list, 1, 512, img);
        }
    }
    if (img != NULL) {
        fclose(img);
    }
    fclose(f);
    return 0;
}
