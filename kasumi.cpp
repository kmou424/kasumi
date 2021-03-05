#include "core/core.cpp"

void printCommandNotFoundError(char *command){
	printf("\033[31mError:\033[m Command or parameter \"%s\" is not available\n", command);
}

void Terminal::prepareVariables(){
	m.init();
}

void Terminal::execCommand(){
	if(argc > 1){
		if(!strcmp(argv[0], KASUMI_CMD_MODULE)){
			switch(argc){
				case 2:
					if(!strcmp(argv[1], KASUMI_CMD_MODULE_IS_ENABLED)){
						printf("%d\n", m.isEnabled());
					} else if (!strcmp(argv[1], KASUMI_CMD_MODULE_GET_LIST)){
						m.getModulesList();
					} else {
						printCommandNotFoundError(argv[1]);
					}
					break;
				case 3:
					if(!strcmp(argv[1], KASUMI_CMD_MODULE_SET_ENABLE)){
						int enable;
						if(!strcmp(argv[2], "0")){
							enable = 0;
						} else {
							enable = 1;
						}
						m.setEnable(enable);
					} else {
						printCommandNotFoundError(argv[1]);
					}
					break;
				default:
					printCommandNotFoundError(argv[1]);
					break;
			}
		} else {
			system(cmd_s);
		}
	} else if(argc == 1){
		if(!strcmp(argv[0], KASUMI_CMD_EXIT)){
			exit(0);
		} else if(!strcmp(argv[0], KASUMI_CMD_MODULE)){
			//m.printHelp();
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