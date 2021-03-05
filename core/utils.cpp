#include <stdio.h>

void printCommandNotFoundError(char *command){
	printf("\033[31mError:\033[m Command or parameter \"%s\" is not available\n", command);
}
