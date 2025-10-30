#include <stdio.h>
int main(void) {
    int x,y,i,t;
    char s;
    scanf("%d",&t);
    for(i=0; i<t; i++) {
        scanf("%d%c%d",&x,&s,&y);
        printf("%d\n",x+y);
    }
}