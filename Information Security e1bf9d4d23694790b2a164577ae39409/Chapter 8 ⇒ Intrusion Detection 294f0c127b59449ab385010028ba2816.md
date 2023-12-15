# Chapter 8 ⇒ Intrusion Detection

# What is Security Intrusion?

The unauthorized act of bypassing security measures to gain access to a system.

---

# What is Intrusion Detection?

A hardware of software function responsible for gathering and analyzing information within a computer or a network to identify potential security intrusions.

---

# Types of Intruders

## Cyber Criminals

Individuals or members of a organized crime group with financial goals in mind.

Their activities include:

- Identity theft
- Theft of financial credentials
- Corporate espionage
- Data theft
- Data ransoming

Typically young and tech savvy.

## Activists

Individuals or part of group working together motivated by social or political cause.

Hacktivists (skill level is low)

Aim to to promote and publicize their cause through:

- website defacement
- denial of service attacks
- negative publicity

## State Sponsored Organizations

Group of hackers hired by government to conduct espionage or sabotage activities

Also known as APTs (Advanced Persistent Threats) due to covert nature and persistence over extended period of time.

## Others

Classical hackers motivated by technical challenges or by peer-group esteem and reputation.

Hobby hackers.

Responsible for discovering new categories of vulnerabilities.

---

# Intruder Skill Levels

## 1. Apprentice

- Minimal technical skills who just use available tools
- Easy to defend against
- Script-Kiddies (use existing scripts without much changes)

## 2. Journeyman

- Sufficient technical skills to modify, and extend attack toolkits to use newly discovered or purchased vulnerabilities.
- Able to locate new vulnerabilities to exploit

## 3. Master

- High level technical skills capable of discovering new categories of vulnerabilities
- The write new powerful toolkits.
- Defense against them is hardest.

---

# Examples of Intrusion

- Remote root compromise
- Web server defacement
- Guessing/cracking passwords
- Copying databases containing credit card numbers

---

# Intruder Behavior!

### 1. Target Acquisition and information gathering

### 2. Initial Access

### 3. Privilege Escalation

### 4. Information gathering or system exploit

### 5. Maintaining access

### 6. Covering tracks

---

# Intrusion Detection Systems

Consist of three logical components

| Sensors | Analyzers | User Interface (UI) |
| --- | --- | --- |
| Collect Data | Determine if intrusion has occurred | View output or control system behavior |

![Untitled](Chapter%208%20%E2%87%92%20Intrusion%20Detection%20294f0c127b59449ab385010028ba2816/Untitled.png)

## IDS Requirements

- Run continually
- Be fault tolerant
- Resist subversion
- Impose a minimal overhead
- Configured according to system security policies
- Adapt to changes in system
- Scalable to larger number of systems
- Provide graceful degradation
- Allow dynamic reconfiguration

## Analysis Approaches

### Anomaly Detection

Involves collection of data related to behavior of legitimate users to be termed as “normal”.

It then classifies any intruder behavior based on the normal authorized behavior of a typical user.

| Statistical | Analysis of observed behavior using univariate, multivariate, or time-series models. |
| --- | --- |
| Knowledge-based | Approaches use an expert system that classifies observed behavior according to a set of rules that model legitimate behavior. |
| Machine Learning | Automatically determines a suitable classification model from training data. |

### Signal/Heuristic Detection

Uses a set of known malicious data patterns or attack rules that are compared with current behavior.

Can only identify known attacks for which it has patterns or rules.

| Signature Approach | -Matches with a large collection of known patterns to determine class to which malicious intrusion belongs. |
| --- | --- |
| Rule-heuristic Approach | -Rules are used to identify known penetration attacks.

-Rules can be defined that identify suspicious behavior and determine if its within bounds to be malicious. |

---

# Host-Based IDS (HIDS)

“Monitors the characteristics of a single host for malicious activity.”

Primary purpose is to detect intrusions, log suspicious behavior and send alerts.

Can use either anomaly based or heuristic based.

 

******************SENSORS:****************** Fundamental component of intrusion detection are sensors that COLLECT DATA.

Data Sources include: 

- System call traces
- Audit (log file)
- File integrity checksums
- Registry Access

![Untitled](Chapter%208%20%E2%87%92%20Intrusion%20Detection%20294f0c127b59449ab385010028ba2816/Untitled%201.png)

![Untitled](Chapter%208%20%E2%87%92%20Intrusion%20Detection%20294f0c127b59449ab385010028ba2816/Untitled%202.png)

---

# Network-Based IDS (NIDS)

“NIDS monitors traffic at selected points in a network.”

Examines traffic packet by packet in real time (at network, transport, or application level protocols).

Comprises of a number of sensors and one or more server for NIDS management.

Analysis of traffic patterns can be done at the sensor, the management server or a combination of both.

![Untitled](Chapter%208%20%E2%87%92%20Intrusion%20Detection%20294f0c127b59449ab385010028ba2816/Untitled%203.png)

---

# Intrusion Detection Techniques

### Attacks for Signature Detection

- Application layer reconnaissance attacks
- Transport layer reconnaissance attacks
- Network layer reconnaissance attacks
- Unexpected Application Services
- Policy violations

### Attacks for Anomaly Detection

- Denial-of-Service Attacks DoS
- Scanning
- Worms

## Stateful Protocol Analysis

Its a subset of anomaly detection.

Compares network traffic with *predetermined universal vendor supplied* profiles of normal protocol traffic.

It is organization specific (meaning organization provides these profiles).

It requires high resources  (disadvantage)

## Honeypots

Decoy systems purposely designed to lure potential attacker away from resources.

They can also collect information about attacker’s activity.

Encourage attacker to stay on honeypot system long enough for administrators to respond.

These systems contain false or fabricated information.

| Low interaction honeypot | -Less realistic targets
-Does not run a full version of services provided by system.
-Used as part of a bigger IDS. |
| --- | --- |
| High interaction honeypot | -A real system running full OS and services.
-A more realistic target.
-Requires significantly more resources. |

![Untitled](Chapter%208%20%E2%87%92%20Intrusion%20Detection%20294f0c127b59449ab385010028ba2816/Untitled%204.png)

![Untitled](Chapter%208%20%E2%87%92%20Intrusion%20Detection%20294f0c127b59449ab385010028ba2816/Untitled%205.png)