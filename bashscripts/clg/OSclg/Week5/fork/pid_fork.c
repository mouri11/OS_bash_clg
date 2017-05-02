#include <unistd.h>
#include <stdio.h>

int main()
{
	pid_t t;
	t = fork();
	if (t > 0) {
		printf("I am parent. My pid is: %d\n",getpid());
	} else if (t == 0) {
		printf("CHILD. My ppid is %d\n",getppid());
	} else {
		printf("ERROR\n");
	}
	printf("This line is common\n");
}
