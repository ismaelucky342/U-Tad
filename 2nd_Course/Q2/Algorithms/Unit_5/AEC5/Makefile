#*************************************************************************************#
#                                                                                     #
#                                         ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      AEC5 - Algorithms                  ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#                                         ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        01/04/2025         ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#      last change:    15/04/2025         ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
#                                          ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
#                                                                                     #
#       Ismael Hernandez Clemente              ismael.hernandez@live.u-tad.com        #
#                                                                                     #
#       Github:  https://github.com/ismaelucky342/                                    #
#                                                                                     #
#*************************************************************************************#



# Compiler and flags
CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++17 -Iincludes

# Directories
SRC_DIR = src
INCLUDE_DIR = includes
OBJ_DIR = obj

# Executables
EXEC1 = ejercicio_1
EXEC2 = ejercicio_2

# Source files
SRC1 = $(SRC_DIR)/Ejercicio_1/agenda.cpp $(SRC_DIR)/Ejercicio_1/mainAgenda.cpp
SRC2 = $(SRC_DIR)/Ejercicio_2/Agenda_colisiones.cpp \
	$(SRC_DIR)/Ejercicio_2/ListaEnlazada.cpp \
	$(SRC_DIR)/Ejercicio_2/Nodo.cpp \
	$(SRC_DIR)/Ejercicio_2/contacto.cpp \
	$(SRC_DIR)/Ejercicio_2/mainAgendaColisiones.cpp

# Object files
OBJ1 = $(SRC1:$(SRC_DIR)/%.cpp=$(OBJ_DIR)/%.o)
OBJ2 = $(SRC2:$(SRC_DIR)/%.cpp=$(OBJ_DIR)/%.o)

# Targets
all: $(EXEC1) $(EXEC2)
	@echo "Building all executables..."
	@echo "Congratulations!!! Build complete."


# Build executable 1
$(EXEC1): $(OBJ1)
	$(CXX) $(CXXFLAGS) $^ -o $@

# Build executable 2
$(EXEC2): $(OBJ2)
	$(CXX) $(CXXFLAGS) $^ -o $@

# Compile source files to object files
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	@mkdir -p $(OBJ_DIR)/Ejercicio_1
	@mkdir -p $(OBJ_DIR)/Ejercicio_2
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean build files
clean:
	rm -rf $(OBJ_DIR) $(EXEC1) $(EXEC2)

# Full clean (clean + remove additional files if needed)
fclean: clean

# Rebuild everything
re: fclean all

# Phony targets
.PHONY: all clean fclean re
