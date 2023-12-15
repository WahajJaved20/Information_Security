# Chapter 6 ⇒ Malicious Software

# Malware

A program that is inserted into the system, usually covertly, with the intent of compromising CIA of user’s data, apps, OS or to annoy victim.

### Malware are classified by 2 main categories:

- How it spreads (propagates) to the target
    - Infection of existing stuff on PC by viruses that spread to other systems.
    - Exploit vulnerabilities by worms or drive-by downloads.
    - Social Engineering attacks that can convince/fool users to give up info.
- Actions or Payload it performs once reaching the target
    - Corruption of files or data.
    - Theft of information.
    - Stealthing its presence.

### Also classified by:

1. Those that need a **host program** (Parasitic code like viruses).
2. Those that are **independent (self-containing):** worms, trojans and bots.
3. Malware that **does not replicate:** trojans, and spam e-mails.
4. Malware that **does replicate**: viruses and worms.

---

# Types of Malwares

## Viruses

Piece of software that infects programs (MODIFIES, REPLICATES, & SPREADS)

When attached to an executable software, the virus is able to do anything the program has permissions to do!

Viruses are specific to OS and Hardware

### Virus Components

1. **Infection Mechanism**: Means by which virus spreads/propagates (Infection vector).
2. **Trigger**: Event which executes payload.
3. ******************Payload:****************** What the Virus does (damage or benign but noticeable activity)

### Virus Phases

| Dormant | Propagation | Triggering | Execution |
| --- | --- | --- | --- |
| idle or waiting to be executed. | Places a copy of itself onto other programs. 
Each infected program will contain a clone of virus. | Virus is activated to perform its function. It is caused by an event | Function is performed |

 

## Worms

Programs that actively seek out other machines to infect. Each infected machine acts as a launching pad for attacks on other machines!

- Exploits vulnerabilities in client or server programs.
- Can use network connections to spread.
- Can use shared media to spread (USB, CD, DVD).
- Can use e-mails to spread (attachments or file transfers).

Upon activation, the worm can replicate and propagate again!

Worms carry some sort of payload usually.

### Worm Replication?

| E-mail or messenger facilities | Worms email a copy of itself to other systems thru attachments in messenger services. |
| --- | --- |
| File Sharing | Creates a copy of itself or infects file as a virus on a removable device. |
| Remote Execution! | Executes a copy of itself on another machine. |
| Remote File Access | Can use remote file access or transfer to copy itself from one system to another. |
| Remote Login | Worm logs onto a remote system as user and copies itself from one system to the other. |

### WannaCry (Worm Example)

- Type of ransomware attack that spreads extremely fast infecting hundreds and thousands of systems (both public and private organizational systems) in over 150 countries.
- It spread as a worm by scanning local and remote networks in order to exploit a vulnerability in unpatched windows file sharing service protocol.
- Once infected, it also encrypted files on a system.

## Mobile Code

- Programs that can be shipped to a collection of platforms and executed with identical semantics.
- Transmitted from remote system to a local system and then executed 😈
- Acts as a mechanism for virus, worm or trojan horses to take advantage of vulnerabilities.
- Popular vehicles for mobile code: Java applets, JavaScript, ActiveX etc.
- Most common ways to use mobile code for malicious operations: cross-site scripting, e-mail attachments, downloads from untrusted sites etc.

 

## Mobile Phone Worms

- Communicate thru Bluetooth wireless connections or MMS.
- Smartphones
- Can completely disable the phone, delete data, or force device to send costly messages,

## Drive-by Downloads

- exploits browser or plugin vulnerabilities so that when user opens a webpage, it contains code that automatically downloads or installs malware without user consent or knowledge.
- In most cases, it does not replicate like worms.
- Spreads when user visits a webpage.

## Watering Hole Attack

- variant of drive-by download attack.
- Attacker researches and identifies websites that user like to frequently visit, then scans these websites for vulnerabilities.
- Attacks can be perpetrated so that it affects only a specific user’s belongings when they visit a site.

## Malvertising

- Malicious actors deploy malware by purchasing specific advertisements that a visitor is likely to click on a webpage.
- Malware is embedded in these ads and often dynamically generated.

## Clickjacking

