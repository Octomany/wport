#!/usr/bin/python3

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Title : What port? *wport*                                                  #
# Just a simple script to help pentesting the most common ports.              #
#                                                                             #
# By : Octomany, AKA Maxime Beauchamp                                         #
# Last update : 02-22-2022                                                    #
#                                                                             #
# Special thanks to Carlos Polop for letting me use his descriptions & links  #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import argparse
from colorama import Fore
import re

parser = argparse.ArgumentParser(description='Search for a port number or service name.')

# Set the argument
parser.add_argument('Port# / Service', metavar='PORT', help='Default port number OR service name')

# Get the argument
args = parser.parse_args()
Arg = args.PORT


# Error message if port doesn't exist
ErrorNotFound = Fore.RED + "ERROR: port or service name not found." + Fore.WHITE


Allports=[
        {
        "nb": "21",
        "name": "FTP",
        "desc": "The File Transfer Protocol (FTP) is a standard network protocol used for the transfer of computer files between a client and server on a computer network.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-ftp",
    },
        {
        "nb": "22",
        "name": "SSH / SFTP",
        "desc": "SSH or Secure Shell or Secure Socket Shell, is a network protocol that gives users a secure way to access a computer over an unsecured network.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-ssh",
    },
    {
        "nb": "23",
        "name": "Telnet",
        "desc": "Telnet is a network protocol that gives users a UNsecure way to access a computer over a network.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-telnet",
    },
        {
        "nb": "25",
        "name": "SMTP",
        "desc": "SMTP (Simple Mail Transfer Protocol) is a TCP/IP protocol used in sending and receiving e-mail. However, since it is limited in its ability to queue messages at the receiving end, it is usually used with one of two other protocols, POP3 or IMAP, that let the user save messages in a server mailbox and download them periodically from the server.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-smtp",
    },
        {
        "nb": "465, 587",
        "name": "SMTP (SSL)",
        "desc": "SMTP (Simple Mail Transfer Protocol) is a TCP/IP protocol used in sending and receiving e-mail. However, since it is limited in its ability to queue messages at the receiving end, it is usually used with one of two other protocols, POP3 or IMAP, that let the user save messages in a server mailbox and download them periodically from the server.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-smtp",
    },
        {
        "nb": "43",
        "name": "WHOIS",
        "desc": "WHOIS (pronounced as the phrase \"who is\") is a query and response protocol that is widely used for querying databases that store the registered users or assignees of an Internet resource, such as a domain name, an IP address block or an autonomous system, but is also used for a wider range of other information. ",
        "link": "https://book.hacktricks.xyz/pentesting/43-pentesting-whois",
    },
        {
        "nb": "53",
        "name": "DNS",
        "desc": "The Domain Name Systems (DNS) is the phonebook of the Internet. Humans access information online through domain names, like nytimes.com or espn.com. Web browsers interact through Internet Protocol (IP) addresses. ",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-dns",
    },
        {
        "nb": "69",
        "name": "UDP TFTP/Bittorrent-tracker",
        "desc": "TFTP uses UDP port 69 and requires no authentication—clients read from, and write to servers using the datagram format outlined in RFC 1350. Due to deficiencies within the protocol (namely lack of authentication and no transport security), it is uncommon to find servers on the public Internet. Within large internal networks, however, TFTP is used to serve configuration files and ROM images to VoIP handsets and other devices.",
        "link": "https://book.hacktricks.xyz/pentesting/69-udp-tftp",
    },
        {
        "nb": "79",
        "name": "Finger",
        "desc": "Finger is a program you can use to find information about computer users. It usually lists the login name, the full name, and possibly other details about the user you are fingering. These details may include the office location and phone number (if known), login time, idle time, time mail was last read, and the user's plan and project files.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-finger",
    },
        {
        "nb": "80",
        "name": "HTTP",
        "desc": "The web service is the most common and extensive service and a lot of different types of vulnerabilities exists.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-web",
    },
        {
        "nb": "443",
        "name": "HTTPS",
        "desc": "The web service is the most common and extensive service and a lot of different types of vulnerabilities exists.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-web",
    },
        {
        "nb": "88",
        "name": "Kerberos",
        "desc": "Kerberos is used in Active Directory. In this platform, Kerberos provides information about the privileges of each user, but it is responsability of each service to determine if the user has access to its resources.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-kerberos-88",
    },
        {
        "nb": "110",
        "name": "POP",
        "desc": "Post Office Protocol (POP) is a type of computer networking and Internet standard protocol that extracts and retrieves email from a remote mail server for access by the host machine. POP is an application layer protocol in the OSI model that provides end users the ability to fetch and receive email.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-pop",
    },
        {
        "nb": "995",
        "name": "POP (SSL)",
        "desc": "Post Office Protocol (POP) is a type of computer networking and Internet standard protocol that extracts and retrieves email from a remote mail server for access by the host machine. POP is an application layer protocol in the OSI model that provides end users the ability to fetch and receive email .",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-pop",
    },
        {
        "nb": "111",
        "name": "RPCbind",
        "desc": "Provides information between Unix based systems. Port is often probed, it can be used to fingerprint the Nix OS, and to obtain information about available services. Port used with NFS, NIS, or any rpc-based service.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-rpcbind",
    },
        {
        "nb": "113",
        "name": "Ident",
        "desc": "The Ident Protocol (Identification Protocol, Ident), specified in RFC 1413, is an Internet protocol that helps identify the user of a particular TCP connection. One popular daemon program for providing the ident service is identd. ",
        "link": "https://book.hacktricks.xyz/pentesting/113-pentesting-ident",
    },
        {
        "nb": "123",
        "name": "NTP",
        "desc": "The Network Time Protocol (NTP) is a networking protocol for clock synchronization between computer systems over packet-switched, variable-latency data networks.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-ntp",
    },
        {
        "nb": "135, 445, 593",
        "name": "MSRPC",
        "desc": "Microsoft RPC (Microsoft Remote Procedure Call) is a modified version of DCE/RPC. Additions include partial support for UCS-2 (but not Unicode) strings, implicit handles, and complex calculations in the variable-length string and structure paradigms already present in DCE/RPC. ",
        "link": "https://book.hacktricks.xyz/pentesting/135-pentesting-msrpc",
    },
        {
        "nb": "137, 138",
        "name": "NetBios",
        "desc": "Name service for name registration and resolution",
        "link": "https://book.hacktricks.xyz/pentesting/137-138-139-pentesting-netbios",
    },
        {
        "nb": "139",
        "name": "NetBios",
        "desc": "Session service for connection-oriented communication",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-smb",
    },
        {
        "nb": "445",
        "name": "SMB",
        "desc": "SMB stands for 'Server Message Blocks'. Server Message Block in modern language is also known as Common Internet File System. The system operates as an application-layer network protocol primarily used for offering shared access to files, printers, serial ports, and other sorts of communications between nodes on a network.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-smb",
    },
        {
        "nb": "143",
        "name": "IMAP",
        "desc": "As its name implies, IMAP allows you to access your email messages wherever you are; much of the time, it is accessed via the Internet. Basically, email messages are stored on servers. Whenever you check your inbox, your email client contacts the server to connect you with your messages. ",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-imap",
    },
        {
        "nb": "993",
        "name": "IMAP (SSL)",
        "desc": "As its name implies, IMAP allows you to access your email messages wherever you are; much of the time, it is accessed via the Internet. Basically, email messages are stored on servers. Whenever you check your inbox, your email client contacts the server to connect you with your messages. ",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-imap",
    },
        {
        "nb": "161, 162",
        "name": "SNMP",
        "desc": "SNMP - Simple Network Management Protocol is a protocol used to monitor different devices in the network (like routers, switches, printers, IoTs...).",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-snmp",
    },
        {
        "nb": "10161, 10162",
        "name": "SNMP (TLS)",
        "desc": "SNMP - Simple Network Management Protocol is a protocol used to monitor different devices in the network (like routers, switches, printers, IoTs...).",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-snmp",
    },
        {
        "nb": "194, 6667, 6660-7000",
        "name": "IRC",
        "desc": "IRC was originally a plain text protocol (although later extended), which on request was assigned port 194/TCP by IANA. However, the de facto standard has always been to run IRC on 6667/TCP and nearby port numbers (for example TCP ports 6660–6669, 7000) to avoid having to run the IRCd software with root privileges.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-irc",
    },
        {
        "nb": "264",
        "name": "CheckPoint Firewall-1",
        "desc": "Module sends a query to the port 264/TCP on CheckPoint Firewall-1 firewalls to obtain the firewall name and management station (such as SmartCenter) name via a pre-authentication request",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-264-check-point-firewall-1",
    },
        {
        "nb": "389, 636",
        "name": "LDAP",
        "desc": "LDAP (Lightweight Directory Access Protocol) is a software protocol for enabling anyone to locate organizations, individuals, and other resources such as files and devices in a network, whether on the public Internet or on a corporate intranet. LDAP is a \"lightweight\" (smaller amount of code) version of Directory Access Protocol (DAP).",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-ldap",
    },
        {
        "nb": "3268, 3269",
        "name": "LDAPS",
        "desc": "LDAP (Lightweight Directory Access Protocol) is a software protocol for enabling anyone to locate organizations, individuals, and other resources such as files and devices in a network, whether on the public Internet or on a corporate intranet. LDAP is a \"lightweight\" (smaller amount of code) version of Directory Access Protocol (DAP).",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-ldap",
    },
        {
        "nb": "500",
        "name": "IPsec/IKE VPN",
        "desc": "IPsec is the most commonly used technology for both gateway-to-gateway (LAN-to-LAN) and host to gateway (remote access) enterprise VPN solutions.",
        "link": "https://book.hacktricks.xyz/pentesting/ipsec-ike-vpn-pentesting",
    },
        {
        "nb": "7",
        "name": "Echo",
        "desc": "An echo service is running on this host. The echo service was intended for testing and measurement purposes and may listen on both TCP and UDP protocols. The server sends back any data it receives, with no modification.",
        "link": "https://book.hacktricks.xyz/pentesting/7-tcp-udp-pentesting-echo",
    },
        {
        "nb": "502",
        "name": "Modbus",
        "desc": "Modbus Protocol is a messaging structure developed by Modicon in 1979. It is used to establish master-slave/client-server communication between intelligent devices.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-modbus",
    },
        {
        "nb": "512",
        "name": "Rexec",
        "desc": "It is a service that allows you to execute a command inside a host if you know valid credentials (username and password).",
        "link": "https://book.hacktricks.xyz/pentesting/512-pentesting-rexec",
    },
        {
        "nb": "513",
        "name": "Rlogin",
        "desc": "This service was mostly used in the old days for remote administration but now because of security issues this service has been replaced by the slogin and the ssh.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-rlogin",
    },
        {
        "nb": "514",
        "name": "Rsh",
        "desc": "Rsh use .rhosts files and /etc/hosts.equiv for authentication. These methods relied on IP addresses and DNS (Domain Name System) for authentication. However, spoofing IP addresses is fairly easy, especially if the attacker is on the local network.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-rsh",
    },
        {
        "nb": "515",
        "name": "LPD",
        "desc": "The Line Printer Daemon (LPD) protocol had originally been introduced in Berkeley Unix in the 80s (later specified by RFC1179). The daemon runs on port 515/tcp and can be accessed using the lprcommand. To print, the client sends a control file defining job/username and a data file containing the actual data to be printed. The input type of the data file can be set in the control file by choosing among various file formats. However it is up to the LPD implementation how to actually handle the print data. A popular LPD implementation for Unix-like operating system is LPRng. LPD can be used as a carrier to deploy malicious PostScript or PJL print jobs. ",
        "link": "https://book.hacktricks.xyz/pentesting/515-pentesting-line-printer-daemon-lpd",
    },
        {
        "nb": "548",
        "name": "AFP",
        "desc": "The Apple Filing Protocol (AFP), formerly AppleTalk Filing Protocol, is a proprietary network protocol, and part of the Apple File Service (AFS), that offers file services for macOS and the classic Mac OS. In macOS, AFP is one of several file services supported. AFP currently supports Unicode file names, POSIX and access control list permissions, resource forks, named extended attributes, and advanced file locking. In Mac OS 9 and earlier, AFP was the primary protocol for file services.",
        "link": "https://book.hacktricks.xyz/pentesting/584-pentesting-afp",
    },
        {
        "nb": "554, 8554",
        "name": "RTSP",
        "desc": "The Real Time Streaming Protocol (RTSP) is a network control protocol designed for use in entertainment and communications systems to control streaming media servers. The protocol is used for establishing and controlling media sessions between end points. ",
        "link": "https://book.hacktricks.xyz/pentesting/554-8554-pentesting-rtsp",
    },
        {
        "nb": "623",
        "name": "IPMI",
        "desc": "Baseboard Management Controllers (BMCs) are a type of embedded computer used to provide out-of-band monitoring for desktops and servers. These products are sold under many brand names, including HP iLO, Dell DRAC, Sun ILOM, Fujitsu iRMC, IBM IMM, and Supermicro IPMI. ",
        "link": "https://book.hacktricks.xyz/pentesting/623-udp-ipmi",
    },
        {
        "nb": "631",
        "name": "IPP",
        "desc": "The Internet Printing Protocol (IPP) is defined in RFC2910 and RFC2911. It's an extendable protocol, for example ‘IPP Everywhere’ is a candidate for a standard in mobile and cloud printing and IPP extensions for 3D printing have been released.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-631-internet-printing-protocol-ipp",
    },
        {
        "nb": "873",
        "name": "Rsync",
        "desc": "rsync is a utility for efficiently transferring and synchronizing files between a computer and a storage drive and across networked computers by comparing the modification times and sizes of files. It is commonly found on Unix-like operating systems and is under the GPL-3.0-or-later license.",
        "link": "https://book.hacktricks.xyz/pentesting/873-pentesting-rsync",
    },
        {
        "nb": "1026",
        "name": "Rusersd",
        "desc": "This protocol will provide you the usernames of the host. You may be able to find this services listed by the port-mapper service like this:",
        "link": "https://book.hacktricks.xyz/pentesting/1026-pentesting-rusersd",
    },
        {
        "nb": "1080",
        "name": "Socks",
        "desc": "SOCKS is an Internet protocol that exchanges network packets between a client and server through a proxy server. SOCKS5 optionally provides authentication, so only authorized users may access a server.",
        "link": "https://book.hacktricks.xyz/pentesting/1080-pentesting-socks",
    },
        {
        "nb": "1098, 1099, 1050",
        "name": "Java RMI - RMI-IIOP",
        "desc": "Java Remote Method Invocation, or Java RMI, is an object oriented RPC mechanism that allows an object located in one Java virtual machine to call methods on an object located in another Java virtual machine. ",
        "link": "https://book.hacktricks.xyz/pentesting/1099-pentesting-java-rmi",
    },
        {
        "nb": "1433",
        "name": "MSSQL",
        "desc": "Microsoft SQL Server is a relational database management system developed by Microsoft. As a database server, it is a software product with the primary function of storing and retrieving data as requested by other software applications—which may run either on the same computer or on another computer across a network (including the Internet). Microsoft markets at least a dozen different editions of Microsoft SQL Server, aimed at different audiences and for workloads ranging from small single-machine applications to large Internet-facing applications with many concurrent users.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-mssql-microsoft-sql-server",
    },
        {
        "nb": "1521, 1522-1529",
        "name": "Oracle TNS Listener",
        "desc": "Oracle database (Oracle DB) is a relational database management system (RDBMS) from the Oracle Corporation.",
        "link": "https://book.hacktricks.xyz/pentesting/1521-1522-1529-pentesting-oracle-listener",
    },
        {
        "nb": "1723",
        "name": "PPTP",
        "desc": "Commonly used to provide remote access to mobile devices, Point-to-Point Tunneling Protocol (PPTP) uses TCP port 1723 for key exchange and IP protocol 47 (GRE) to encrypt data between peers.",
        "link": "https://book.hacktricks.xyz/pentesting/1723-pentesting-pptp",
    },
        {
        "nb": "1883",
        "name": "MQTT (Mosquitto)",
        "desc": "MQTT stands for MQ Telemetry Transport. It is a publish/subscribe, extremely simple and lightweight messaging protocol, designed for constrained devices and low-bandwidth, high-latency or unreliable networks. The design principles are to minimise network bandwidth and device resource requirements whilst also attempting to ensure reliability and some degree of assurance of delivery. ",
        "link": "https://book.hacktricks.xyz/pentesting/1883-pentesting-mqtt-mosquitto",
    },
        {
        "nb": "2049",
        "name": "NFS Service",
        "desc": "It is a client/server system that allows users to access files across a network and treat them as if they resided in a local file directory.",
        "link": "https://book.hacktricks.xyz/pentesting/nfs-service-pentesting",
    },
        {
        "nb": "2301, 2381",
        "name": "Compaq/HP Insight Manager",
        "desc": "Compaq Web-based Management Software.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-compaq-hp-insight-manager",
    },
        {
        "nb": "2375,2376",
        "name": "Docker",
        "desc": "The Docker Platform is the industry-leading container platform for continuous, high-velocity innovation, enabling organizations to seamlessly build and share any application — from legacy to what comes next — and securely run them anywhere.",
        "link": "https://book.hacktricks.xyz/pentesting/2375-pentesting-docker",
    },
        {
        "nb": "3128",
        "name": "Squid",
        "desc": "Squid is a caching and forwarding HTTP web proxy. It has a wide variety of uses, including speeding up a web server by caching repeated requests, caching web, DNS and other computer network lookups for a group of people sharing network resources, and aiding security by filtering traffic. Although primarily used for HTTP and FTP, Squid includes limited support for several other protocols including Internet Gopher, SSL, TLS and HTTPS. Squid does not support the SOCKS protocol, unlike Privoxy, with which Squid can be used in order to provide SOCKS support.",
        "link": "https://book.hacktricks.xyz/pentesting/3128-pentesting-squid",
    },
        {
        "nb": "3260",
        "name": "ISCSI",
        "desc": "In computing, iSCSI is an acronym for Internet Small Computer Systems Interface, an Internet Protocol (IP)-based storage networking standard for linking data storage facilities. It provides block-level access to storage devices by carrying SCSI commands over a TCP/IP network. iSCSI is used to facilitate data transfers over intranets and to manage storage over long distances. It can be used to transmit data over local area networks (LANs), wide area networks (WANs), or the Internet and can enable location-independent data storage and retrieval.",
        "link": "https://book.hacktricks.xyz/pentesting/3260-pentesting-iscsi",
    },

        {
        "nb": "3299",
        "name": "SAPRouter",
        "desc": "Saprouter is basically a reverse proxy for SAP systems, typically sitting between the Internet and internal SAP systems. Its main purpose is to allow controlled access from hosts on the Internet to the internal SAP systems, since it allows for a finer grained control of SAP protocols than a typical firewall.",
        "link": "https://book.hacktricks.xyz/pentesting/3299-pentesting-saprouter",
    },
        {
        "nb": "3306",
        "name": "MySQL",
        "desc": "MySQL is a freely available open source Relational Database Management System (RDBMS) that uses Structured Query Language (SQL).",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-mysql",
    },
        {
        "nb": "3389",
        "name": "RDP",
        "desc": "Remote Desktop Protocol (RDP) is a proprietary protocol developed by Microsoft, which provides a user with a graphical interface to connect to another computer over a network connection. The user employs RDP client software for this purpose, while the other computer must run RDP server software.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-rdp",
    },
        {
        "nb": "3632",
        "name": "distcc",
        "desc": "Distcc is designed to speed up compilation by taking advantage of unused processing power on other computers. A machine with distcc installed can send code to be compiled across the network to a computer which has the distccd daemon and a compatible compiler installed",
        "link": "https://book.hacktricks.xyz/pentesting/3632-pentesting-distcc",
    },
        {
        "nb": "3690",
        "name": "Subversion (svn server)",
        "desc": "Subversion is one of many version control options available today. It's often abbreviated as SVN. Subversion is used for maintaining current and historical versions of projects. Subversion is an open source centralized version control system. It's licensed under Apache. It's also referred to as a software version and revisioning control system.",
        "link": "https://book.hacktricks.xyz/pentesting/3690-pentesting-subversion-svn-server",
    },
        {
        "nb": "4369",
        "name": "EPMD",
        "desc": "The erlang port mapper daemon is used to coordinate distributed erlang instances. His job is to keep track of which node name listens on which address. Hence, epmd map symbolic node names to machine addresses.",
        "link": "https://book.hacktricks.xyz/pentesting/4369-pentesting-erlang-port-mapper-daemon-epmd",
    },

        {
        "nb": "5000",
        "name": "Docker Registry",
        "desc": "A Docker registry is a storage and distribution system for named Docker images. The same image might have multiple different versions, identified by their tags. A Docker registry is organized into Docker repositories , where a repository holds all the versions of a specific image. The registry allows Docker users to pull images locally, as well as push new images to the registry (given adequate access permissions when applicable).",
        "link": "https://book.hacktricks.xyz/pentesting/5000-pentesting-docker-registry",
    },

        {
        "nb": "5353",
        "name": "mDNS",
        "desc": "Apple Bonjour and Linux zero-configuration networking implementations (e.g., Avahi) use mDNS to discover network peripherals within the local network.",
        "link": "https://book.hacktricks.xyz/pentesting/5353-udp-multicast-dns-mdns",
    },

        {
        "nb": "5432, 5433",
        "name": "Postgresql",
        "desc": "PostgreSQL is an open source object-relational database system that uses and extends the SQL language.",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-postgresql",
    },

        {
        "nb": "5555",
        "name": "ADB - Android Debug Bridge",
        "desc": "Android Debug Bridge (adb) is a versatile command-line tool that lets you communicate with a device. The adb command facilitates a variety of device actions, such as installing and debugging apps, and it provides access to a Unix shell that you can use to run a variety of commands on a device.",
        "link": "https://book.hacktricks.xyz/pentesting/5555-android-debug-bridge",
    },

        {
        "nb": "5601",
        "name": "Kibana",
        "desc": "Kibana provides search and data visualization capabilities for data indexed in Elasticsearch. The service runs per default on port 5601. Kibana also acts as the user interface for monitoring, managing, and securing an Elastic Stack cluster.",
        "link": "https://book.hacktricks.xyz/pentesting/5601-pentesting-kibana",
    },

        {
        "nb": "5671, 5672",
        "name": "AMQP",
        "desc": "RabbitMQ is a message-queueing software also known as a message broker or queue manager. Simply said; it is software where queues are defined, to which applications connect in order to transfer a message or messages.",
        "link": "https://book.hacktricks.xyz/pentesting/5671-5672-pentesting-amqp",
    },

        {
        "nb": "5800, 5801, 5900, 5901",
        "name": "VNC",
        "desc": "In computing, Virtual Network Computing (VNC) is a graphical desktop-sharing system that uses the Remote Frame Buffer protocol (RFB) to remotely control another computer. It transmits the keyboard and mouse events from one computer to another, relaying the graphical-screen updates back in the other direction, over a network. ",
        "link": "https://book.hacktricks.xyz/pentesting/pentesting-vnc",
    },

        {
        "nb": "5984, 6984",
        "name": "CouchDB",
        "desc": "CouchDB is a document-oriented database and within each document fields are stored as key-value maps. Fields can be either a simple key/value pair, list, or map.",
        "link": "https://book.hacktricks.xyz/pentesting/5984-pentesting-couchdb",
    },

        {
        "nb": "5985, 5986",
        "name": "WinRM or OMI",
        "desc": "Windows Remote Management (WinRM) is a Microsoft protocol that allows remote management of Windows machines over HTTP(S) using SOAP. On the backend it's utilising WMI, so you can think of it as an HTTP based API for WMI. \n\nOMI is an open-source remote configuration management tool developed by Microsoft. ",
        "link": "WinRM : https://book.hacktricks.xyz/pentesting/5985-5986-pentesting-winrm\nPentesting tips : OMI : https://book.hacktricks.xyz/pentesting/5985-5986-pentesting-omi",
    },

        {
        "nb": "6000",
        "name": "X11",
        "desc": "The X Window System (aka X) is a windowing system for bitmap displays, which is common on UNIX-based operating systems. X provides the basic framework for a GUI based environment. X also does not mandate the user interface – individual programs handle this.",
        "link": "https://book.hacktricks.xyz/pentesting/6000-pentesting-x11",
    },

        {
        "nb": "6379",
        "name": "Redis",
        "desc": "Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker. ",
        "link": "https://book.hacktricks.xyz/pentesting/6379-pentesting-redis",
    },


        {
        "nb": "8009",
        "name": "AJP",
        "desc": "AJP is a wire protocol. It an optimized version of the HTTP protocol to allow a standalone web server such as Apache to talk to Tomcat. Historically, Apache has been much faster than Tomcat at serving static content. The idea is to let Apache serve the static content when possible, but proxy the request to Tomcat for Tomcat related content. ",
        "link": "https://book.hacktricks.xyz/pentesting/8009-pentesting-apache-jserv-protocol-ajp",
    },

        {
        "nb": "8086",
        "name": "InfluxDB",
        "desc": "InfluxDB is an open-source time series database (TSDB) developed by the company InfluxData. A time series database (TSDB) is a software system that is optimized for storing and serving time series through associated pairs of time(s) and value(s). ",
        "link": "https://book.hacktricks.xyz/pentesting/8086-pentesting-influxdb",
    },

        {
        "nb": "8089",
        "name": "Splunkd",
        "desc": "The Splunk Universal Forwarder Agent (UF) allows authenticated remote users to send single commands or scripts to the agents through the Splunk API. ",
        "link": "https://book.hacktricks.xyz/linux-unix/privilege-escalation/splunk-lpe-and-persistence",
    },

        {
        "nb": "9000",
        "name": "FastCGI",
        "desc": "PHP fastCGI Process Manager is an alternative PHP FastCGI implementation with some additional features (mostly) useful for heavy-loaded sites.",
        "link": "https://book.hacktricks.xyz/pentesting/9000-pentesting-fastcgi",
    },
        {
        "nb": "9001",
        "name": "HSQLDB",
        "desc": "HSQLDB (HyperSQL Database) is the leading SQL relational database system written in Java. It offers a small, fast multithreaded and transactional database engine with in-memory and disk-based tables and supports embedded and server modes",
        "link": "https://book.hacktricks.xyz/pentesting/9001-pentesting-hsqldb",
    },

        {
        "nb": "9042, 9160",
        "name": "Cassandra",
        "desc": "Apache Cassandra is a highly scalable, high-performance distributed database designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure. It is a type of NoSQL database. In several cases you will find cassandra accepting any credentials (as there aren't any configured) and you will be able to enumerate the database.",
        "link": "https://book.hacktricks.xyz/pentesting/cassandra",
    },
        {
        "nb": "9100",
        "name": "Raw Printing (JetDirect, AppSocket, PDL-datastream)",
        "desc": "Raw printing is what we define as the process of making a connection to port 9100/tcp of a network printer. It is the default method used by CUPS and the Windows printing architecture to communicate with network printers as it is considered as ‘the simplest, fastest, and generally the most reliable network protocol used for printers’. ",
        "link": "https://book.hacktricks.xyz/pentesting/9100-pjl",
    },
        {
        "nb": "9200",
        "name": "Elasticsearch",
        "desc": "Elasticsearch is a distributed, open source search and analytics engine for all types of data, including textual, numerical, geospatial, structured, and unstructured. Elasticsearch is built on Apache Lucene and was first released in 2010 by Elasticsearch N.V. (now known as Elastic). ",
        "link": "https://book.hacktricks.xyz/pentesting/9200-pentesting-elasticsearch",
    },
        {
        "nb": "10000",
        "name": "NDMP",
        "desc": "NDMP, or Network Data Management Protocol, is a protocol meant to transport data between network attached storage (NAS) devices and backup devices. This removes the need for transporting the data through the backup server itself, thus enhancing speed and removing load from the backup server. It was originally invented by NetApp and Intelliguard, acquired by Legato and then EMC Corporation. Currently, the Storage Networking Industry Association (SNIA) oversees the development of the protocol. ",
        "link": "https://book.hacktricks.xyz/pentesting/10000-network-data-management-protocol-ndmp",
    },
        {
        "nb": "11211",
        "name": "Memcached",
        "desc": "Memcached (pronounced variously mem-cash-dee or mem-cashed) is a general-purpose distributed memory-caching system. It is often used to speed up dynamic database-driven websites by caching data and objects in RAM to reduce the number of times an external data source (such as a database or API) must be read.",
        "link": "https://book.hacktricks.xyz/pentesting/11211-memcache",
    },
        {
        "nb": "15672",
        "name": "RabbitMQ Management",
        "desc": "RabbitMQ is a message-queueing software also known as a message broker or queue manager. Simply said; it is software where queues are defined, to which applications connect in order to transfer a message or messages.",
        "link": "https://book.hacktricks.xyz/pentesting/15672-pentesting-rabbitmq-management",
    },
        {
        "nb": "24007, 24008, 24009, 49152+",
        "name": "GlusterFS",
        "desc": "GlusterFS is a distributed, arbitrarily scalable file system that aggregates storage components from several servers into one, uniform file system.",
        "link": "https://book.hacktricks.xyz/pentesting/24007-24008-24009-49152-pentesting-glusterfs",
    },
        {
        "nb": "27017, 27018",
        "name": "MongoDB",
        "desc": "MongoDB is an open source NoSQL database management program. NoSQL is used as an alternative to traditional relational databases. NoSQL databases are quite useful for working with large sets of distributed data. MongoDB is a tool that can manage document-oriented information, store or retrieve information.",
        "link": "https://book.hacktricks.xyz/pentesting/27017-27018-mongodb",
    },
        {
        "nb": "44134",
        "name": "Tiller (Helm)",
        "desc": "Helm is the package manager for Kubernetes. It allows to package YAML files and distribute them in public and private repositories. These packages are called Helm Charts. Tiller is the service running by default in the port 44134 offering the service. ",
        "link": "https://book.hacktricks.xyz/pentesting/44134-pentesting-tiller-helm",
    },
        {
        "nb": "44818",
        "name": "EthernetIP",
        "desc": "EtherNet/IP was developed in the late 1990s by Rockwell Automation as part of Rockwell's industrial Ethernet networking solutions. Rockwell gave EtherNet/IP its moniker and handed it over to ODVA, which now manages the protocol and assures multi-vendor system interoperability by requiring adherence to established standards whenever new products that utilize the protocol are developed today.",
        "link": "https://book.hacktricks.xyz/pentesting/44818-ethernetip",
    },
        {
        "nb": "47808",
        "name": "BACNet",
        "desc": "BACnet is a communication protocol for Building Automation and Control (BAC) networks that leverage the ASHRAE, ANSI, and ISO 16484-5 standard[1] protocol. BACnet was designed to allow communication of building automation and control systems for applications such as heating, ventilating, and air-conditioning control (HVAC), lighting control, access control, and fire detection systems and their associated equipment. The BACnet protocol provides mechanisms for computerized building automation devices to exchange information, regardless of the particular building service they perform. ",
        "link": "https://book.hacktricks.xyz/pentesting/47808-udp-bacnet",
    },
        {
        "nb": "50030, 50060, 50070, 50075, 50090",
        "name": "Hadoop",
        "desc": "Apache Hadoop is an open source framework supporting the distributed storage and processing of large datasets using computer clusters. Storage is handled by the Hadoop Distributed File System (HDFS) and processing is performed by using MapReduce and other applications (e.g., Apache Storm, Flink, and Spark) via YARN.",
        "link": "https://book.hacktricks.xyz/pentesting/50030-50060-50070-50075-50090-pentesting-hadoop",
    },
        {
        "nb": "",
        "name": "",
        "desc": "",
        "link": "",
    },
]

