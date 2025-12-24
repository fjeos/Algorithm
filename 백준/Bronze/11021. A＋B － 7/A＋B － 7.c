#include <stdio.h>
int main(void) {
    int t,x,y,i;
    scanf("%d",&t);
    for(i=1; i<=t; i++) {
        scanf("%d %d",&x, &y);
        printf("Case #%d: %d\n",i,x+y);
    }
}