# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.8

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/Users/alexandersolovyov/Downloads/huffman-master 3"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/Users/alexandersolovyov/Downloads/huffman-master 3/cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/huffman.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/huffman.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/huffman.dir/flags.make

CMakeFiles/huffman.dir/huffman.c.o: CMakeFiles/huffman.dir/flags.make
CMakeFiles/huffman.dir/huffman.c.o: ../huffman.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/Users/alexandersolovyov/Downloads/huffman-master 3/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/huffman.dir/huffman.c.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/huffman.dir/huffman.c.o   -c "/Users/alexandersolovyov/Downloads/huffman-master 3/huffman.c"

CMakeFiles/huffman.dir/huffman.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/huffman.dir/huffman.c.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E "/Users/alexandersolovyov/Downloads/huffman-master 3/huffman.c" > CMakeFiles/huffman.dir/huffman.c.i

CMakeFiles/huffman.dir/huffman.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/huffman.dir/huffman.c.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S "/Users/alexandersolovyov/Downloads/huffman-master 3/huffman.c" -o CMakeFiles/huffman.dir/huffman.c.s

CMakeFiles/huffman.dir/huffman.c.o.requires:

.PHONY : CMakeFiles/huffman.dir/huffman.c.o.requires

CMakeFiles/huffman.dir/huffman.c.o.provides: CMakeFiles/huffman.dir/huffman.c.o.requires
	$(MAKE) -f CMakeFiles/huffman.dir/build.make CMakeFiles/huffman.dir/huffman.c.o.provides.build
.PHONY : CMakeFiles/huffman.dir/huffman.c.o.provides

CMakeFiles/huffman.dir/huffman.c.o.provides.build: CMakeFiles/huffman.dir/huffman.c.o


CMakeFiles/huffman.dir/huffcode.c.o: CMakeFiles/huffman.dir/flags.make
CMakeFiles/huffman.dir/huffcode.c.o: ../huffcode.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/Users/alexandersolovyov/Downloads/huffman-master 3/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Building C object CMakeFiles/huffman.dir/huffcode.c.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/huffman.dir/huffcode.c.o   -c "/Users/alexandersolovyov/Downloads/huffman-master 3/huffcode.c"

CMakeFiles/huffman.dir/huffcode.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/huffman.dir/huffcode.c.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E "/Users/alexandersolovyov/Downloads/huffman-master 3/huffcode.c" > CMakeFiles/huffman.dir/huffcode.c.i

CMakeFiles/huffman.dir/huffcode.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/huffman.dir/huffcode.c.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S "/Users/alexandersolovyov/Downloads/huffman-master 3/huffcode.c" -o CMakeFiles/huffman.dir/huffcode.c.s

CMakeFiles/huffman.dir/huffcode.c.o.requires:

.PHONY : CMakeFiles/huffman.dir/huffcode.c.o.requires

CMakeFiles/huffman.dir/huffcode.c.o.provides: CMakeFiles/huffman.dir/huffcode.c.o.requires
	$(MAKE) -f CMakeFiles/huffman.dir/build.make CMakeFiles/huffman.dir/huffcode.c.o.provides.build
.PHONY : CMakeFiles/huffman.dir/huffcode.c.o.provides

CMakeFiles/huffman.dir/huffcode.c.o.provides.build: CMakeFiles/huffman.dir/huffcode.c.o


# Object files for target huffman
huffman_OBJECTS = \
"CMakeFiles/huffman.dir/huffman.c.o" \
"CMakeFiles/huffman.dir/huffcode.c.o"

# External object files for target huffman
huffman_EXTERNAL_OBJECTS =

libhuffman.dylib: CMakeFiles/huffman.dir/huffman.c.o
libhuffman.dylib: CMakeFiles/huffman.dir/huffcode.c.o
libhuffman.dylib: CMakeFiles/huffman.dir/build.make
libhuffman.dylib: CMakeFiles/huffman.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/Users/alexandersolovyov/Downloads/huffman-master 3/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_3) "Linking C shared library libhuffman.dylib"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/huffman.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/huffman.dir/build: libhuffman.dylib

.PHONY : CMakeFiles/huffman.dir/build

CMakeFiles/huffman.dir/requires: CMakeFiles/huffman.dir/huffman.c.o.requires
CMakeFiles/huffman.dir/requires: CMakeFiles/huffman.dir/huffcode.c.o.requires

.PHONY : CMakeFiles/huffman.dir/requires

CMakeFiles/huffman.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/huffman.dir/cmake_clean.cmake
.PHONY : CMakeFiles/huffman.dir/clean

CMakeFiles/huffman.dir/depend:
	cd "/Users/alexandersolovyov/Downloads/huffman-master 3/cmake-build-debug" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/Users/alexandersolovyov/Downloads/huffman-master 3" "/Users/alexandersolovyov/Downloads/huffman-master 3" "/Users/alexandersolovyov/Downloads/huffman-master 3/cmake-build-debug" "/Users/alexandersolovyov/Downloads/huffman-master 3/cmake-build-debug" "/Users/alexandersolovyov/Downloads/huffman-master 3/cmake-build-debug/CMakeFiles/huffman.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/huffman.dir/depend

