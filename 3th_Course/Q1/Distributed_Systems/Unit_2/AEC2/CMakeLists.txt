#====================================================================================================#
#                                                                                                    #
#                                                        ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      AEC2 - Sistemas Distribuidos                      ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#                                                        ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        29/10/2025  -  03:00:15           ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#      last change:    15/11/2025  -  02:55:40           ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
#                                                         ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
#                                                                                                    #
#      Ismael Hernandez Clemente                         ismael.hernandez@live.u-tad.com             #
#                                                                                                    #
#      Github:                                           https://github.com/ismaelucky342            #
#                                                                                                    #
#====================================================================================================#

cmake_minimum_required(VERSION 3.10)
project(ChatRoom_ClientServer)

# C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Incluir headers
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

# Ejecutable servidor
add_executable(server src/server.cpp src/utils.cpp)
target_link_libraries(server pthread)

# Ejecutable cliente
add_executable(client src/client.cpp src/utils.cpp)
target_link_libraries(client pthread)

# warnings
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    target_compile_options(server PRIVATE -Wall -Wextra -Wpedantic)
    target_compile_options(client PRIVATE -Wall -Wextra -Wpedantic)
endif()
