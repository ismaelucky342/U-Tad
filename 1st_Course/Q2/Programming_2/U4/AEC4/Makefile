NAME	=	AEC4.a
INCLUDE	= 	funciones.h 

SRC		=	funciones.c \


OBJ		=	${SRC:.c=.o}

CC		=	gcc
RM		=	rm -f
AR		=	ar rc
RN		=	ranlib

CFLAGS	=	-Wall -Wextra -Werror

.c.o:
	${CC} ${CFLAGS} -c $< -o ${<:.c=.o}

$(NAME):	${OBJ} 
	@echo "Compiling .."
	${AR} ${NAME} ${OBJ}
	${RN} ${NAME}

	@echo "ft_printf compiled!"
	@echo "Compiled Objects:  $(words $(NAME)  ${OBJ})"
	@echo " Done ! "
	
clean:
	@echo "Removing .o  ..."
	${RM} ${OBJ}
	@echo "Deleted Objects: $(words ${OBJ})  ${OBJ}"
	@echo "Done !"

fclean: clean
	@echo "Removing AEC4.a ..."	
	${RM} $(NAME)
	@echo "Deleted Objects:  $(words $(NAME))  $(NAME)"
	@echo "Done !"

re: fclean all  