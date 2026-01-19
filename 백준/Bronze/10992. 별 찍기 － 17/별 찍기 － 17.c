#include <stdio.h>
int main(void) {
    int i,j,x;
    scanf("%d", &x);

    for (j = 0; j < x - 1; j++) {
        printf(" ");
    }
    printf("*\n");
    if (x != 1) {
        for (i = 1; i < x - 1; i++) {
            for (j = 0; j < x - i - 1; j++) {
                printf(" ");
            }
            printf("*");
            for (j = 0; j < 2 * i - 1; j++) {
                printf(" ");
            }
            printf("*\n");
        }
        for (j = 0; j < 2 * x - 1; j++) {
            printf("*");
        }
        if (j != 2 * x - 1) {
            printf("\n");
        }
    }
    return 0;
}