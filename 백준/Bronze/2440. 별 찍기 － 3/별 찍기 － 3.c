#include <stdio.h>

int main(void)
{
    int i,j,n;
    
    scanf("%d",&i);
    
    for(j=i; j>=1; j--)
    {
        for(n=j; n>=1; n--)
            printf("*");
        printf("\n");
    }
    return 0;
}