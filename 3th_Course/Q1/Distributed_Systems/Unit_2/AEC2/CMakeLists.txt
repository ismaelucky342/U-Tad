cmake_minimum_required(VERSION 3.10)
project(ChatRoom_ClientServer)

# Configuración de C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Incluir directorio de headers
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include)

# Buscar la librería libUtils (ajusta la ruta según tu sistema)
# Suponiendo que libUtils está en el directorio lib/
link_directories(${CMAKE_CURRENT_SOURCE_DIR}/lib)

# Ejecutable del servidor
add_executable(server src/server.cpp)
target_link_libraries(server Utils pthread)

# Ejecutable del cliente
add_executable(client src/client.cpp)
target_link_libraries(client Utils pthread)

# Configuración de warnings
if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
    target_compile_options(server PRIVATE -Wall -Wextra -Wpedantic)
    target_compile_options(client PRIVATE -Wall -Wextra -Wpedantic)
endif()
