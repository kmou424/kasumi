CC := clang
CXXFLAGS += -lstdc++ -O2 -Werror

ifdef RELEASE
	DEFINE = -D KASUMI_RELEASE_BUILD
else
	DEFINE =
endif

SRCS = kasumi.cpp
OUT = out/kasumi

all: build

build:
	@if [ ! -d "out" ]; then mkdir out; fi
	$(CC) $(SRCS) -o $(OUT) $(CXXFLAGS) $(DEFINE)

clean:
	rm out/kasumi*