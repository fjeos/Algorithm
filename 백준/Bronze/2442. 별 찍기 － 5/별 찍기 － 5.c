#include <stdio.h>

int main(void)
{
	int i, j, n, z;
	scanf("%d", &n);

	for (i = 1; i <= n; i++) {
		for (j = (n - i); j > 0; j--) {
			printf(" ");
		}


		for (z = 1; z < 2 * i; z++) {
			printf("*");
		}


		printf("\n");
	}

	return 0;
}