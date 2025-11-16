#include <stdio.h>
#include <string.h>
int main(void) {
    char a[101];
    int i,j;

    gets(a);
    for (i = 0; i<strlen(a); i++) {
        printf("%c", a[i]);
        if ((i + 1) % 10 == 0) {
            printf("\n");
        }
    }
    printf("\n");
    return 0;
}