#*************************************************************************************#
#                                                                                     #
#                                         ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      exam - Algorithms                  ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#                                         ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        01/03/2025         ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#      last change:    15/03/2025         ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
#                                          ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
#                                                                                     #
#       Ismael Hernandez Clemente              ismael.hernandez@live.u-tad.com        #
#                                                                                     #
#       Github:  https://github.com/ismaelucky342/                                    #
#                                                                                     #
#*************************************************************************************#

# Compiler and flags
CXX = g++
CXXFLAGS = 

SRC_DIR = src
INCLUDE_DIR = /home/nirmata/U-Tad/2nd_Course/Q2/Algorithms/Unit_2/AEC2/includes

OBJECTS = $(SRC_DIR)/Ejercicio1.o $(SRC_DIR)/Ejercicio2.o

EXECUTABLES = Ejercicio1 Ejercicio2

all: $(EXECUTABLES)
	@echo "███████╗██╗  ██╗ █████╗ ███╗   ███╗"
	@echo "██╔════╝╚██╗██╔╝██╔══██╗████╗ ████║"
	@echo "█████╗   ╚███╔╝ ███████║██╔████╔██║"
	@echo "██╔══╝   ██╔██╗ ██╔══██║██║╚██╔╝██║"
	@echo "███████╗██╔╝ ██╗██║  ██║██║ ╚═╝ ██║"
	@echo "╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝"
	@echo "U-Tad - Ismael Hernández Clemente"                              

Ejercicio1: $(SRC_DIR)/Ejercicio1.o
	$(CXX) $(CXXFLAGS) -I$(INCLUDE_DIR) -o $@ $^

Ejercicio2: $(SRC_DIR)/Ejercicio2.o
	$(CXX) $(CXXFLAGS) -I$(INCLUDE_DIR) -o $@ $^

$(SRC_DIR)/Ejercicio1.o: $(SRC_DIR)/Ejercicio1.cpp
	$(CXX) $(CXXFLAGS) -I$(INCLUDE_DIR) -c $< -o $@

$(SRC_DIR)/Ejercicio2.o: $(SRC_DIR)/Ejercicio2.cpp
	$(CXX) $(CXXFLAGS) -I$(INCLUDE_DIR) -c $< -o $@

clean:
	rm -f $(OBJECTS) $(EXECUTABLES)

re: clean all

.PHONY: all clean re