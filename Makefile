all:
	@if [ ! -d "out" ]; then mkdir out; fi
	clang kasumi.cpp -o out/kasumi -lstdc++

release:
	@if [ ! -d "out" ]; then mkdir out; fi
	clang kasumi.cpp -o out/kasumi -lstdc++ -D KASUMI_RELEASE_BUILD

clean:
	rm out/kasumi*