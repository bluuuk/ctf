#include <stdio.h>

int main()
{
	printf("size:%ld\n", sizeof(int));
	int k = 1;
	char a[] = "ABCD";
	int j = 1;
	printf("%p\n", (void *)&k);
	for (int i = 0; i < 5; i++)
	{
		printf("%u-%u\t%p\n", i, *(a + i), (void *)(a + i));
	}
	printf("%p\n", (void *)&j);
	a[5] = 1;
	printf("%s,%d", a, k);
}
