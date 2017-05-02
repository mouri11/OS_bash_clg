#include <unistd.h>
#include <stdio.h>

int main()
{
	pid_t t;
	t = fork();
	if (t > 0) {
		printf("I am parent\n");
	} else if (t == 0) {
		printf("CHILD\n");
	} else {
		printf("ERROR\n");
	}
	printf("This line is common\n");
}
