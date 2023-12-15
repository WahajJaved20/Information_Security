# Chapter 9 ⇒ Firewall and Intrusion Prevention Systems (IPS)

# The Need for Firewalls

Internet connectivity is no longer optional, it is a major part of organizational transaction with external networks.

These connections are provided by ISPs to external networks which may pose threats. 

Firewalls provide effective means for LAN protection.

Inserted between the premise network and the internet to establish a controlled link via choke points which help insulate internal systems from external networks.

![Untitled](Chapter%209%20%E2%87%92%20Firewall%20and%20Intrusion%20Prevention%20Syst%20acd7e3d031664bba9a8c5ff35cee3633/Untitled.png)

---

# Firewall Characteristics

A critical component in planning and implementation of firewall is specifying a suitable access policy.

Firewall Access Policy used in filtering traffic:

- **IP Address and Protocol Values**: Controls access based on src dest IP, port nums and inbound/outbound traffic.
- **Application Protocol:** Controls access based on authorized application protocol data. This type of filtering is used by application level gateways that relay and monitor exchange of info.
- ******************************User Identity:****************************** Controls access based on user’s identity, typically for inside users who identify themselves as a form of secure authentication (IPSec).
- ************************************Network Activity:************************************ Controls access based on considerations like time and request (ex. only in business hours, rate of requests, or other activity patterns).

| Capabilities | Limitations |
| --- | --- |
| -defines single choke point | -cant protect against attacks that bypass firewall |
| -provides location for monitoring security events | -may not be able to protect against internal threats |
| -convenient platform for several internet functions that are not security related | -improper LAN config allows attackers to access from outside organization |
| -can serve as platform for IPSec | -laptop or portable devices may be infected from outside the corporate network. |

---

# Types of Firewalls

## 1. Packet Filtering Firewall

Applies rules (to forward or discard) to each incoming and outgoing IP packet.

Typically, rules are matched using the info inside TCP or IP headers:

- Src/Dest IP addr
- Src/Dest transport-level addr
- IP Protocol field
- Interface

**Discard *-*** to **prohibit** unless expressly permitted (more conservative, controlled, visible to others)

********************Forward -******************** to **permit** unless expressly prohibited (easier to manage but less secure)

![Untitled](Chapter%209%20%E2%87%92%20Firewall%20and%20Intrusion%20Prevention%20Syst%20acd7e3d031664bba9a8c5ff35cee3633/Untitled%201.png)

![Untitled](Chapter%209%20%E2%87%92%20Firewall%20and%20Intrusion%20Prevention%20Syst%20acd7e3d031664bba9a8c5ff35cee3633/Untitled%202.png)

![Untitled](Chapter%209%20%E2%87%92%20Firewall%20and%20Intrusion%20Prevention%20Syst%20acd7e3d031664bba9a8c5ff35cee3633/Untitled%203.png)

![Untitled](Chapter%209%20%E2%87%92%20Firewall%20and%20Intrusion%20Prevention%20Syst%20acd7e3d031664bba9a8c5ff35cee3633/Untitled%204.png)

### Weaknesses

