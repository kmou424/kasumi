// kasumi attrs
#define KASUMI_VERSION "1.0"
#define KASUMI_SUBVERSION "1"

#ifdef KASUMI_RELEASE_BUILD
	#define KASUMI_BUILD_TYPE "Release";
#else
	#define KASUMI_BUILD_TYPE "Debug";
#endif

// kasumi runtime constants
#define COMMAND_PARAMETERS_MAX 64
#define COMMAND_LENGTH_MAX 256

// kasumi command constants
#define KASUMI_CMD_MODULE "kmod"
#define KASUMI_CMD_MODULE_IS_ENABLED "isEnabled"
#define KASUMI_CMD_MODULE_SET_ENABLE "setEnable"
#define KASUMI_CMD_MODULE_GET_LIST "getModulesList"
#define KASUMI_CMD_EXIT "exit"