# Unit 1: Computer Networks and the Internet

### General Concepts

### Types of Networks

- **LAN:** Usually private networks that occupy a building.
- **MAN:** Network for a province or region.
- **WAN:** Networks that span a country or continent. The Internet is considered a WAN.

### *Hardware* Components of a Computer Network

Communication elements:

- **HUB:** Receives a packet and sends it to all its ports.
- **Switch:** Analyzes the packet and sends it only to its recipient(s). Analyzes traffic at the MAC level.
- **Router:** Interconnects LAN, MAN, and WAN networks. Analyzes the packet at the IP level and sends it to the appropriate recipient.

Transmission elements:

- **Copper cable**
- **Fiber optic cable**
- **Air**

### *Software* Components of a Computer Network

There are two layer models: OSI and TCP/IP.

### Internet Architecture

### Organizations Governing the Internet

IETF, IANA/ICANN, 3GPP.

### Layer Models: OSI and TCP/IP

### OSI

Theoretical model of 7 layers: Application, presentation, session, transport, network, link, physical.

### TCP/IP

- **Application Layer**: Protocols → HTTP (80), HTTPS (443), SSH (22), FTP (21 and 20), DNS (53), DHCP (67 and 68), SMTP…
- **Transport Layer**: Protocols → TCP and UDP.
- **Network Layer**: IP
- **Link Layer**: MAC
- **Physical Layer**: Electrical signal level, frequency, radio channel…

Communication is vertical: from the application layer (5) of computer one to the transport layer (4), and so on down to the physical layer (1). Then, through the network to the physical layer (1) of computer two, and back up to the application layer (5) of computer two.

### Test Questions

### If we PING Google's DNS 8.8.8.8, what packets will we see in Wireshark?

→ Ping request packets to the destination IP 8.8.8.8 and ping reply packets with source IP 8.8.8.8.

### What is the most commonly used protocol for file transfer on the Internet?

→ FTP.

### Of the three connectivity options available in VirtualBox, which one allows connection to the Internet?

→ NAT and Bridged Adapter.

### The IETF (Internet Engineering Task Force)

Publishes the so-called RFCs (Request for Comments).