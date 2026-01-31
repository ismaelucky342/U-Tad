 
cmake_minimum_required(VERSION 3.5)

set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project(gestorPersonas LANGUAGES CXX)
add_executable(gestorPersonas persona.h persona.cpp main.cpp)
target_link_libraries(gestorPersonas pthread)

project(clientePersonas LANGUAGES CXX)
add_executable(clientePersonas utils.h utils.cpp persona.h personaRemota.cpp main.cpp)
target_link_libraries(clientePersonas pthread)

project(serverPersonas LANGUAGES CXX)
add_executable(serverPersonas utils.h utils.cpp persona.h persona.cpp server.cpp
							  gestorClientes.h gestorClientes.cpp)
target_link_libraries(serverPersonas pthread)