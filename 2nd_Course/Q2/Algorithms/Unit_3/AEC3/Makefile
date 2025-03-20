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

# Variables
CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++11
INCLUDES = -I./includes
SRC = src/
OBJ_DIR = obj/

SRCS_HANOI = $(SRC)hanoi.cpp $(SRC)Stack.cpp
SRCS_RULETA = $(SRC)RussianRoulette.cpp

OBJS_HANOI = $(SRCS_HANOI:$(SRC)%.cpp=$(OBJ_DIR)%.o)
OBJS_RULETA = $(SRCS_RULETA:$(SRC)%.cpp=$(OBJ_DIR)%.o)

EXEC_HANOI = hanoi
EXEC_RULETA = roulette

all: $(EXEC_HANOI) $(EXEC_RULETA)

$(EXEC_HANOI): $(OBJS_HANOI)
	$(CXX) $(CXXFLAGS) $(INCLUDES) -o $@ $^

$(EXEC_RULETA): $(OBJS_RULETA)
	$(CXX) $(CXXFLAGS) $(INCLUDES) -o $@ $^

$(OBJ_DIR)%.o: $(SRC)%.cpp
	@mkdir -p $(OBJ_DIR)
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

$(OBJ_DIR)%.o: $(SRC)%.cpp
	@mkdir -p $(OBJ_DIR)
	$(CXX) $(CXXFLAGS) $(INCLUDES) -c $< -o $@

clean:
	rm -rf $(OBJ_DIR)

fclean: clean
	rm -f $(EXEC_HANOI) $(EXEC_RULETA)

re: fclean all

.PHONY: all clean fclean re
