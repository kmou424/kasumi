#include <stdio.h>
#include <module.h>

class Module{
	public:
		void init();
		int isEnabled();
		void setEnable(int status);
		char** getModulesList();
	private:
		int module_status;
		char *list[];
};

void Module::init(){
	module_status = MODULES_ENABLED;
}

int Module::isEnabled(){
	return module_status;
}

void Module::setEnable(int status){
	switch(status){
		case MODULES_ENABLED:
			module_status = MODULES_ENABLED;
			break;
		case MODULES_DISABLED:
			module_status = MODULES_DISABLED;
			break;
		default:
			printf("Module: setStatus() failed");
	}
}

char** Module::getModulesList(){
	return list;
}