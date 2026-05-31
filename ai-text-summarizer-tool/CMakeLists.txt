cmake_minimum_required(VERSION 3.10)
project(AITextSummarizerTool)

set(CMAKE_CXX_STANDARD 17)

find_package(OpenMP REQUIRED)

add_executable(summarizer
    src/main.cpp
    src/summarizer.cpp
    src/analyzer.cpp
)

target_link_libraries(summarizer OpenMP::OpenMP_CXX)
target_include_directories(summarizer PRIVATE include)