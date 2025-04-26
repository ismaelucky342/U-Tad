# Compiler and flags
CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++11 -Iincludes

# Directories
SRC_DIR = src
OBJ_DIR = obj

# Targets
TARGET_1 = Ejercicio_1
TARGET_2 = Ejercicio_2

# Source files
SRC_1 = $(SRC_DIR)/Ejercicio_1/Polinomio.cpp $(SRC_DIR)/Ejercicio_1/main.cpp
SRC_2 = $(wildcard $(SRC_DIR)/Ejercicio_2/*.cpp)

# Object files
OBJ_1 = $(SRC_1:$(SRC_DIR)/%.cpp=$(OBJ_DIR)/%.o)
OBJ_2 = $(SRC_2:$(SRC_DIR)/%.cpp=$(OBJ_DIR)/%.o)

# Rules
all: $(TARGET_1) $(TARGET_2)

$(TARGET_1): $(OBJ_1)
	$(CXX) $(CXXFLAGS) -o $@ $^

$(TARGET_2): $(OBJ_2)
	$(CXX) $(CXXFLAGS) -o $@ $^

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	@mkdir -p $(dir $@)
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	$(RM) -r $(OBJ_DIR) $(TARGET_1) $(TARGET_2)

re: clean all

.PHONY: all clean
