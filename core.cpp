#include <cstdio>
#include <cstring>
#include <fstream>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>

using namespace std;

#define COMMAND_PARAMETERS_MAX 64
#define COMMAND_LENGTH_MAX 256

class Terminal{
	public:
		int argc;
		char *argv[COMMAND_PARAMETERS_MAX];
		char cmd_s[COMMAND_LENGTH_MAX];
	public:
		void launchTerminal();
	private:
		void processCommand();
		void execCommand();
};

void Terminal::launchTerminal(){
	while (true){
		printf("\033[31m♡kasumi♡ \033[37m~> ");
		char *res = NULL;
		res = fgets(cmd_s, COMMAND_LENGTH_MAX - 1, stdin);
		if (res == NULL && ferror(stdin)){
			printf("Input error\n");
		}
		processCommand();
		execCommand();
	}
}

void Terminal::execCommand(){
	if(argc > 0 && strcmp(argv[0], "exit") == 0){
		exit(0);
	}
}

void Terminal::processCommand(){
	int len = strlen(cmd_s);
	cmd_s[len - 1] = ' ';
	argc = 0;
	char tmp_str[COMMAND_LENGTH_MAX];
	int position_tmp_str=0;
	
	// fuck up the space at first position of command
	int start = 0;
	bool cycleable = true;
	while (cycleable){
		if(cmd_s[start] != ' '){
			cycleable = false;
		} else {
			start++;
		}
	}
	// allocate argc and argv
	for (int i=start; i<=len; i++){
		if (cmd_s[i] != ' '){
			tmp_str[position_tmp_str++]=cmd_s[i];
		}else{
			tmp_str[position_tmp_str]='\0';
			int tmp_str_len = strlen(tmp_str);
			argv[argc] = (char *)malloc(sizeof(char)*(tmp_str_len + 1));
			strcpy(argv[argc], tmp_str);
			if (cmd_s[i + 1] != ' '){
				argc++;
			}
			position_tmp_str=0;
		}
	}
}