#*************************************************************************************#
#                                                                                     #
#                                         ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      AEC1 - Algorithms                  ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
#                                         ██║   ██║█████╗██║   ███████║██║  ██║       #
#      created:        01/02/2025         ██║   ██║╚════╝██║   ██╔══██║██║  ██║       #
#      last change:    02/03/2025         ╚██████╔╝      ██║   ██║  ██║██████╔╝       #
#                                          ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝        #
#                                                                                     #
#       Ismael Hernandez Clemente              ismael.hernandez@live.u-tad.com        #
#                                                                                     #
#       Github:  https://github.com/ismaelucky342/                                    #
#                                                                                     #
#*************************************************************************************#

# Makefile for Sum of First N Numbers and Palindrome Checker

# Compiler and flags
CXX = g++
CXXFLAGS = -std=c++11 -Wall

# Directory where the source files are located
SRC_DIR = src

# Object files
OBJECTS = $(SRC_DIR)/SumFirstNNumbers.o $(SRC_DIR)/Palindrome.o

# Executables
EXECUTABLES = SumFirstNNumbers Palindrome

# Default target
all: $(EXECUTABLES)

# Target to create SumFirstNNumbers executable
SumFirstNNumbers: $(SRC_DIR)/SumFirstNNumbers.o
	$(CXX) $(CXXFLAGS) -o $@ $^

# Target to create Palindrome executable
Palindrome: $(SRC_DIR)/Palindrome.o
	$(CXX) $(CXXFLAGS) -o $@ $^

# Rule to compile SumFirstNNumbers.cpp into an object file
$(SRC_DIR)/SumFirstNNumbers.o: $(SRC_DIR)/SumFirstNNumbers.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Rule to compile Palindrome.cpp into an object file
$(SRC_DIR)/Palindrome.o: $(SRC_DIR)/Palindrome.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Clean up object files and executables
clean:
	rm -f $(OBJECTS) $(EXECUTABLES)

# Phony targets (not associated with files)
.PHONY: all clean
