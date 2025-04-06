# Networks and Operating Systems Laboratory | Unit 6

## Text Editors. Bash Scripting

## **Text Editors in Linux**

### **1. Vim**

Vim is a highly configurable text editor used for editing code and text. It is an enhanced version of the original `vi` editor.

### **Basic Commands**

- **Start Vim**:
    
    ```bash
    bash
    CopyEdit
    vim filename  # Opens the file in Vim editor
    
    ```
    
- **Insert Mode**:
Press `i` to enter insert mode, where you can type and edit text.
- **Command Mode**:
Press `Esc` to return to command mode, where you can issue commands to Vim.
- **Save and Quit**:
    - `:w`: Save the file.
    - `:q`: Quit the editor.
    - `:wq`: Save and quit.
    - `:q!`: Quit without saving.
- **Search**:
    - Press `/` followed by the search term to search forward.
    - Press `?` followed by the search term to search backward.
    - Press `n` to jump to the next match.
- **Undo and Redo**:
    - Press `u` to undo.
    - Press `Ctrl + r` to redo.
- **Copy, Cut, and Paste**:
    - `yy`: Copy the current line.
    - `dd`: Cut the current line.
    - `p`: Paste after the cursor.
    - `P`: Paste before the cursor.
- **Navigation**:
    - Press `j` to move down, `k` to move up, `h` to move left, and `l` to move right.
    - Press `:number` to jump to a specific line number.

### **2. Nano**

Nano is a simple and easy-to-use text editor that is available by default on many Linux distributions. It is ideal for beginners or those who need to quickly edit configuration files.

### **Basic Commands**

- **Start Nano**:
    
    ```bash
    bash
    CopyEdit
    nano filename  # Opens the file in Nano editor
    
    ```
    
- **Save and Quit**:
    - `Ctrl + O`: Save the file (you will be prompted to confirm the filename).
    - `Ctrl + X`: Exit Nano (you will be prompted to save if there are unsaved changes).
- **Cut, Copy, and Paste**:
    - `Ctrl + K`: Cut the current line.
    - `Ctrl + U`: Paste the cut line.
    - `Ctrl + Shift + 6`: Mark text to copy.
    - `Ctrl + Shift + 6` (again): Copy the marked text.
- **Search**:
    - `Ctrl + W`: Search for a string in the text.
    - `Ctrl + \`: Replace a string.
- **Navigation**:
    - `Ctrl + A`: Move to the beginning of the line.
    - `Ctrl + E`: Move to the end of the line.
    - `Ctrl + Y`: Move up one page.
    - `Ctrl + V`: Move down one page.

### **3. Emacs**

Emacs is a powerful text editor with a steep learning curve but many advanced features, including an integrated development environment (IDE).

### **Basic Commands**

- **Start Emacs**:
    
    ```bash
    bash
    CopyEdit
    emacs filename  # Opens the file in Emacs editor
    
    ```
    
- **Save and Quit**:
    - `Ctrl + X, Ctrl + S`: Save the file.
    - `Ctrl + X, Ctrl + C`: Quit Emacs (prompts to save if necessary).
- **Cut, Copy, and Paste**:
    - `Ctrl + K`: Cut the text from the cursor to the end of the line.
    - `Ctrl + Y`: Paste the cut text.
    - `Ctrl + W`: Cut the selected text.
    - `Alt + W`: Copy the selected text.
- **Search**:
    - `Ctrl + S`: Search forward.
    - `Ctrl + R`: Search backward.
- **Navigation**:
    - `Ctrl + A`: Move to the beginning of the line.
    - `Ctrl + E`: Move to the end of the line.
    - `Ctrl + F`: Move forward one character.
    - `Ctrl + B`: Move backward one character.

---

## **Bash Scripting**

### **What is Bash Scripting?**

Bash scripting is the process of writing scripts for the Bash shell, which is the default command-line interface on many Unix-like operating systems. Bash scripts can automate tasks, process files, and execute commands in sequence.

### **Basic Structure of a Bash Script**

A basic Bash script consists of a series of commands that are executed sequentially. Here’s an example:

```bash

#!/bin/bash

# This is a comment
echo "Hello, World!"  # Prints "Hello, World!" to the terminal

```

- The `#!/bin/bash` at the top is called a shebang. It tells the system that the script should be run using the Bash shell.
- Lines starting with `#` are comments and are not executed.
- `echo` is a command that prints text to the terminal.

### **Running a Bash Script**

To run a Bash script, follow these steps:

1. Make the script executable:
    
    ```bash
    bash
    CopyEdit
    chmod +x script.sh
    
    ```
    
2. Execute the script:
    
    ```bash
    bash
    CopyEdit
    ./script.sh
    
    ```
    

### **Variables in Bash Scripts**

Variables are used to store data in Bash scripts. You can create a variable like this:

```bash

#!/bin/bash

name="Alice"  # Assign value to the variable
echo "Hello, $name!"  # Prints "Hello, Alice!"

```

- Variables are referenced using `$`.
- No spaces around the `=` sign when assigning values to variables.

### **Conditional Statements**

Bash scripts can include conditional statements to execute different commands based on conditions.

```bash

#!/bin/bash

if [ $1 -gt 10 ]; then
    echo "The number is greater than 10"
else
    echo "The number is less than or equal to 10"
fi

```

- `$1` refers to the first argument passed to the script.
- `gt` checks if the first number is greater than the second.
- The `if` statement executes the command following `then` if the condition is true, otherwise the command after `else` is executed.

### **Loops in Bash Scripts**

Bash supports loops, which allow you to repeat actions. Here's an example of a `for` loop:

```bash

#!/bin/bash

for i in {1..5}
do
    echo "Iteration $i"
done

```

- The loop will print "Iteration 1", "Iteration 2", ..., "Iteration 5".

You can also use `while` loops:

```bash

#!/bin/bash

count=1
while [ $count -le 5 ]
do
    echo "Count is $count"
    ((count++))
done

```

### **Functions in Bash Scripts**

Functions allow you to organize your script into reusable blocks of code.

```bash

#!/bin/bash

function greet {
    echo "Hello, $1!"
}

greet "Alice"

```

- `greet` is a function that takes one argument (`$1`), which is printed in the message.

### **Reading Input in Bash Scripts**

You can prompt the user for input with the `read` command:

```bash

#!/bin/bash

echo "Enter your name:"
read name
echo "Hello, $name!"

```

- The script will prompt the user to enter their name and then greet them.

### **Example of a Full Bash Script**

Here’s a simple Bash script that accepts user input, checks a condition, and performs an action:

```bash

#!/bin/bash

echo "Enter a number:"
read number

if [ $number -gt 10 ]; then
    echo "The number is greater than 10"
else
    echo "The number is 10 or less"
fi

```
