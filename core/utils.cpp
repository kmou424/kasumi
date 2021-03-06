#include <stdio.h>

void printErrorHeader(){
	printf("\033[31mError:\033[m ");
}

void printCommandNotFoundError(char *command){
	printErrorHeader();
	printf("Command or parameter \"%s\" is not available\n", command);
}
