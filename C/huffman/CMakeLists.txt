cmake_minimum_required(VERSION 3.8)
project(huffman)

set(CMAKE_C_STANDARD 11)

set(SOURCE_FILES huffman.c huffcode.c huffman.h)
add_library(huffman SHARED ${SOURCE_FILES})
