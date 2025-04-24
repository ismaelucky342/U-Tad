# Unit 6: Network Security

## **Network Security Concepts**

### **Introduction**

Computer networks are essential for communication and data exchange. However, these networks are exposed to numerous security risks, making it necessary to implement protection mechanisms to ensure the integrity and confidentiality of information.

### **Concept of Information Security**

Information security refers to a set of practices and technologies designed to protect information from unauthorized access, modification, or destruction. Its goal is to ensure **confidentiality** (prevent unauthorized access to data), **integrity** (prevent unauthorized modifications), and **availability** (ensure information is accessible when needed).

### **Security Attacks**

There are different types of attacks that can compromise a network, including:

- **Denial of Service (DoS/DDoS) attacks**: overload a server with fake requests to render it inoperative.
- **Phishing**: tricking users into revealing confidential information.
- **SQL Injection**: manipulating database queries to obtain sensitive information.
- **Packet sniffing**: intercepting data in transit on the network.

### **Security Services**

To mitigate the aforementioned attacks, security services are implemented, such as:

- **Authentication**: verifying user identity through passwords, digital certificates, or biometrics.
- **Data integrity**: ensuring information has not been altered.
- **Encryption**: protecting information confidentiality using cryptographic algorithms.
- **Access control**: restricting access to sensitive resources based on established privileges.

---

## **Symmetric and Asymmetric Encryption**

### **Introduction**

Encryption is a fundamental technique for protecting information in networks. It involves transforming data into an unreadable format without the appropriate key to decrypt it.

### **Types of Encryption**

There are two main encryption approaches:

- **Symmetric encryption**: uses the same key for encrypting and decrypting data.
- **Asymmetric encryption**: uses a pair of keys, one public and one private.

### **Symmetric Encryption**

This type of encryption is fast and efficient but presents challenges in key management. Examples of symmetric algorithms include:

- **AES (Advanced Encryption Standard)**
- **DES (Data Encryption Standard)**

### **Asymmetric Encryption**

Uses two keys: a public key (which can be shared) and a private key (which must remain secret). It is used in applications such as email encryption and digital authentication. Examples of algorithms:

- **RSA (Rivest-Shamir-Adleman)**
- **ECC (Elliptic Curve Cryptography)**

### **Comparison: Symmetric vs. Asymmetric Encryption**

- **Symmetric encryption** is faster and more efficient but less secure in key distribution.
- **Asymmetric encryption** is more secure in key distribution but slower and more resource-intensive.

---

## **Security Mechanisms in TCP/IP Networks and the Internet**

### **Introduction**

The TCP/IP communication model is the foundation of the Internet and many local networks, making its security a crucial aspect.

### **Security in TCP/IP Client/Server Applications**

Client-server applications rely on protocols like HTTP, FTP, and SSH, which must implement security measures such as authentication and data encryption.

### **TLS Protocols**

Transport Layer Security (TLS) is a protocol that encrypts Internet communications to protect sensitive data, replacing the obsolete SSL.

### **IPSec**

IPSec is a set of protocols designed to encrypt and authenticate IP packets, ensuring secure communications in public and private networks.

---

## **Port Scanning**

### **Introduction**

Port scanning is a technique used to identify open services on a system and detect vulnerabilities.

### **TCP Port Scanning**

Involves sending SYN packets to determine if a port is open, closed, or filtered.

### **UDP Port Scanning**

More challenging than TCP scanning due to the lack of confirmation in UDP packets.

### **Legality of Port Scanning**

Port scanning can be illegal if performed without the network owner's authorization, as it may be interpreted as an intrusion attempt.

---

## **Firewalls and IPTABLES**

### **Introduction**

A firewall is a system that controls network traffic based on security rules to block unauthorized access.

### **Types of Firewalls**

- **Packet filtering firewalls**: inspect individual packets.
- **Stateful inspection firewalls**: verify the context of the connection.
- **Application firewalls**: protect specific applications like HTTP or FTP.

### **IPTABLES Functionality**

iptables is a firewall tool in Linux that allows defining rules to accept, reject, or block traffic.

---

## **Security Architectures: DMZ, Intranet, and Internet**

### **Elements of a Corporate Network**

Describes the basic components of a corporate network, such as servers, workstations, and routers.

### **Security Architectures**

- **DMZ (Demilitarized Zone)**: a network segment that exposes services to the Internet while keeping the internal network secure.
- **Intranet**: a private network with restricted access for employees.
- **Internet**: a public network with global access.

---

## **IPv4 Issues and Evolution to IPv6**

### **IPv4 Protocol**

Explains the exhaustion of IPv4 addresses and the need for a scalable solution.

### **IPv6 Protocol**

IPv6 offers a much larger address space and improvements in security and routing efficiency.

### **IPv4 vs. IPv6 Header Comparison**

IPv6 has a simplified header, improving packet transmission performance.

---

## **IPv6 Configuration on Network Nodes**

### **IPv6 Configuration with Core Network Emulator**

Using emulators to simulate IPv6 networks and test configurations before deployment.

### **IPv6 Configuration on Ubuntu Virtual Machines**

Practical process for assigning IPv6 addresses and configuring connectivity in Linux.