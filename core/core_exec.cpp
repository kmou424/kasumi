void Terminal::prepareVariables(){
	m.init();
}

void Terminal::execCommand(){
	bool is_root = isRoot();
	if(argc > 1){
		if(!strcmp(argv[0], KASUMI_CMD_MODULE)){
			if(is_root){
				if(!strcmp(argv[1], KASUMI_CMD_MODULE_IS_ENABLED) && argc == 2){
					printf("%d\n", m.isEnabled());
				} else if (!strcmp(argv[1], KASUMI_CMD_MODULE_GET_LIST) && argc == 2){
					m.getModulesList();
				} else if(!strcmp(argv[1], KASUMI_CMD_MODULE_SET_ENABLE)){
					switch(argc){
						case 2:
							printErrorHeader();
							printf("You must type 0/1 to enable/disable Module feature after \"%s\"\n", KASUMI_CMD_MODULE_SET_ENABLE);
							break;
						case 3:
							if(!strcmp(argv[2], "0")){
								m.setEnable(MODULES_DISABLED);
							} else if(!strcmp(argv[2], "1")){
								m.setEnable(MODULES_ENABLED);
							}
							break;
					}
				} else {
					printCommandNotFoundError(argv[1]);
				}
			} else {
				printNotExecInRootError(argv[0]);
			}
		} else {
			printCommandNotFoundError(argv[1]);
		}
	} else if(argc == 1){
		if(!strcmp(argv[0], KASUMI_CMD_EXIT)){
			exit(0);
		} else if(!strcmp(argv[0], KASUMI_CMD_MODULE)){
			if(is_root){
				//m.printHelp();
			} else {
				printNotExecInRootError(argv[0]);
			}
		} else {
			printCommandNotFoundError(argv[0]);
		}
	}
}