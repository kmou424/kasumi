#include "core/core.cpp"
#include "core/core_exec.cpp"

int main(int argc,char *argv[]){
	Terminal msg;
	if(argc == 1){
		msg.launchTerminal();
	}
	return 0;
}