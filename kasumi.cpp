#include "core/core.cpp"

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

int main(int argc,char *argv[]){
	Terminal msg;
	if(argc == 1){
		msg.launchTerminal();
	}
	return 0;
}
