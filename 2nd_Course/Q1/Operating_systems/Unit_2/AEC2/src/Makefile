# Compiler
CC = gcc

# Compiler flags
CFLAGS = -Wall -Wextra -Werror -pthread

# Source files
SRCS = mini_philosophers.c

# Header files
HDRS = mini_philosophers.h

# Output executable
TARGET = a.out

# Object files
OBJS = $(SRCS:.c=.o)

# Default target
all: $(TARGET)

# Link object files to create the executable
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^

# Compile source files into object files
%.o: %.c $(HDRS)
	$(CC) $(CFLAGS) -c $< -o $@

# Clean up build files
clean:
	rm -f $(OBJS) $(TARGET)
# Recompile the project
re: clean all

# Phony targets
.PHONY: all clean
