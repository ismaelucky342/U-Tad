# Networks and Operating Systems Laboratory | Unit 3

## User and Group Management. Permissions

### Key Concepts

1. **Users in Linux**
    - Users are accounts created to interact with the operating system.
    - Each user has a unique identifier called `UID` (User Identifier).
    - A user's home directory is commonly `/home/username`.
    - The `/etc/passwd` file contains user information.
2. **Groups in Linux**
    - Groups allow for more efficient management of permissions and access rights for multiple users.
    - Each group has a unique identifier called `GID` (Group Identifier).
    - The `/etc/group` file contains group information.
3. **Permissions in Linux**
    - Permissions are how the operating system manages access to files and directories.
    - Three types of permissions are assigned: **read (r)**, **write (w)**, and **execute (x)**.
    - Permissions are assigned to three types of users: **owner**, **group**, and **others**.

### Basic Commands for Managing Users and Groups

#### Commands for Users

1. **adduser [username]**
    Creates a new user in the system.
    ```bash
    sudo adduser john
    ```

2. **usermod [options] [username]**
    Modifies user attributes, such as name, group, etc.
    ```bash
    sudo usermod -aG sudo john
    ```

3. **deluser [username]**
    Deletes a user from the system.
    ```bash
    sudo deluser john
    ```

4. **id [username]**
    Displays the UID and GID of a user.
    ```bash
    id john
    ```

5. **passwd [username]**
    Changes a user's password.
    ```bash
    sudo passwd john
    ```

#### Commands for Groups

1. **groupadd [group]**
    Creates a new group in the system.
    ```bash
    sudo groupadd admins
    ```

2. **groupdel [group]**
    Deletes a group from the system.
    ```bash
    sudo groupdel admins
    ```

3. **usermod -aG [group] [username]**
    Adds a user to a group.
    ```bash
    sudo usermod -aG admins john
    ```

4. **groups [username]**
    Displays the groups a user belongs to.
    ```bash
    groups john
    ```

#### Commands for File Permissions

1. **ls -l [file]**
    Displays the permissions of a file or directory.
    ```bash
    ls -l file.txt
    ```

2. **chmod [permissions] [file]**
    Changes the permissions of a file or directory.
    - Example: To give read, write, and execute permissions to the owner, and read-only permissions to the group and others:
        ```bash
        chmod 755 file.txt
        ```
    - Example: To remove write permissions:
        ```bash
        chmod -w file.txt
        ```

3. **chown [user]:[group] [file]**
    Changes the owner and group of a file.
    ```bash
    sudo chown john:admins file.txt
    ```

4. **chgrp [group] [file]**
    Changes the group of a file.
    ```bash
    sudo chgrp admins file.txt
    ```

### Example of Managing Permissions

Imagine we have a file called `document.txt` and want to manage its permissions.

1. **View current permissions**:
    ```bash
    ls -l document.txt
    ```
    Possible output:
    ```
    -rwxr-xr-- 1 john admins 12345 Mar 20 10:00 document.txt
    ```
    In this case, the owner `john` has read, write, and execute permissions (rwx), the group `admins` has read and execute permissions (r-x), and others have read-only permissions (r--).

2. **Change permissions**:
    Suppose we want only the owner to have full access, and the group and others to have no access.
    ```bash
    chmod 700 document.txt
    ```

3. **Change owner and group**:
    If we want `mary` to be the owner of the file and the group to be `developers`:
    ```bash
    sudo chown mary:developers document.txt
    ```

4. **Delete the file**:
    To delete the file `document.txt`, ensuring only the owner can do so:
    ```bash
    rm document.txt
    ```

### Example of Group Usage

1. **Create a group called `developers`**:
    ```bash
    sudo groupadd developers
    ```

2. **Add the user `john` to the group `developers`**:
    ```bash
    sudo usermod -aG developers john
    ```

3. **Verify the groups `john` belongs to**:
    ```bash
    groups john
    ```

4. **Verify the users in the group `developers`**:
    ```bash
    grep developers /etc/group
    ```

### Additional Content: File Permission Numeric Representation

Permissions can also be represented numerically:
- **4**: Read (r)
- **2**: Write (w)
- **1**: Execute (x)

The numeric value is the sum of these permissions. For example:
- `7` (4+2+1): Read, write, and execute.
- `5` (4+1): Read and execute.
- `0`: No permissions.

Example:
```bash
chmod 750 file.txt
```
This gives the owner full permissions (7), the group read and execute permissions (5), and others no permissions (0).
