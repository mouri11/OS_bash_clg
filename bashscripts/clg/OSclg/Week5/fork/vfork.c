#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main()
{
	pid_t t;
	t = vfork();
	if (t > 0) {
		printf("I am parent\n");
	} else if (t == 0) {
		printf("CHILD\n");
	} else {
		printf("ERROR\n");
		exit(1);
	}
	printf("This line is common\n");
	exit(0);
}
