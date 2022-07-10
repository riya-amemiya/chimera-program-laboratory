CXX = g++
OBJDIR = ./obj
INCLUDE = ./lib/include
NAME = Mainapp
CFLAGS = -Wall -O3 -std=c++11
SOURCES  = $(wildcard lib/cpp/*.cpp)
OBJECTS  = $(addprefix $(OBJDIR)/, lib$(notdir $(SOURCES:.cpp=.so)))
RUST_DIR = target/release
RUST = $(wildcard $(RUST_DIR)/*.dylib)
RUST_SOURCES = $(wildcard src/*.rs)
CYTHON = $(wildcard calc.*.so)
CYTHON_SOURCES = $(wildcard lib/cython/*.pyx)
GOLANG = $(wildcard lib/go/*.go)
RS_CPP_HPP = $(INCLUDE)/rs.hpp
CARGO = Cargo.toml

$(CYTHON): $(RS_CPP_HPP) $(OBJECTS) $(RUST) $(CYTHON_SOURCES)
	sudo CFLAGS=-stdlib=libc++ python setup.py build_ext -i

$(INCLUDE)/rs.hpp: $(RUST_SOURCES)
	cbindgen . -o lib/include/rs.hpp
	python script/index.py

$(NAME): $(OBJECTS) $(RUST)
	$(CXX) -o $@ $^ -g

$(OBJDIR):
	mkdir $(OBJDIR)

$(OBJDIR)/lib%.so: $(SOURCES) $(OBJDIR)

	@[ -d $(OBJDIR) ]
	$(CXX) $(CFLAGS) -I$(INCLUDE) -c -o $@ $<

$(RUST_DIR)/%.dylib: $(RUST_SOURCES) $(CARGO) $(GOLANG)
	cd lib/go && go build -buildmode=c-archive -o libgo_main.a main.go
	cargo build --release

.PHONY: check
check:
	cppcheck --enable=all ./
.PHONY: clean
clean:
	$(RM) obj/*.o
.PHONY:build
build:
	cbindgen . -o lib/include/rs.hpp
	python script/index.py
	cargo build --release
	mkdir obj
	g++ -Wall -O3 -std=c++11 -I./lib/include -c -o obj/libmain.so lib/cpp/main.cpp
	sudo CFLAGS=-stdlib=libc++ python setup.py build_ext -i

.PHONY: Rustbuild

Rustbuild:
	cd lib/go && go build -buildmode=c-archive -o libhellogo.a main.go
	cargo build --release
	cbindgen . -o lib/include/rs.hpp
	python script/index.py