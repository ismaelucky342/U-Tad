#*************************************************************************************#
#                                                                                     #
#                                         ██╗   ██╗   ████████╗ █████╗ ██████╗        #
#      AEC4 - Algorithms                  ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗       #
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

CC = g++
CFLAGS = -Wall -Wextra -Werror -Iincludes
SRC_DIR = src
BIN_DIR = bin

SRCS = $(SRC_DIR)/ex01.cpp $(SRC_DIR)/ex02.cpp
OBJS = $(SRCS:$(SRC_DIR)/%.cpp=$(BIN_DIR)/%.o)

EXE1 = $(BIN_DIR)/ex01
EXE2 = $(BIN_DIR)/ex02

all: $(EXE1) $(EXE2)

$(BIN_DIR)/%.o: $(SRC_DIR)/%.cpp | $(BIN_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(EXE1): $(BIN_DIR)/ex01.o
	$(CC) $(CFLAGS) $^ -o $@

$(EXE2): $(BIN_DIR)/ex02.o
	$(CC) $(CFLAGS) $^ -o $@

$(BIN_DIR):
	mkdir -p $(BIN_DIR)

clean:
	rm -rf $(BIN_DIR)

fclean: clean
	rm -rf $(EXE1) $(EXE2)

re: fclean all