#if 

def PrintResult(rs):
    print("\n" + Fore.YELLOW + rs['name'] + Fore.WHITE)
    print("Port " + rs['nb']+"\n")
    print(rs['desc']+"\n")
    print(Fore.GREEN + "Pentesting tips : " + rs['link'])
    exit()

def PortNB(PN):
    PN = int(PN)
    if PN >= 6660 and PN <= 7000: # IRC
        SelectedPort = next((item for item in Allports if item['nb'] == '194, 6667, 6660-7000'), ErrorNotFound)
    elif PN >= 1522 and PN <= 1529: # Oracle TNS Listener
        SelectedPort = next((item for item in Allports if item['nb'] == '1521, 1522-1529'), ErrorNotFound)
    elif PN >= 49152 and PN <= 49160: # GlusterFS
        SelectedPort = next((item for item in Allports if item['nb'] == '124007, 24008, 24009, 49152+'), ErrorNotFound)
    else:
        PN = str(PN)
        SelectedPort = next((item for item in Allports if re.search(r'\b'+PN+r'\b', item['nb'])), ErrorNotFound)
    
    if SelectedPort != ErrorNotFound:
        PrintResult(SelectedPort)

    else:
        print(SelectedPort)

def ServiceN(SN):
    #ServiceNames = [i for i, x in enumerate(Allports) if re.search(r'\b'+SN+r'\b', x['name'])]
    SelectedPort = next((item for item in Allports if re.search(r'(?i)\b'+SN+r'\b', item['name'])), ErrorNotFound)
        
    if SelectedPort != ErrorNotFound:
        PrintResult(SelectedPort)
        
    else:
        print(SelectedPort)
