# Networks and Operating Systems Laboratory | Unit 2

## Basic Linux Commands

### Commands for Navigating and Viewing Directories

1. **`pwd`** (Print Working Directory)
    
    Displays the current directory you are in.
    
2. **`cd`** (Change Directory)
    
    Changes the current working directory.
    
    ```bash
    $ cd /path/to/directory
    ```
    
3. **`ls`** (List)
    
    Displays the contents of the current directory.
    
    ```bash
    $ ls
    file1.txt  file2.txt  directory1
    ```
    
4. **`ls -l`**
    
    Displays the contents of the directory with details (permissions, size, date).
    
    ```bash
    $ ls -l
    ```
    
5. **`ls -a`**
    
    Displays all files, including hidden ones (those starting with a dot `.`).
    
    ```bash
    $ ls -a
    ```

---

### Commands for File and Directory Operations

1. **`touch`**
    
    Creates an empty file or updates the modification date of an existing file.
    
    ```bash
    $ touch file.txt
    ```
    
2. **`mkdir`** (Make Directory)
    
    Creates a new directory.
    
    ```bash
    $ mkdir new_directory
    ```
    
3. **`cp`** (Copy)
    
    Copies files or directories.
    
    ```bash
    $ cp file.txt /destination/path/
    ```
    
4. **`mv`** (Move)
    
    Moves or renames files and directories.
    
    ```bash
    $ mv file.txt /destination/path/
    ```
    
5. **`rm`** (Remove)
    
    Deletes files.
    
    ```bash
    $ rm file.txt
    ```
    
6. **`rm -r`**
    
    Recursively deletes directories (including files inside them).
    
    ```bash
    $ rm -r directory/
    ```
    
7. **`rmdir`** (Remove Directory)
    
    Deletes an empty directory.
    
    ```bash
    $ rmdir empty_directory
    ```

---

### Commands for Viewing File Contents

1. **`cat`** (Concatenate)
    
    Displays the contents of a file.
    
    ```bash
    $ cat file.txt
    ```
    
2. **`less`**
    
    Displays the contents of a file in a paginated manner.
    
    ```bash
    $ less file.txt
    ```
    
3. **`head`**
    
    Displays the first 10 lines of a file.
    
    ```bash
    $ head file.txt
    ```
    
4. **`tail`**
    
    Displays the last 10 lines of a file.
    
    ```bash
    $ tail file.txt
    ```

---

### Commands for Searching Files and Directories

1. **`find`**
    
    Searches for files and directories in the file system.
    
    ```bash
    $ find /destination/path -name "file.txt"
    ```
    
2. **`locate`**
    
    Searches for files in the system using a file database.
    
    ```bash
    $ locate file.txt
    ```

---

### Commands for Modifying Permissions and Ownership

1. **`chmod`** (Change Mode)
    
    Changes the permissions of a file or directory.
    
    ```bash
    $ chmod 755 file.txt
    ```
    
2. **`chown`** (Change Owner)
    
    Changes the owner and group of a file or directory.
    
    ```bash
    $ chown user:group file.txt
    ```
    
3. **`chgrp`** (Change Group)
    
    Changes the group of a file or directory.
    
    ```bash
    $ chgrp group file.txt
    ```

---

## Practical Exercises

### Exercise 1: Create a Directory and Files

1. Create a directory named `project`.
    
    ```bash
    $ mkdir project
    ```
    
2. Inside `project`, create three files: `file1.txt`, `file2.txt`, `file3.txt`.
    
    ```bash
    $ touch project/file1.txt project/file2.txt project/file3.txt
    ```
    
3. Add some text to each file using the `echo` command.
    
    ```bash
    $ echo "Sample text 1" > project/file1.txt
    $ echo "Sample text 2" > project/file2.txt
    $ echo "Sample text 3" > project/file3.txt
    ```
    
4. Verify the creation of the files inside `project`.
    
    ```bash
    $ ls -l project
    ```

---

### Exercise 2: Move and Rename Files

1. Move `file1.txt` to a subdirectory named `subdirectory`.
    
    ```bash
    $ mkdir project/subdirectory
    $ mv project/file1.txt project/subdirectory/
    ```
    
2. Rename `file2.txt` to `renamed_file.txt`.
    
    ```bash
    $ mv project/file2.txt project/renamed_file.txt
    ```
    
3. Verify that the files have been moved and renamed correctly.
    
    ```bash
    $ ls -l project/subdirectory
    $ ls -l project
    ```

---

### Exercise 3: Search for Files

1. Search for the file `renamed_file.txt` within your working directory.
    
    ```bash
    $ find project -name "renamed_file.txt"
    ```

---

### Exercise 4: Delete Files and Directories

1. Delete the file `file3.txt`.
    
    ```bash
    $ rm project/file3.txt
    ```
    
2. Delete the subdirectory `subdirectory` (it must be empty first).
    
    ```bash
    $ rmdir project/subdirectory
    ```
    
3. Verify the deletion.
    
    ```bash
    $ ls -l project
    ```
