NAME	=	lib-utad-AEC3.a
INCLUDE	= 	animacion.h \
			mensaje.h \

SRC		=	mensaje.c \
			animacion.c  \

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
	@echo "Removing libftprintf.a ..."	
	${RM} $(NAME)
	@echo "Deleted Objects:  $(words $(NAME))  $(NAME)"
	@echo "Done !"

re: fclean all  