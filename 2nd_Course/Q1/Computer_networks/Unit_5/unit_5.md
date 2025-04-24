# Unit 5: Wireless Networks: WiFi and Cellular Mobile Networks (4G and 5G)

### Access Network Technologies

To browse the Internet, an Internet Service Provider (*ISP*) must enable access. This access can be either fixed or mobile.

- **Fixed Access Networks**:

ADSL (**copper**), FTTH (**Fiber Optics**), or Wireless Access like **Wi-Fi**.

The ISP connects a copper or fiber optic line to the desired location and installs a router, from which we build our LAN.

- **Mobile Access Networks**:
1G, 2G, **3G, 4G, or 5G**. No router is needed, just a **SIM** card.

### Wireless Networks

Signals are transmitted through the air.

### Undesired Effects in Wireless Channels

- **Fading**: The signal loses strength when passing through materials or dispersing.
- **Noise**: Devices using similar frequencies or environmental noise sources (like microwaves) generate interference that affects signal quality.
- **Multipath Propagation**: The signal bounces off objects and reaches the receiver through different paths, causing distortion as multiple versions of the same signal arrive at different times.

### Solutions to Undesired Effects

For WiFi networks:

- DFS: Avoids repeated channels.
- Power Management: Saves energy and prevents interference.
- Rate Adaptation: Maintains a stable connection by adapting the speed.

For mobile networks:

- **CSMA**: A system that allows multiple transmitters to use the same communication channel and frequency band simultaneously without interference.
- MIMO: Utilizes multiple transmission and reception antennas to take advantage of multipath propagation.

### WiFi Networks IEEE 802.11

There are several 802.11 standards for WLAN.

The two main frequency bands are 2.4 GHz and 5 GHz. Both are **free to use and unlicensed**.

Additionally, all these standards share several common features:

- All are backward compatible.
- Use CSMA/CA.
- Same frame structure.
- All can reduce transmission speed to cover greater distances.

### WLAN IEEE 802.11 Architecture

**AP or Wireless Access Point:**

The **physical device** that enables wireless communication between wireless devices and a wired network.

**BSS or Basic Service Set:**

The WiFi coverage area. It includes the AP and several wireless devices.

**BSSID or Basic Service Set Identifier:**
The MAC address of the AP (6 bytes).

**SSID or Service Set Identifier**

The name of the WiFi network.

### Connection to WLAN IEEE 802.11

The process for a wireless node to connect to a WiFi network is as follows:

1. **Scanning:**
    - **Passive Scanning**: APs send *Beacon* frames to announce themselves, allowing wireless devices to discover them.
    - **Active Scanning**: Devices actively send *Probe Request* frames to discover available networks. Active APs respond with *Probe Response* frames.
2. **Authentication:** Authentication Request and Authentication Response are performed using WPA or WPA2 protocols.
3. **Association:** The host joins the AP. Association Request and Association Response.
4. **Data Transfer.**

### IEEE 802.11 Frame Header

Unlike the Ethernet header, which includes only 2 MAC addresses, this one includes 4:

1. **Destination Address (DA):** MAC address of the **destination node**.
2. **Source Address (SA):** MAC address of the **source node**.
3. **Receiver Address (RA):** MAC address of the AP (**BSSID**).
4. **Transmitter Address (TA):** MAC address of the **source node**.

### Medium Access Control

These networks use an acknowledgment/retransmission scheme (ARQ) to ensure error-free frame delivery.

### ARQ Protocol

1. If the channel is free, the station transmits after a short delay (DIFS).
2. If the channel is busy, the station selects a random time and waits, pausing the countdown if the channel remains busy.
3. When the countdown reaches zero and the channel is free, the station sends the frame and waits for acknowledgment.
4. The receiver, after a short delay (SIFS), sends the acknowledgment.
5. If the station receives the acknowledgment, it knows the frame was successfully received.

### CSMA/CA Protocol

Prevents collisions in a wireless network.

Imagine we have 3 nodes and an AP:

1. N1 wants to send data, so it sends an **RTS (Request to Send)** frame to notify all stations, including the AP.
2. The AP responds with a **CTS (Clear to Send)** frame to authorize the transmission and notify other stations (like N2 and N3) to wait to avoid collisions.
3. N2 and N3 listen to the CTS and refrain from transmitting during the indicated time.
4. N1 sends the **DATA** frame.
5. The AP confirms successful reception by sending an **ACK** frame.

### Cellular Mobile Networks: 4G and 5G

These networks are continuously improving in speed, latency, and reliability.

The **5G** network opens doors to new services:

1. **Enhanced Mobile Broadband (eMBB).**
2. **Massive Machine-Type Communications (mMTC).**
3. **Ultra-Reliable Low-Latency Communications (URLLC).**

### Radio Spectrum in Cellular Networks

**The spectrum used by mobile networks is licensed.**

### Test Questions

### Multi-access Edge Computing consists of…

→ …reducing latency by placing application servers as close as possible to clients.

### If a laptop 1 with MAC=c8:cb:9e:fd:a5:bb is sending a packet to another laptop 2 with MAC=50:98:39:ee:f9:76 through a WiFi AP with BSSID=78:29:ed:9f:fb:7e, what are the values of the DA, SA, RA, and TA fields in the IEEE 802.11 header in the segment between laptop 1 and the AP?

→ DA (destination node)=50:98:39:ee:f9:76, SA (source node)=c8:cb:9e:fd:a5:bb, RA (BSSID AP)=78:29:ed:9f:fb:7e, and TA (source node)=c8:cb:9e:fd:a5:bb.

### The deployment of 5G networks requires much more investment than WiFi networks mainly because:

→ Cost of spectrum licenses and deployment of a significant number of antennas to achieve national coverage.

### The process for a wireless node to connect to a WiFi network is as follows:

→ 1) Scanning, 2) Authentication, 3) Association, and 4) Data Transfer.

### What is the main feature that differentiates 5G technology from previous generations?

→ Greater bandwidth.