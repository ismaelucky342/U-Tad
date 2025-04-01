# Unit 4: Data Link Layer and Wired LANs

### Functions of the Data Link Layer

It is responsible for providing services to the network layer and managing the sending and receiving of frames (*encapsulated messages*) with the physical layer.

### FUNCTIONS:

1. **Frame Construction:** Encapsulation of network layer messages.
2. **Logical Link Control (LLC).**
3. **Medium Access Control (MAC).**
4. **Addressing:** Each node is identified by its MAC address.
5. **Error Detection and Correction.**

### Implementation of the Data Link Layer

The data link layer and the physical layer are responsible for the speed and latency of communication.

Some protocols used are:

- LAN Networks: Ethernet (IEEE 802.3), WiFi (IEEE 802.11)
- WAN Networks: PPP, HDLC, SDLC, ATM.

### MAC Addresses

It is a **12-digit hexadecimal number** (**48 bits**) embedded in the **network card** (recorded during its manufacturing). It is also called a **physical address**.

Example → 00:1A:2B:3C:4D:5E

### MAC Format and Types:

Format:

- The first 6 digits identify the manufacturer (OUI).
- The other 6 digits represent the network interface controller (NIC).

There are 3 types:

- **Unicast:** If a frame has a unicast destination MAC address, it is sent only to the node with that MAC on its NIC.
- **Multicast:** The multicast address allows the source to send a frame to a group of devices.
- **Broadcast:** Frames with destination address **FF.FF.FF.FF.FF.FF** are called broadcast addresses and will reach all devices in that LAN segment.

### ARP Protocol

The Address Resolution Protocol (ARP) **is a protocol that maps an IP address to a MAC address** in a **LAN**.

We know the source IP and MAC, the destination IP, and we need this protocol to find the destination MAC. The procedure is as follows:

1. The sender node sends an **ARP request** (containing the destination IP) at the **broadcast** level.
2. All nodes in the LAN receive the request, but only the device with that IP responds by returning its MAC (**ARP reply**).
3. The **sender** **receives** the **response** and **stores the MAC in cache**.

Example:

- On the way out, the broadcast frame has MAC source=49:BD:D2:C7:56:2A, MAC destination=FF:FF:FF:FF:FF:FF, and message *ARP Request* with IP=141.23.56.23.
- On the way back, the *unicast* frame has MAC source=A4:6E:F4:59:83:AB, MAC destination=49:BD:D2:C7:56:2A, and message *ARP Reply* with MAC=A4:6E:F4:59:83:AB.

### Error Detection and Correction

For error detection, we continue using **checksum** and also the **cyclic redundancy check (CRC)** algorithm.

Additionally, the data link layer includes error correction codes such as:

- Hamming Codes.
- Binary Convolutional Codes.
- Reed-Solomon Codes.
- Low-Density Parity-Check Codes.

### Cyclic Redundancy Check (CRC)

It is a more complex code than checksum as it is performed at the hardware level, allowing for more complex operations.

It is based on binary XOR divisions:

1. The sender **divides** the frame by a special value called the **generator polynomial**.
2. The **remainder** of the division is the **CRC**. It is added to the data and sent.
3. The **receiver performs the same division**.
    - If the remainder is **zero**, the data arrived **without errors**.
    - If the remainder is **non-zero**, the data arrived **with errors**.

### Wired LANs - Ethernet IEEE 802.3 Standard

It is a very fast technology that initially provided 3MB but today reaches up to 10GB.

The main **hardware components** of Ethernet are:

- Hub, Switch, Copper Cables, Fiber Optic Cables.

### Ethernet Medium Access Control CSMA/CD

In this algorithm, network devices listen to the medium before transmitting to determine if resources are available.

### DHCP Service

This protocol allows a host to obtain an **IP address** **automatically** (the **IP address, subnet mask, DNS servers**, and **default gateway**).

The **port** used by the **server** is **67**, and the **client** uses **68**, both **UDP**.

### DORA Process

This is the process carried out between the client and server to use DHCP:

1. **Discover:** The client generates this first message to check if there is a DHCP server on the network.
2. **Offer:** The DHCP server responds to the client with an offer message containing an IP for the client to use.
3. **Request:** The client receives the IP and sends a DHCP Request message confirming acceptance of that IP.
4. **Acknowledge:** The server sends an Acknowledge message with the IP, subnet mask, gateway, and DNS to the client.

### isc-dhcp-server Package in Linux

To configure a DHCP server, you can use the Linux package ***isc-dhcp-server***.

Example of DHCP server configuration in Ubuntu:

In Wireshark, using the DHCP filter, we can observe the steps of the DORA process.

### NAT Service

NAT is the Internet mechanism that translates private IP addresses into public ones needed to access the internet.

The router connecting the local network to the Internet performs this translation by changing the **private source IP to its own public IP**. When the packet returns, the router changes the **public destination IP to the private IP of the original device**, enabling proper communication.

NAT helps save public IP addresses and facilitates security and connectivity.

### Test Questions

### When in an Ethernet network, a node with MAC=00:0a:83:b1:c0:ff wants to send a broadcast message to all nodes connected to that LAN, it will construct a message with the following characteristics:

→ MAC source=00:0a:83:b1:c0:ff – MAC destination=ff:ff:ff:ff:ff:ff (broadcast)

### What type of network technology uses cables for data transmission?

→ Local Area Network (LAN): Ethernet

→ WAN Network: Fiber Optic.

→ Personal Area Network (PAN): Bluetooth

→ Metropolitan Area Network (MAN): Token Ring

### If the Ethernet card manufacturer CISCO is assigned the OUI=cc:46:d6 and has no additional OUIs, how many different cards can it manufacture?

→ 2^24 (like any manufacturer with a single OUI)

### If a router connecting a private intranet (with private IPs) to the Internet has an intranet interface with IP=192.168.15.1 and MAC=00:1b:44:11:3a:b7, and an Internet interface with IP=81.46.243.1 and MAC=00:fb:4a:48:3a:bb, and that router performs NAT functions. If a device in the intranet with IP=192.168.15.20 and MAC=00:fa:5c:27:aa:b7 sends a ping to Google's DNS IP=8.8.8.8, what is the source IP and source MAC of the packets going to the Internet on the router's Internet interface?

→ Source IP=81.46.243.1 – Source MAC=00:fb:4a:48:3a:bb (public interface)

### If I want my DHCP server to offer clients the DNS servers 80.58.61.250 and 80.58.61.254 and the IP range to offer is 192.168.17.5 to 192.168.17.10, in the configuration file or /etc/dhcp/dhcpd.conf, I must write the following primitives:

→ range 192.168.17.5 192.168.17.10; option domain-name-servers 80.58.61.250, 80.58.61.254;

### The CSMA/CD algorithm that allows efficient access to the shared medium (cable), when a collision occurs:

→ The nodes that collided are made to wait for a random time before they can retransmit, reducing the statistical probability of another collision.