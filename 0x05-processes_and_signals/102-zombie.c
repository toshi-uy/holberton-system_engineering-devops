#include <stdio.h>
#include <stdlib.h>

/**
 * infinite_while - infinite loop
 * Return: 0
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
 * main - Main function.
 * 
 * Return: 0 on success.
 */

int main(void)
{
	pid_t z1, z2, z3, z4, z5;

	z1 = fork();
	if (z1 > 0)
		printf("Zombie process created, PID: %d\n", z1);
	else
		return (1);

	z2 = fork();
	if (z2 > 0)
		printf("Zombie process created, PID: %d\n", z2);
	else
		return (1);

	z3 = fork();
	if (z3 > 0)
		printf("Zombie process created, PID: %d\n", z3);
	else
		return (1);

	z4 = fork();
	if (z4 > 0)
		printf("Zombie process created, PID: %d\n", z4);
	else
		return (1);

	z5 = fork();
	if (z5 > 0)
		printf("Zombie process created, PID: %d\n", z5);
	else
		return (1);

	infinite_while();
}