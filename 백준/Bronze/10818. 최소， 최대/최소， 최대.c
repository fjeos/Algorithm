#include <stdio.h>
int main(void) {
    int x, max, min;
    int t;
    scanf("%d", &t);
     max = -1000000;
     min = 1000000;
    for (int i = 0; i < t; i++) {
        scanf("%d", &x);
        if (x >= max) {
            max = x;
        }
        if (x <= min) {
            min = x;
        }
    }
    printf("%d %d", min, max);
    return 0;
}