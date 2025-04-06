# Unit 1: Introduction - Basic Concepts of Operating Systems. Installation

## Introduction to Operating Systems

An **Operating System (OS)** is a set of programs that manage a computer's hardware and provide services for running programs. It acts as an intermediary layer between the hardware and the user, facilitating interaction between the two.

### Main Functions of an OS

1. **Process Management**
    - The OS manages program execution, creates and terminates processes, and handles resource allocation.
2. **Memory Management**
    - Allocates and frees memory for running programs, ensuring no conflicts occur between them.
3. **File Management**
    - Enables storing, organizing, and accessing files on storage devices (hard drives, SSDs, etc.).
4. **Device Management**
    - Controls and coordinates the use of hardware devices, such as printers, keyboards, screens, and more.
5. **Security and Access**
    - Controls access to system resources, protecting information from unauthorized access.

---

## Types of Operating Systems

### 1. **General-Purpose Operating Systems**

- **Windows**: Used on PCs, easy to use, with a user-friendly graphical interface.
- **Linux**: Open-source operating system, mainly used on servers and embedded systems.
- **macOS**: Apple's operating system for its computers.
- **Unix**: Multi-tasking and multi-user system, primarily used on servers and mainframes.

### 2. **Real-Time Operating Systems (RTOS)**

- Designed to respond to events within a specific time frame, used in embedded systems and critical devices like vehicles, medical systems, etc.

### 3. **Mobile Operating Systems**

- **Android**: Based on Linux, used on mobile devices and tablets.
- **iOS**: The operating system for Apple's mobile devices, such as the iPhone and iPad.

---

## Installing an Operating System

Installing an operating system involves configuring the software to work correctly with the hardware. Depending on the OS, the process may vary but generally includes:

1. **Preparing the Installation Device**
    - This can be a USB or DVD containing the OS installer.
2. **Configuring the BIOS/UEFI**
    - The system boot must be configured to start from the installation device.
3. **Disk Partitioning**
    - The hard drive must be partitioned for the OS to install correctly and manage memory.
4. **Operating System Installation**
    - Follow the installer steps, selecting the language, installation type (custom or automatic), and initial settings like time zone and username.

---

## Basic Commands for Installation on Windows

1. **setup.exe**
    - Command to start the OS installation from a USB or DVD.
2. **diskpart**
    - Tool for disk management in Windows, allowing disk partitioning and storage unit management.
3. **sfc /scannow**
    - Command to repair damaged system files.

---

## Basic Commands for Installation on Linux

1. **dd if=path/to/iso of=/dev/sdX**
    - Copies the OS ISO image to a USB device to create an installation medium in Linux.
2. **fdisk /dev/sda**
    - Tool for creating and managing partitions on hard drives.
3. **sudo apt-get install <package>**
    - Installs software and updates on Debian-based distributions like Ubuntu.
4. **grub-install /dev/sda**
    - Installs the GRUB bootloader on the disk so the system can boot.

---

## Examples of Operating System Installation

### Example 1: Installing Windows

1. Insert the installation USB or DVD into the computer.
2. Restart the computer and access the BIOS/UEFI to select the boot device.
3. Follow the installer instructions to select the language, partition, and network configuration.
4. Once the installation is complete, restart the system and access Windows.

### Example 2: Installing Linux (Ubuntu)

1. Create an installation medium with the Ubuntu ISO image using the `dd` command in Linux.
2. Restart the computer and boot from the USB device.
3. Select "Install Ubuntu" from the startup menu.
4. Follow the instructions to configure partitions and installation.
5. After completing the installation, restart the system and boot into Ubuntu.

---

## Practical Exercises

### Exercise 1: Network Configuration in Windows

1. Open the **Command Prompt** and use the `ipconfig` command to get your machine's IP address.
2. Run `ipconfig /all` to view detailed information about network connections.

### Exercise 2: Network Configuration in Linux

1. Run `ifconfig` or `ip a` to view your machine's IP address.
2. Install the **net-tools** package with the command:
    
    ```bash
    sudo apt install net-tools
    ```
    
3. Use `nmcli dev show | grep DNS` to check the configured DNS servers.
