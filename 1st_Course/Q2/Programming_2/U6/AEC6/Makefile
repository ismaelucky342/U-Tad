CC = gcc
CFLAGS = -Wall -Wextra -Werror -std=c99
SRCDIR = src
OBJDIR = obj

SRCFILES = $(wildcard $(SRCDIR)#.c)
OBJFILES = $(patsubst $(SRCDIR)/%.c, $(OBJDIR)/%.o, $(SRCFILES))
EXECUTABLE = program.exe

.PHONY: all clean fclean

all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJFILES)
	$(CC) $(CFLAGS) $^ -o $@

$(OBJDIR)/%.o: $(SRCDIR)/%.c
	@mkdir -p $(OBJDIR)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -rf $(OBJDIR)

fclean: clean
	rm -f $(EXECUTABLE)

