void Terminal::prepareVariables(){
	m.init();
}

void Terminal::execCommand(){
	bool is_root = isRoot();
	if(argc > 1){
		if(!strcmp(argv[0], KASUMI_CMD_MODULE)){
			if(is_root){
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