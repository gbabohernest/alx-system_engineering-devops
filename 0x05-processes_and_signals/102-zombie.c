#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
* infinite_while - Run an infinite while loop.
*
* Return: Always 0.
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
* main - Creates five zombie processes.
*
* Return: Always 0.
*/

int main(void)
{
	pid_t pid;
	char count = 0;

	while (count < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
			count++;
		}
		else if (pid == 0)
		{
			exit(0); /*child exits immediately, becoming a zombie*/
		}
		else
		{
			perror("fork");
			return (EXIT_FAILURE);
		}
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