- Logging functionality is limited in packet filtering firewalls because they dont examine upper layer data (Ex. packet filtering firewall can not block specific application commands)
- PFF dont support advanced user auth. schemes due to lack of upper layer functionality
- PFF cant examine upper layer data so they can NOT prevent application-specific attacks
- PFF are prone to attacks that target known TCP/IP vulnerabilities like *network addr spoofing* :(
- PFF are prone to security breaches caused by improper configuration (which packets to allow based on traffic, source and dest.)

### Attacks which can be made on PFF

### IP Address Spoofing

The intruder transmits packets with a src IP address disguised as some internal host (from within org) in hopes of penetrating system. 

Countermeasure - discard packets with an inside source address if packets arrive on external interface

### Source Routing Attacks

Source stations are something that define the route a packet is supposed to take when crossing the internet, in hopes of bypassing the security measures.

Countermeasure - discard any packet that uses a source station

### Tiny Fragment Attacks

Intruder uses fragmentation to create tiny fragments and pushes all TCP header information into a single fragment in hopes that the filtering rule is able to only check first fragment (header info) and allow all subsequent fragments access.

Countermeasure - first fragment must contain predefined amount of the TCP header.

![Untitled](Chapter%209%20%E2%87%92%20Firewall%20and%20Intrusion%20Prevention%20Syst%20acd7e3d031664bba9a8c5ff35cee3633/Untitled%205.png)

## 2. Stateful Inspection Firewall

Stateful packet inspection tightens the rule for TCP traffic by creating a directory of outbound TCP connections.

There is an entry for each established connection.

The packet filter will not allow incoming traffic to high-numbered ports, only those that fit the profile in directory are allowed!

> Simple packet filtering firewalls must permit inbound traffic on all high-numbered ports for TCP traffic which creates vulnerabilities which can be exploited (so we use Stateful inspection).
> 

SPI reviews all information about the packet, but also records info about the TCP connection (some even keep track of sequence numbers! this is to prevent attacks like session hijacking)

![Untitled](Chapter%209%20%E2%87%92%20Firewall%20and%20Intrusion%20Prevention%20Syst%20acd7e3d031664bba9a8c5ff35cee3633/Untitled%206.png)

![Untitled](Chapter%209%20%E2%87%92%20Firewall%20and%20Intrusion%20Prevention%20Syst%20acd7e3d031664bba9a8c5ff35cee3633/Untitled%207.png)

## 3. Application Level Gateway

AKA application proxy, it acts as a relay of application-level traffic.

1. The user contacts the gateway using TCP/IP application (like Telnet or FTP), the gateway then asks the user for name of the remote host he wants to access.
2. User then responds with valid ID and auth info.
3. The gateway contacts the application on remote host and relays the TCP segments between the 2 endpoints.

![Untitled](Chapter%209%20%E2%87%92%20Firewall%20and%20Intrusion%20Prevention%20Syst%20acd7e3d031664bba9a8c5ff35cee3633/Untitled%208.png)

Application-level gateways are more secure than PFF

Main disadvantage is additional processing overhead required for each connection.

## 4. Circuit Level Gateway

It can be a standalone function or a specialized function performed by application level gateways.

![Untitled](Chapter%209%20%E2%87%92%20Firewall%20and%20Intrusion%20Prevention%20Syst%20acd7e3d031664bba9a8c5ff35cee3633/Untitled%209.png)

As with application level gateways, they do not permit end-to-end TCP connection, instead, it sets up 2 TCP connections: one b/w itself and TCP user on outside host, and one b/w itself and inside host.

Once the 2 connections are established, gateway relays TCP segments from one connection to the other without examining its contents.

### SOCKS Circuit Level Gateway

Designed to provide a framework for client/server apps using TCP or UDP domains to access the security features of a firewall.

![Untitled](Chapter%209%20%E2%87%92%20Firewall%20and%20Intrusion%20Prevention%20Syst%20acd7e3d031664bba9a8c5ff35cee3633/Untitled%2010.png)

Client app contacts SOCKS server which authenticates, sends relay request. This server evaluates either establishing the connection, or denying it.

---

# Intrusion Prevention Systems

Theyre an extension of IDS that have capability to attempt to block or prevent detected malicious activity.

Can use anomaly based detection techniques to determine if behavior is that of a normal user.

Can use signature/heuristic based detection to identify known malicious behavior.

## Host-Based IPS (HIPS)

Can use either anomaly or signature/heuristic based approaches to identify attacks.

Malicious behavior which can be identified by HIPS:

- **Modification of system resources**: rootkits, trojan horses, backdoors used to change system resources like libraries, directories and registry settings.
- **Privilege escalation exploit**: attempts to give normal users admin rights
- **Buffer Overflow exploit:** attackers exploit buffer overflow by overwriting memory of an application
- **Access to email contact list**: Worms are able to spread by mailing a copy of themselves to addresses in contact list.
- **Directory traversal**: A directory traversal vulnerability in web server allows attacker to access files

HIPS can use a sandbox approach (suitable for mobile code and scripting langs)

HIPS quarantines such code in isolated system area then runs and monitors its behavior

HIPS offers the following protections services:

- **System calls:** The kernel controls access to system resources such as memory, I/O devices, and processor. To use these resources, user applications invoke system calls to the kernel.
- **File System access:** The HIPS can ensure that file access system calls are not
malicious and meet established policy
- **System Registry settings:** The registry maintains persistent configuration information about programs and is often maliciously modified to extend the life of an exploit. The HIPS can ensure that the system registry maintains its integrity
- **Host input/output:** I/O communications, whether local or network-based, can propagate exploit code and malware. The HIPS can examine and enforce proper client interaction with the network and its interaction with other devices.

 

Many industry observers claim endpoints are the real point of concerns which can be used by hackers and criminals.

Security vendors work on providing endpoint solutions (anti viruses, anti spyware, anti spam etc.)

**“HIPS is able to provide an amalgamation of security prevention tools and techniques into a single product (HIPS), these tools work closely and thus threat prevention is more comprehensive.”**

## Network-Based IPS (NIPS)

Basically NIDS with the added ability to modify and discard packets and tear down TCP connections.

- Make use of both anomaly and signature/heuristic based detection approaches.
- May provide flow data protection (provided the app payload is a sequence of packets can be reassembled)

Methods used by NIPS to detect malicious packets:

- **Pattern Matching:** scans incoming packets for specific byte sequences (signature) stored in database of known attacks.
- **Stateful Matching:** Scans for attack signatures in context of traffic streams rather than individual packets.
- **Protocol Anomaly:** Looks for deviations from standards set by RFCs.
- **Traffic Anomaly:** Watches for unusual traffic activity like flood of UDP packets.
- **Statistical Anomaly:** Develops baseline of normal traffic throughput and alerts on deviations from the baselines.

## Distributed/Hybrid IPS

This approach gathers data from host + network based sensors, then relays it to a *central analysis system* for analysis. 

This in turn, returns the updated signature and behavior patterns to enable all the coordinated systems to respond and defend against malicious behavior 🛡️

### Digital Immune System

Comprehensive defense against malware/malicious behaviors.

![Untitled](Chapter%209%20%E2%87%92%20Firewall%20and%20Intrusion%20Prevention%20Syst%20acd7e3d031664bba9a8c5ff35cee3633/Untitled%2011.png)

Simple packet filtering firewalls must permit inbound traffic on all high-numbered ports for TCP traffic which creates vulnerabilities which can be exploited (so we use Stateful inspection).