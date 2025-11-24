cmake_minimum_required(VERSION 3.5)

set(CMAKE_BUILD_TYPE Debug)

project(server LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)	
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(includes)

add_library(FileManager STATIC IMPORTED) 
set_target_properties(FileManager PROPERTIES
  IMPORTED_LOCATION "${CMAKE_SOURCE_DIR}/src/libFileManager.a"
  INTERFACE_INCLUDE_DIRECTORIES "${CMAKE_SOURCE_DIR}/includes"
)

project(server LANGUAGES CXX)
add_executable(server includes/utils.h src/utils.cpp src/server.cpp includes/clientManager.h src/clientManager.cpp)
target_link_libraries(server pthread  FileManager stdc++fs)


#Replace "client.cpp" with "main_fm.cpp"
project(client LANGUAGES CXX)
add_executable(client includes/utils.h src/utils.cpp src/main_fm.cpp src/fileManagerRemoto.cpp)
target_link_libraries(client pthread stdc++fs)


project (fileManager)
add_executable (fileManager includes/utils.h src/utils.cpp src/main_fm.cpp includes/filemanager.h)
target_link_libraries(fileManager pthread FileManager stdc++fs)

project(broker LANGUAGES CXX)
add_executable(broker includes/utils.h src/utils.cpp src/broker.cpp)
target_link_libraries(broker pthread stdc++fs)
