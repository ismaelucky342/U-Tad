# Networks and Operating Systems Laboratory | Unit 5

## Process and memory management. Linux commands## **Process Management in Linux**

### **Commands**

1. **ps**
    
    Displays information about the currently running processes. The most commonly used options are:
    
    - `ps aux`: Shows a list of all running processes.
    - `ps -ef`: Similar to `ps aux`, but in a different format.
2. **top**
    
    Provides a dynamic, real-time view of the system's processes. Displays CPU usage, memory usage, process IDs, and more.
    
3. **htop**
    
    A more advanced, interactive version of `top`, with a user-friendly interface and additional features like process search, filtering, and tree views. It may need to be installed:
    
    ```bash
    bash
    CopyEdit
    sudo apt install htop
    
    ```
    
4. **kill**
    
    Sends a signal to a process, typically to terminate it. For example:
    
    ```bash
    bash
    CopyEdit
    kill 1234  # Terminate the process with PID 1234
    
    ```
    
    To forcefully terminate a process, use the `-9` signal:
    
    ```bash
    bash
    CopyEdit
    kill -9 1234
    
    ```
    
5. **killall**
    
    Terminates all processes with a given name. For example:
    
    ```bash
    bash
    CopyEdit
    killall firefox  # Terminates all Firefox processes
    
    ```
    
6. **bg**
    
    Resumes a suspended process in the background. It can be used after stopping a process with `Ctrl+Z`.
    
7. **fg**
    
    Brings a background process to the foreground.
    
8. **nice**
    
    Starts a process with a specified priority (niceness value). A higher niceness value means a lower priority:
    
    ```bash
    bash
    CopyEdit
    nice -n 10 command  # Starts a command with lower priority
    
    ```
    
9. **renice**
    
    Changes the priority of an already running process:
    
    ```bash
    bash
    CopyEdit
    renice 10 -p 1234  # Changes the priority of process with PID 1234 to 10
    
    ```
    
10. **jobs**
    
    Displays the status of background jobs (processes that were suspended or run in the background).
    
11. **wait**
    
    Pauses the execution of a script until a background process finishes.
    
12. **nohup**
    
    Runs a command that will not be terminated when the user logs out. It’s useful for long-running processes:
    
    ```bash
    bash
    CopyEdit
    nohup command &  # Runs command in the background, ignoring hangup signals
    
    ```
    

---

## **Memory Management in Linux**

### **Commands**

1. **free**
    
    Displays memory usage statistics, including used, free, and cached memory:
    
    ```bash
    bash
    CopyEdit
    free -h  # Shows memory usage in human-readable format
    
    ```
    
2. **vmstat**
    
    Provides a snapshot of the system's memory, processes, paging, and block IO. It is useful for diagnosing memory bottlenecks:
    
    ```bash
    bash
    CopyEdit
    vmstat 1  # Displays memory statistics every second
    
    ```
    
3. **top (Memory)**
    
    In addition to processes, `top` also provides memory statistics. To view memory details specifically, press `M` to sort processes by memory usage.
    
4. **htop (Memory)**
    
    `htop` provides detailed memory usage in a more readable and interactive format, including memory usage for each process.
    
5. **pmap**
    
    Displays memory maps for a process, showing how memory is allocated:
    
    ```bash
    bash
    CopyEdit
    pmap 1234  # Shows memory map for the process with PID 1234
    
    ```
    
6. **cat /proc/meminfo**
    
    Displays detailed information about the system’s memory, including total, free, and available memory, among other statistics:
    
    ```bash
    bash
    CopyEdit
    cat /proc/meminfo
    
    ```
    
7. **cat /proc/[pid]/status**
    
    Displays memory and process-specific statistics for a given process by PID:
    
    ```bash
    bash
    CopyEdit
    cat /proc/1234/status  # Displays memory stats for process with PID 1234
    
    ```
    
8. **swap**
    
    Displays or manages swap space. To check swap usage:
    
    ```bash
    bash
    CopyEdit
    swapon --show  # Displays active swap devices and their usage
    
    ```
    
9. **sysctl vm.swappiness**
    
    Adjusts the kernel parameter that determines how aggressively Linux swaps out processes. A value of 60 is default, and 0 means no swapping unless absolutely necessary:
    
    ```bash
    bash
    CopyEdit
    sysctl vm.swappiness=30  # Reduces the swapping aggressiveness
    
    ```
    
10. **mmap**
    
    A system call for mapping files or devices into memory. Useful for efficient memory management and inter-process communication.
    

---

## **Linux Commands for Process and Memory Diagnostics**

1. **lsof**
    
    Lists open files and the processes that opened them. It's useful for diagnosing issues related to file usage:
    
    ```bash
    bash
    CopyEdit
    lsof  # Lists all open files
    
    ```
    
2. **strace**
    
    Traces system calls and signals, showing how processes interact with the system:
    
    ```bash
    bash
    CopyEdit
    strace -p 1234  # Traces the system calls made by process with PID 1234
    
    ```
    
3. **dmesg**
    
    Displays kernel messages, including information about the system's memory usage and hardware, such as memory errors:
    
    ```bash
    bash
    CopyEdit
    dmesg | grep -i memory  # Filters dmesg output for memory-related entries
    
    ```
    
4. **sar**
    
    Provides historical data on system performance, including memory usage and process activity:
    
    ```bash
    bash
    CopyEdit
    sar -r 1 5  # Reports memory usage every 1 second for 5 intervals
    
    ```
    

---

## **Practical Exercises**

### **Example 1: Check the Memory Usage**

1. Open the terminal and run the following commands:
    
    ```bash
    bash
    CopyEdit
    free -h  # Displays memory usage in a human-readable format
    vmstat 1  # Displays memory statistics every second
    
    ```
    
2. Identify the total, used, and free memory on your system.

### **Example 2: Monitor Processes Using Top**

1. Run the `top` command:
    
    ```bash
    bash
    CopyEdit
    top  # Displays system processes and their resource usage
    
    ```
    
2. Press `M` to sort processes by memory usage, and note which processes are using the most memory.

### **Example 3: Terminate a Process**

1. Find the process ID (PID) of a running process:
    
    ```bash
    bash
    CopyEdit
    ps aux | grep firefox  # Find the PID of Firefox
    
    ```
    
2. Terminate the process by running:
    
    ```bash
    bash
    CopyEdit
    kill 1234  # Replace 1234 with the actual PID
    
    ```
    
3. Use `kill -9` if the process doesn't terminate with the regular `kill` command.

### **Example 4: Managing Swap Space**

1. Check the current swap usage:
    
    ```bash
    bash
    CopyEdit
    swapon --show
    
    ```
    
2. Disable swap space:
    
    ```bash
    bash
    CopyEdit
    sudo swapoff -a  # Disables all swap devices
    
    ```
    
3. Enable swap space again:
    
    ```bash
    bash
    CopyEdit
    sudo swapon -a  # Enables all swap devices
    
    ```
    

### **Example 5: Adjusting Swappiness**

1. View the current swappiness value:
    
    ```bash
    bash
    CopyEdit
    sysctl vm.swappiness
    
    ```
    
2. Set the swappiness to a lower value (less aggressive swapping):
    
    ```bash
    bash
    CopyEdit
    sudo sysctl vm.swappiness=30
    
    ```