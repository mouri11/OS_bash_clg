#include <unistd.h>
#include <stdio.h>

int main()
{
	pid_t t;
	t = fork();
	printf("This is a common line\n");
	if (t > 0) {
		printf("I am parent. My pid is: %d\n",getpid());
	} else if (t == 0) {
		printf("CHILD. My pid is %d, my ppid is %d\n",getpid(), getppid());
	} else {
		printf("ERROR\n");
	}
	//printf("This line is common\n");
}
