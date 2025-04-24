 #include <stdio.h>

int main(void)
{
	int i,j,n;
	
	scanf("%d",&i);

	for(j=1; j<=i; j++) 
    {
		for(n=1; n<=j; n++)
			printf("*");
	    printf("\n");
	}
    return 0;
}