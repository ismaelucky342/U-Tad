# Unit 3: TCP-IP: Transport Layer and Network Layer

### Functions of the Transport Layer

### Error Control

The 3 basic aspects to ensure reliable delivery are:

- Error detection and retransmission of erroneous segments.
- Sequence control to detect if information is lost or damaged.
- Duplicate control.

### Application Addressing – Ports

Ports are divided into **three ranges**:

- ***Well-Known Ports*** (0-1023): Used by specific applications and should only be used by them (80, 443, etc.). These are assigned by the ***IANA*** (*Internet Assigned Numbers Authority*).
- *Registered Ports* (1024-49151): Can be assigned to an application established by the *IANA*, but in practice, anyone can use them.
- *Ephemeral Ports* (49152-65535): Can be freely used as source ports. They are not assigned to specific applications.

### Segmentation and Multiplexing

Segmentation or **packetization** is the process where the (**sender**) **divides** the message **into packets**, adds the source and destination ports in the header, and transfers the message to the network layer.

On the **receiver** side, the transport layer receives data from the network layer, **reassembles the packets**, reads their headers, identifies the port number, and sends the information to the corresponding application.

**Multiplexing** optimizes the use of network resources by allowing simultaneous transmission of multiple data streams over one (**upstream**) or several (**downstream**) connections, improving efficiency and communication capacity.

### Flow and Congestion Control

The goal is to prevent information loss due to a fast sender and a slow receiver.

### Flow Control

The **sliding window method** is commonly used, meaning that **the receiver informs the sender of how much information it can process** so the sender adjusts the amount of information it sends.

### Congestion Control

Occurs when many devices on a network send data, and routers begin to overflow, causing packet loss.

- Open-Loop Congestion Control or passive solutions: Aim to prevent congestion.
- Closed-Loop Congestion Control or active solutions: Act when problems are detected.

### Checksum

Protocols detect errors in received packets through the checksum mechanism.

It is applied in UDP, TCP, and IP protocols.

### In summary:

The binary sum of the packet blocks is calculated, the one's complement (checksum) is obtained, and both the blocks and the checksum are sent over the network.

At the receiver, all blocks and the checksum are summed, and if:

- **The result is all 1’s → Transmission WITHOUT errors.**
- **The result contains any 0 → Transmission WITH errors.**

### Transport Protocols UDP/TCP

Connectivity in the transport layer can be classified as connection-oriented *(Connection-Oriented)*, implemented in **TCP**, or connectionless *(Connectionless)*, implemented in **UDP**.

### UDP Protocol

Used to **transmit datagrams quickly** in IP networks and functions as a simple, delay-free alternative to the TCP protocol. It is mainly used for **DNS queries** and **audio and video transmission.**

- Provides the minimum required functionality → Application addressing.
- **Less reliable** → Does not guarantee datagram delivery.
- **Stateless** → Each datagram is independent, and there is no initial connection.
- **Fast → Does not establish an initial connection.**
- **Low network overhead.**
- Used in → **Voice communications, DHCP, DNS, RIP…**

Datagrams are exchanged via request-response. The header includes data such as source and destination ports, datagram length, checksum, and the data.

### TCP Protocol

- Stateful → The sending and receiving applications share context about the communication.
- Uses streams → A set of all packets.
- More reliable.
- Used in → Text communications (WhatsApp), file transfers, web browsing, email…

### THREE PHASES:

As a connection-oriented protocol, it follows these three phases:

1. **Connection – Three-Way Handshake:** Sequence numbers are synchronized to later use them to recover, order, and resend packets. Flags → SYN, SYN+ACK, ACK.
2. **Data Transmission:** Data is sent. TCP manages packet loss and disorder. Each time a packet is sent, the recipient sends an ACK to confirm receipt.
3. **Disconnection – Teardown:** Flags → FIN, ACK, and FIN, ACK.

### Functions of the Network Layer

Provides services to enable end devices to exchange data across networks. **The main protocol is IP.**

### FUNCTIONS:

1. **Node Addressing:** Each node has a unique IP.
2. **Encapsulation:** IP header information is added, such as the source and destination hosts' IP addresses.
3. **Routing:** Routes packets through the network of routers.
4. **Decapsulation:** The destination node decapsulates the information.

**The IP protocol uses UDP, and there are two versions → IPv4 (32 bits) and IPv6 (128 bits).**

### IPv4 CIDR Addressing

### Subnet Mask

The **subnet mask** is an essential component of IP addressing that separates an address into two parts: **network** and **host**. Its length is **32 bits**, with the first bits set to 1 to identify the network and the remaining bits set to 0 for the hosts. It is represented as */M*, where M is the number of bits set to 1. For example, a **/24** mask uses the first **24 bits** for the network.

### CIDR in IPv4

The goal of CIDR is to use **variable-length masks** to create as many **subnets** as needed, assigning IPs efficiently.

### Available IPs:

Calculated as 2^BH, where BH is the number of host bits. Example → For /24, we would have 2^8 IPs (256), of which 2 are reserved for the network and broadcast (x.x.x.0 and x.x.x.255). It is common to assign the first to the router.

### Broadcast Address:

Used when information needs to be sent to all nodes on the network.

### Public and Private IPs

### STATIC and DYNAMIC IPs:

- Static: Permanently assigned. Used for servers.
- Dynamic: A different IP is assigned each time a node connects to the network (e.g., a laptop connecting to WiFi).

### PUBLIC and PRIVATE IPs:

- Private: Cannot travel over the internet. Example → All devices in a home connected to WiFi.
- Public: IPs assigned to nodes connecting to public networks like the Internet.

### Other Network Layer Protocols

### ICMP Protocol

Allows nodes to send informational messages such as errors or network diagnostics (**PING or** **traceroute**).

### Routing Protocols (RIP, OSPF, and BGP)

Routing protocols **enable routers to communicate**, exchanging routing tables and ensuring packets travel from one router to another until they reach their destination.

### Test Questions

### If packets arrive out of order in a communication, there are mechanisms in network software to reorder them.

→ True.

### If 32 bits are used to encode an IPv4 address, how many different IPs can we have?

→ 2^32=4,294,967,296

### In a communication, if a packet is lost, some transport protocols can recover it, but others do not have that capability.

→ True (TCP can, but UDP cannot).

### When a public IP is needed for a server, I have several options:

→ Use a service like AWS, where you can pay for public IPs for your servers.

→ Request it from an Internet Service Provider (ISP).

### Considering the TCP/IP software model created by the fathers of the Internet, Robert Kahn and Vinton Cerf, we can say:

→ They laid the foundations and the first versions of the current TCP/IP model that governs Internet communications.

### If when pinging a distant device, we receive an ICMP message with the description "TTL expired," what could be happening?

→ The TTL of the IP packets has expired because the maximum number of hops was exceeded, and the outgoing packet was discarded by a router on the Internet.

### When performing an nslookup on the URL www.u-tad.com, we get the IP 81.46.243.216. Since U-tad's web service is visible on the Internet, what can we say about the IP 81.46.243.216?

→ It is a public IP so it can be used on the Internet, allowing clients from anywhere in the world to access the university's website.

→ It is likely a static IP to avoid continuously updating domains in DNS.

### The UDP header has four main fields: source port, destination port, length, and checksum, each 16 bits. If the length field has the following value 0000.0000.0111.1111, how many bytes does the UDP Datagram have, including the header and data?

→ 111.1111 in binary = 127 bytes.