defined = $(findstring $(1), y)
CC := clang
CXXFLAGS += -lstdc++ -O2 -Werror

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
	$(CC) $(SRCS) -o $(OUT) $(CXXFLAGS) $(DEFINE)

clean:
	rm out/kasumi*