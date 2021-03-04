all:
	@if [ ! -d "out" ]; then mkdir out; fi
	clang kasumi.cpp -o out/kasumi -lstdc++

clean:
	rm out/kasumi*