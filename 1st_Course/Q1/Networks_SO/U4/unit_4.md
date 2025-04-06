# Networks and Operating Systems Laboratory | Unit 4

## IP Addressing for Windows

### Commands

1. **ipconfig**
    
    Displays the IP address assigned to the configured network.
    
2. **ipconfig /all**
    
    Provides detailed information, including the MAC address, DNS server addresses (primary and secondary), among others.
    

## IP Addressing for Linux

### Commands

1. **ifconfig**
    
    Displays the machine's IP address in Linux, with a typical address like `10.0.2.15` and the loopback address `127.0.0.1` (localhost).
    
2. **net-tools package**
    
    First, install the package with the following command:
    
    ```bash
    sudo apt install net-tools
    ```
    
3. **nmcli dev show | grep DNS**
    
    Displays information related to the DNS servers configured on the Linux machine.
    
4. **nmcli**
    
    Command to manage and administer network connections in Linux using Network Manager.
    

### Linux Commands for Network Management

1. **ip addr (ip a)**
    
    Displays information about available network interfaces, including IP and MAC addresses.
    
2. **ip -s l**
    
    Shows transmission and reception statistics for IP interfaces.
    
3. **ping URL/IP**
    
    Tests connectivity with another node using ICMP, measuring round-trip time.
    
4. **traceroute**
    
    Displays the route packets take to reach their destination.
    
5. **route**
    
    Displays the routing table and allows modifications.
    
6. **route -n**
    
    Displays the routing table in numeric format.
    
7. **route -e**
    
    Presents another view of the routing table.
    
8. **route add/del**
    
    Allows adding or deleting routes in the routing table.
    
9. **nslookup**
    
    Tool for troubleshooting DNS servers.
    
10. **hostname**
    
    Displays or sets the host name.
    
11. **arp**
    
    Resolves IP addresses to MAC addresses and displays the ARP cache.
    
12. **ifconfig**
    
    Configures network interfaces and displays information about them.
    
13. **ip**
    
    Modern alternative to `ifconfig` for managing IP addresses and the routing table.
    
14. **iwconfig**
    
    Configures wireless network interfaces, showing details like channel and SSID.
    
15. **nmap**
    
    Tool for scanning ports and performing network security audits.
    
16. **iperf**
    
    Measures network performance between two hosts.
    
17. **tcpdump**
    
    Captures and displays network packets, allowing filtering by protocol, port, IP, etc.
    

## Windows Commands for Network Management

1. **ping**
    
    Command to verify connectivity between the local host and a destination on the network.
    
2. **ipconfig**
    
    Displays the system's network configuration, including IP address, subnet mask, and gateway.
    
3. **hostname**
    
    Displays the machine's host name.
    
4. **getmac**
    
    Displays the MAC address of the network interface.
    
5. **arp**
    
    Displays and manipulates the ARP table.
    
6. **nslookup**
    
    Tool to query DNS servers.
    
7. **nbtstat**
    
    Displays NetBIOS over TCP/IP statistics and connections.
    
8. **netstat**
    
    Displays network connections and traffic statistics.
    
9. **tracert**
    
    Similar to `traceroute`, shows the route packets take to the destination.
    
10. **route**
    
    Displays or modifies routing tables.
    
11. **netsh**
    
    Command to configure and display network information.
    

## Practical Exercises

### Example 1: Router IP Addressing

The router has a public IP address `81.39.97.73` and a private address `192.168.1.1/24`.

The subnet mask `255.255.255.0` indicates that the first 24 bits are the network address. The address range for nodes in the private subnet is `192.168.1.0` to `192.168.1.255`, though `0` and `255` are reserved, leaving 254 addresses available for nodes.

### Example 2: Subnet 192.168.1.1/23

1. **Part of the address identifying the subnet**
    
    The first 23 bits identify the subnet.
    
2. **Part of the address identifying each node**
    
    The last 9 bits are for the node address.
    
3. **IP address range**
    
    The range is from `192.168.0.0` to `192.168.1.255`.
    
4. **Maximum number of nodes**
    
    This subnet can accommodate up to 512 nodes.
    

### Example 3: Subnetting the Network 200.3.25.0 into 8 Subnets

The subnet mask is `255.255.255.224`.

The subnets resulting from `200.3.25.0/27` are:

- Subnet 1: 200.3.25.0/27
    
    Network address: `200.3.25.0`
    
    Broadcast address: `200.3.25.31`
    
    Start address for nodes: `200.3.25.1`
    
    End address for nodes: `200.3.25.30`
    
- Subnet 2: 200.3.25.32/27
    
    Network address: `200.3.25.32`
    
    Broadcast address: `200.3.25.63`
    
    Start address for nodes: `200.3.25.33`
    
    End address for nodes: `200.3.25.62`
    

... and so on for the remaining subnets.
