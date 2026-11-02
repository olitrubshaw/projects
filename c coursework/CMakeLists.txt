cmake_minimum_required(VERSION 3.20)
project(c_coursework C)

set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED ON)

add_executable(c_coursework main.c List.c Exoplanet.c ExoplanetTest.c)
