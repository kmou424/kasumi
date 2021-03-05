defined = $(findstring $(1), y)
CC := clang
CXXFLAGS += -lstdc++ -O2 -Werror
INC = -I ./include

ifeq ($(RELEASE), y)
	DEFINE = -D
endif

ifeq ($(RELEASE), y)
	DEFINE += KASUMI_RELEASE_BUILD
endif

SRCS = kasumi.cpp
OUT = out/kasumi

all: build

build:
	@if [ ! -d "out" ]; then mkdir out; fi
	$(CC) $(SRCS) -o $(OUT) $(CXXFLAGS) $(INC) $(DEFINE)

clean:
	rm out/kasumi*