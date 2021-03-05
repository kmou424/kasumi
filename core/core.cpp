#include <cstdio>
#include <cstring>
#include <fstream>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <unistd.h>

#include <constants.h>

using namespace std;

class Terminal{
	public:
		// init variables
		int argc;
		char *argv[COMMAND_PARAMETERS_MAX];
		char cmd_s[COMMAND_LENGTH_MAX];
		char root_identifier;
	public:
		void launchTerminal();
	private:
		void welcomeToKasumi();
		void setRootIdentifier();
		void processCommand();
		void execCommand();
};

void Terminal::launchTerminal(){
	welcomeToKasumi();
	while (true){
		setRootIdentifier();
		printf("\033[31m♡kasumi♡ \033[m %c ~> ", root_identifier);
		char *res = NULL;
		res = fgets(cmd_s, COMMAND_LENGTH_MAX - 1, stdin);
		if (res == NULL && ferror(stdin)){
			printf("Input error\n");
		}
		processCommand();
		execCommand();
	}
}

void Terminal::welcomeToKasumi(){
	string header;
	string banner;
	string version;
	string build_type;
	string footer;
	int all_len;
	int version_len;
	int build_type_len;
	banner = "│ Welcome to \033[31mkasumi\033[m      │";
	all_len = banner.size() - 14;
	header = "┌";
	footer = "└";
	for(int i = 0; i < all_len; i++){
		header = header + "─";
		footer = footer + "─";
	}
	header = header + "┐";
	footer = footer + "┘";
	version = "│ Version: " + (string)KASUMI_VERSION + "." + (string)KASUMI_SUBVERSION;
	#ifdef KASUMI_RELEASE_BUILD
		build_type = "│ Build type: Release";
	#else
		build_type = "│ Build type: Debug";
	#endif
	version_len = version.size();
	build_type_len = build_type.size();
	for(int i = 0; i < all_len - version_len + 2; i++){
		version = version + " ";
	}
	for(int i = 0; i < all_len - build_type_len + 2; i++){
		build_type = build_type + " ";
	}
	version = version + " │";
	build_type = build_type + " │";
	printf("%s\n%s\n%s\n%s\n%s\n", header.c_str(), banner.c_str(), version.c_str(), build_type.c_str(), footer.c_str());
}

void Terminal::setRootIdentifier(){
	if (geteuid() == 0)
        root_identifier = '#';
    else
        root_identifier = '$';
}

void Terminal::execCommand(){
	if(argc > 1){
		system(cmd_s);
	} else if(argc == 1){
		if(!strcmp(argv[0], KASUMI_CMD_EXIT)){
			exit(0);
		} else {
			system(argv[0]);
		}
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