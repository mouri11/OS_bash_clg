#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main()
{
	pid_t t = vfork();
	if (t > 0) {
		// We are in A
		printf("In A. Pid=%d\n",getpid());
		pid_t te = vfork();
		if (te > 0) {
			printf("In A. Pid: %d, Ppid=%d\n",getpid(),getppid());
			// We are in A
		} else if (te == 0) {
			printf("In E. Pid= %d, PPid=%d\n",getpid(),getppid());
			// We are in E
		}
		exit(0);
	} else if (t == 0) {
		// We are in B
		printf("In B. Pid=%d, PPid=%d\n",getpid(),getppid());
		pid_t tee = vfork();
		if (tee > 0) {
			printf("IN B,  Pid= %d, PPid=%d\n",getpid(),getppid());
			// We are in B
		} else if (tee == 0) {
			// We are in C
			printf("In C  Pid= %d, PPid=%d\n",getpid(),getppid());
			pid_t teee = vfork();
			if (teee > 0) {
				printf("In B  Pid= %d, PPid=%d\n",getpid(),getppid());
				// We are in B
			} else if (teee == 0) {
				printf("In D  Pid= %d, PPid=%d\n",getpid(),getppid());
				// We are in D
			}
			exit(0);
		}
		exit(0);
	}
	exit(0);
}