- UI redress attacks.
- Keystrokes and clicks can be hijacked.
- User can believe they are typing into a textbox but are being misled by typing their sensitive info like passwords into a frame controlled by attacker.
- Attacker can place button on top of another using HTML JS code.

## Social Engineering

Tricking users into giving up sensitive information without their realization.

| Spam | Trojan Horse | Mobile Phone trojans |
| --- | --- | --- |
| - unsolicited bulk e-mails | - program or utility containing harmful hidden code | - target is smartphone |
| -significant carrier of malware | - used to accomplish tasks attacker is unable to do directly |  |
| -used for phishing attacks |  |  |

---

# Payloads 🚀

## System Corruption

**Chernobyl Virus**

- infects exe files when they are opened or when trigger date is reached.
- deletes data on system by overwriting first megabyte with 0 in HDD
- results in massive corruption of entire file system.

**Klez**

- Spreads by emailing copy of itself to addresses found on system
- It can stop and disable anti-virus programs running on system
- By the trigger date, it completely wipes HDD.

**Ransomware**

- Encrypts user data and demands payment in order to access a key to retrieve or recover items.
- WannaCry [read it again]

Real-World damage

- causes damage to physical components.
- Chernobyl virus rewrites BIOS code
- StuxNet Worm targets industrial grade system software

Logic Bomb

- Code embedded in malware is set to explode when certain conditions are met.

Attack Agent Bots (Botnet)

- Takes over another computers on the same network and launches or manages attacks from there.
- Botnet - collection of bots capable of acting in coordinated manner
- Uses:
    - DDOS
    - Spamming
    - Packet sniffing
    - Keylogging, etc.
    

![Untitled](Chapter%206%20%E2%87%92%20Malicious%20Software%20dfc7cc8938a640c58904e5b71afe0a68/Untitled.png)

![Untitled](Chapter%206%20%E2%87%92%20Malicious%20Software%20dfc7cc8938a640c58904e5b71afe0a68/Untitled%201.png)

![Untitled](Chapter%206%20%E2%87%92%20Malicious%20Software%20dfc7cc8938a640c58904e5b71afe0a68/Untitled%202.png)

## Information Theft

Keylogger

- Captures keystrokes to monitor sensitive information

Spyware

- Monitors a wide range of activity done on a system without the owner realizing or consenting.

Phishing

- Exploits social engineering by leveraging users trust
- URLs to fake sites, required user authentication, exploiting credentials

Spear-Phishing

- Recipients are carefully researched by attacker and an email is carefully created to target that user, usually containing a lot on information to CONVINCE them its real.

## Stealthing

Backdoor/Trapdoor

- Secret entry point into system unbeknownst to user to gain access and bypass security
- Maintenance hooks used by programmers to debug and test programs
- Difficult to implement OS controls for backdoor in applications.

Rootkits

- Set of hidden programs installed on system to maintain covert access to the system
- Gives admin rights or access to attacker (can add, change programs and files, monitor processes and receive network traffic and get backdoor access on demand)
- Persistent: Activates each time a system boots.
- Memory based: it is stored in memory so harder to detect.
- User mode: intercepts calls to APIs and modifies returned files.
- Kernel mode: can intercept calls to native API in kernel.
- Virtual Machine based: installs a lightweight VM on system.
- External mode: malware is located outside for ex BIOS or system management mode where it can access hardware.

---

# Malware Countermeasures/Approaches

Four main elements of prevention:

1. Policy
2. Awareness
3. Vulnerability Mitigation
4. Threat Mitigation

If prevention fails, technical mechanisms can be used to support the following threat mitigation options:

- Detection
- Identification
- Removal

## Sandbox Analysis

Running potentially malicious code in an emulated controlled environment or VM to better understand the effects of the malware. 

Through this, we are able to detect complex encrypted, polymorphic, or metamorphic malware.

Downside is that we dont know how long to run each interpretation in a sandbox

## Host-Based Behavior blocking software

Integrates with OS of a host PC and monitors program behavior in real time for malicious stuff.

ADVANTAGE: blocks malicious actions before they have a chance to damage system

LIMITATION: because malicious code needs to be run on target machine b4 its behavior can be identified, it can cause harm before it is detected and blocked.

## Perimeter Scanning Approaches

Anti-virus software typically included in e-mails and web proxy running on an organization’s firewall.

May include intrusion prevention measures, blocking flow of suspicious traffic.