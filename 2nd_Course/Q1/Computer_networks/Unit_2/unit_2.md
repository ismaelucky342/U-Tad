# Unit 2: Application Layer

### Functions

It connects the user with the network.

It contains application software, which can be:

- Network Applications: Those that use the network for their own operation, such as DNS or DHCP services.
- Services: Applications used by the user, such as Firefox, email service, Teams, SSH, etc.

### Applications on the TCP/IP Stack

Protocols like HTTP/S, SMTP/S, POP3/S, FTP, TELNET, or SSH use TCP to ensure packet delivery.

On the other hand, DHCP and DNS use UDP.

### Tools for Checking Application Availability

In *Linux*, we can manage the services running on our machine with the **service** command.

With the **NMAP** tool, we can check the services running on a remote machine:

Example → nmap <server> -p<port> -s<transport protocol T or U>

### Web Browsing Service

Apache2 or Nginx provide this service.

1. The client enters a URL. After a DNS resolution, the IP of the WEB server is obtained.
2. A connection is made with the server (GET with HTTP or HTTPS). The server retrieves the content and returns it (200 OK HTTP or HTTPS).
3. The web page is presented to the client.

In Linux, the web information of our apache2 server is located at:

/var/www/html/index.html

### DNS Service

Its function is to translate domain names like [www.u-tad.com](http://www.u-tad.com/) or [mail.telefonica.net](http://mail.telefonica.net/) into the IPs of the servers offering these services.

### BIND9 Package in Linux

To create a DNS server, we can use the *bind9* package in Linux. Once installed, we can configure the server by modifying the configuration files.

- **/etc/bind/named.conf.options:** General configuration file.
- **/etc/bind/named.conf.local:** Zone (domain) definition file.
- **/etc/bind/db.<domain>:** Created from /etc/bind/db.local and is the zone (domain) configuration file.

Once configured, the following commands ensure these configurations take effect:

- **named-checkconf:** Checks for syntax errors in the DNS configuration files.
- **named-checkzone:** Checks the syntax of the zone file, e.g., named-checkzone u-tad.uni /etc/bind/db.u-tad.uni.
- **rndc reload:** Reloads the database.
- **service bind9 restart:** Restarts the DNS server.

### Other Services

For each server application, its corresponding daemon (apache2 or bind9) must be installed to leave an operational service, listening on the corresponding port and waiting for a client (Stand Alone daemon).

### INETD

INETD (internet super server) is a daemon that listens to all requests arriving at the server and, depending on the requested port, starts the corresponding service.

It optimizes resources.

### File Transfer and Remote Connection Services

- FTP: Allows file transfer between systems. Does not encrypt data.
- Telnet: Allows remote connection. Does not encrypt data.
- **SSH:** Allows remote connection and file transfer with encryption.

### Test Questions

### The TTL=3600 seconds primitive in a zone file (DNS) means what?

→ After a query, the client caches it and does not query it again until 3600 seconds have passed.

### The INETD service or daemon is used by Linux systems for:

→ Optimizing the execution of server applications by starting services only when there are client requests.

### When we install a WEB server like Apache on a machine with the IP address (192.168.20.10) and that server only has that service active, what does the command: nmap 192.168.20.10 -p80 -sU show?

→ The following response will appear: PORT STATE SERVICE: 80/udp closed http

→ That the UDP port 80 is closed since the WEB pages service only listens on TCP port 80.

### The following entry "u-tad.uni. IN NS ns.u-tad.uni." in the zone file or resource record file indicates that the URLs u-tad.uni and ns.u-tad.uni return the same IP when queried.

→ FALSE