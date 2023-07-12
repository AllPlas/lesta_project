cmake_minimum_required(VERSION 3.22)

if (EXISTS ${CMAKE_BINARY_DIR}/conan_toolchain.cmake)
    set(CMAKE_TOOLCHAIN_FILE ${CMAKE_BINARY_DIR}/conan_toolchain.cmake)
endif ()

project(lesta_project)

if (WIN32)
    set(CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS ON)
endif ()

set(DataDir ${CMAKE_CURRENT_SOURCE_DIR}/data)

add_subdirectory(engine)
add_subdirectory(game)
