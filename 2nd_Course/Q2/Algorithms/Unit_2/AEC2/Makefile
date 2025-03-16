#*************************************************************************************#
#                                                                                     #
#                                         ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      AEC2 - Algorithms                  ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
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

# Makefile for ex00 and ex01

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++11 -Wall

SRC_DIR = src
INCLUDE_DIR = /home/nirmata/U-Tad/2nd_Course/Q2/Algorithms/Unit_2/AEC2/includes

OBJECTS = $(SRC_DIR)/ex00.o $(SRC_DIR)/ex01.o

EXECUTABLES = ex00 ex01

all: $(EXECUTABLES)

ex00: $(SRC_DIR)/ex00.o
	$(CXX) $(CXXFLAGS) -I$(INCLUDE_DIR) -o $@ $^

ex01: $(SRC_DIR)/ex01.o
	$(CXX) $(CXXFLAGS) -I$(INCLUDE_DIR) -o $@ $^

$(SRC_DIR)/ex00.o: $(SRC_DIR)/ex00.cpp
	$(CXX) $(CXXFLAGS) -I$(INCLUDE_DIR) -c $< -o $@

$(SRC_DIR)/ex01.o: $(SRC_DIR)/ex01.cpp
	$(CXX) $(CXXFLAGS) -I$(INCLUDE_DIR) -c $< -o $@

clean:
	rm -f $(OBJECTS) $(EXECUTABLES)

re: clean all

.PHONY: all clean re
