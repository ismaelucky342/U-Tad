#**************************************************************************************************#
#                                                                                                  #
#                            ██╗   ██╗   ████████╗ █████╗ ██████╗                                  #
#                            ██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗                                 #
#                            ██║   ██║█████╗██║   ███████║██║  ██║                                 #
#                            ██║   ██║╚════╝██║   ██╔══██║██║  ██║                                 #
#                            ╚██████╔╝      ██║   ██║  ██║██████╔╝                                 #
#                             ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝                                  #
#                                                                                                  #
#                              ismael.hernandez@live.u-tad.com                                     #
#                                                                                                  #
#**************************************************************************************************#

# Nombre del ejecutable
NAME = cache_simulator

# Compilador y opciones
CC = gcc
CFLAGS = #-Wall -Wextra -Werror innecesarias

# Directorios
SRC_DIR = src
OBJ_DIR = obj
INC_DIR = include

# Archivos fuente y objetos
SRCS = $(SRC_DIR)/main.c $(SRC_DIR)/cache.c $(SRC_DIR)/utils.c
OBJS = $(SRCS:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)

# Reglas principales
all: $(NAME)

$(NAME): $(OBJS)
	@echo "\033[1;32mCompilando el ejecutable $(NAME)...\033[0m"
	$(CC) $(CFLAGS) -o $(NAME) $(OBJS) -lm
	@echo "\033[1;32m¡Compilación completada!\033[0m"
	@echo "	"
	@echo "\033[1;34m██╗   ██╗   ████████╗ █████╗ ██████╗          █████╗ ███████╗ ██████╗██████╗ \033[0m"
	@echo "\033[1;34m██║   ██║   ╚══██╔══╝██╔══██╗██╔══██╗        ██╔══██╗██╔════╝██╔════╝╚════██╗\033[0m"
	@echo "\033[1;34m██║   ██║█████╗██║   ███████║██║  ██║        ███████║█████╗  ██║      █████╔╝\033[0m"
	@echo "\033[1;34m██║   ██║╚════╝██║   ██╔══██║██║  ██║        ██╔══██║██╔══╝  ██║      ╚═══██╗\033[0m"
	@echo "\033[1;34m╚██████╔╝      ██║   ██║  ██║██████╔╝███████╗██║  ██║███████╗╚██████╗██████╔╝\033[0m"
	@echo "\033[1;34m ╚═════╝       ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═════╝ \033[0m"
	@echo "\033[1;34m                                23/11/2024   ismael.hernandez@live.u-tad.com      \033[0m"                                   
	@echo ""

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c | $(OBJ_DIR)
	@echo "\033[1;33mCompilando $<...\033[0m"
	$(CC) $(CFLAGS) -I$(INC_DIR) -c $< -o $@

# Crear el directorio de objetos si no existe
$(OBJ_DIR):
	@mkdir -p $(OBJ_DIR)

clean:
	@echo "\033[1;31mEliminando archivos objeto...\033[0m"
	@rm -rf $(OBJ_DIR)

fclean: clean
	@echo "\033[1;31mEliminando el ejecutable $(NAME)...\033[0m"
	@rm -f $(NAME)

re: fclean all
