### Installation of Core Network Emulator

1. **Download Core Network Emulator**:
    - Go to the official page and download the file corresponding to your operating system: Core Network Emulator.
2. **Installation on Ubuntu**:
    - Open a terminal and follow these steps:
    
    ```bash
    sudo apt update
    sudo apt install core-network
    ```

1. **Start Core Network Emulator**:
    - After installation, you can start Core Network Emulator from the terminal with the following command:
    
    ```bash
    core-gui
    ```

### Network Configuration in Core Network Emulator

### Step 1: Intranet Configuration

1. **Create nodes for the Router and the APP-EMP Server**:
    - Open Core Network Emulator.
    - Add a network node (router) and a node for the server (APP-EMP).
    - Connect them with a network link.
2. **Configure the IP of the router's eth1 interface**:
    - Right-click on the router > `Configure`
    - Assign the IP `192.168.50.1/24` to the eth1 interface.
3. **Configure the IP of the APP-EMP server**:
    - Right-click on the APP-EMP server > `Configure`
    - Assign the IP `192.168.50.2/24` to the eth0 interface.
4. **Activate the FTP service on APP-EMP** (within the emulation):
    
    ```bash
    sudo apt update
    sudo apt install vsftpd
    sudo systemctl start vsftpd
    sudo systemctl enable vsftpd
    ```

### Step 2: DMZ Configuration

1. **Create nodes for the Router and the WEB-INTRA Server**:
    - Add a network node (router) and a node for the server (WEB-INTRA).
    - Connect them with a network link.
2. **Configure the IP of the router's eth2 interface**:
    - Right-click on the router > `Configure`
    - Assign the IP `192.168.100.1/24` to the eth2 interface.
3. **Configure the IP of the WEB-INTRA server**:
    - Right-click on the WEB-INTRA server > `Configure`
    - Assign the IP `192.168.100.2/24` to the eth0 interface.
4. **Activate the HTTP service on WEB-INTRA** (within the emulation):
    
    ```bash
    sudo apt update
    sudo apt install apache2
    sudo systemctl start apache2
    sudo systemctl enable apache2
    ```

### Step 3: Internet Configuration

1. **Create nodes for the Router, Hacker's Laptop, and WEB-UBUNTU Server**:
    - Add a network node (router), a node for the laptop (Hacker), and a node for the server (WEB-UBUNTU).
    - Connect them with network links.
2. **Configure the IP of the router's eth0 interface**:
    - Right-click on the router > `Configure`
    - Assign the IP `80.20.150.1/24` to the eth0 interface.
3. **Configure the IP of the Hacker's Laptop**:
    - Right-click on the Hacker's Laptop > `Configure`
    - Assign the IP `80.20.150.2/24` to the eth0 interface.
4. **Configure the IP of the WEB-UBUNTU server**:
    - Right-click on the WEB-UBUNTU server > `Configure`
    - Assign the IP `80.20.150.3/24` to the eth0 interface.
5. **Activate the HTTP service on WEB-UBUNTU** (within the emulation):
    
    ```bash
    sudo apt update
    sudo apt install apache2
    sudo systemctl start apache2
    sudo systemctl enable apache2
    ```

### Step 4: Screenshot of Network Configuration (CAPTURE 1)

1. **Capture the IP configuration**:
    Ensure all interfaces have the correct IPs assigned. Capture the network configuration in Core Network Emulator and take a screenshot.

### Step 5: Connectivity Test (CAPTURE 2)

1. **Test connectivity from Hacker to APP-EMP and WEB-INTRA**:
    
    ```bash
    ping 192.168.50.2  # From Hacker to APP-EMP
    ping 192.168.100.2  # From Hacker to WEB-INTRA
    ```

### Step 6: IPTABLES Rules Configuration

1. **Allow WEB traffic from the Internet to the DMZ**:
    
    ```bash
    sudo iptables -A FORWARD -i eth0 -o eth2 -p tcp --dport 80 -j ACCEPT
    sudo iptables -A FORWARD -i eth2 -o eth0 -p tcp --sport 80 -j ACCEPT
    ```

2. **Allow FTP traffic from the DMZ to the Intranet**:
    
    ```bash
    sudo iptables -A FORWARD -i eth2 -o eth1 -p tcp --dport 21 -j ACCEPT
    sudo iptables -A FORWARD -i eth1 -o eth2 -p tcp --sport 21 -j ACCEPT
    ```

3. **Block all other traffic**:
    
    ```bash
    sudo iptables -A FORWARD -j DROP
    ```

### Step 7: Display IPTABLES Rules (CAPTURE 3)

1. **Show the configured rules**:
    
    ```bash
    sudo iptables -t filter -L -v
    ```

### Step 8: Firewall Verification and Results (CAPTURE 4)

1. **Ping test from Hacker to APP-EMP (should fail)**:
    
    ```bash
    ping 192.168.50.2
    ```

2. **Nmap test from Hacker to WEB-INTRA (only TCP/80 port should be open)**:
    
    ```bash
    sudo apt install nmap
    nmap 192.168.100.2
    ```

3. **Nmap test from WEB-INTRA to APP-EMP (only FTP/21 port should be open)**:
    
    ```bash
    nmap 192.168.50.2
    ```

4. **Ping test from WEB-INTRA to APP-EMP (should fail)**:
    
    ```bash
    ping 192.168.50.2
    ```
