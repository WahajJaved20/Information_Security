# Chapter 1 ⇒ Overview

# // Computer Security

Measures and Control that ensure CIA of information system assets.

# // CIAAA Triad

## 1) Confidentiality

### i) Data Confidentiality ⇒

Private information is not disclosed to unauthorized entity.

### ii) Privacy ⇒

Individuals Control what information is disclosed.

## 2) Integrity

### i) Data Integrity ⇒

Information is changed in authorized manner.

### ii) System Integrity ⇒

System functions in intended manner.

## 3) Availability

System performs timely

## 4) Authenticity

Property of being genuine and being able to be verified and trusted.

## 5) Accountability

Goal that generates the requirement for actions of an entity to be traced uniquely to that entity

# // Challenges of Computer Security

- The requirements seem simple but are hard to implement
- In developing a particular security mechanism or algorithm, one must always consider potential attacks on those security features.
- Having designed various security mechanisms, it is necessary to decide where to use them.
- Security mechanisms typically involve more than a particular algorithm or, protocol. They also require that participants be in possession of some secret information (e.g., an encryption key), which raises questions about the creation, distribution, and protection of that secret  information.
- Computer security is essentially a battle of wits between a perpetrator who tries to find holes, and the designer or administrator who tries to close them.

# // Adversary

Individual/group that conducts detrimental activities.

# // Vulnerability

Weakness in a system

# // Threats

Entities Capable of exploiting vulnerabilities.

# // Attacks

A threat that is carried out.

# // Active Attack

Alter System Resources or affect system operations.

# // Passive Attack

Attempt to Learn information.

# // Countermeasures

means to deal with an attack

# // Risk

A measure of the extent of damage incase of an attack.

![Untitled](Chapter%201%20%E2%87%92%20Overview%203cbf78acf3d0426a9da2ebf0b62a491c/Untitled.png)

# // Unauthorized Disclosure (Threat to Confidentiality)

## 1) Exposure

Sensitive Data Released to unauthorized entity.

## 2) Interception

unauthorized entity gaining access to data travelling between authorized entities.

## 3) Inference

unauthorized entity gaining access to data by reasoning from characteristics or by-products of communications.

## 4) Intrusion

entity gains access to system data by bypassing security controls

# // Deception (Threat to Integrity)

## 1) Masquerade

An unauthorized entity gains access to a system or performs malicious activity while posing as an **********************************authorized entity**********************************

## 2) Falsification

False data to deceive authorized entity

## 3) Repudiation

An entity deceives another entity by falsely denying responsibility for an act.

# // Disruption (Threat to Availability)

## 1) Incapacitation

Interrupt system operation by disabling a system component.

## 2) Corruption

alter system operation by adversely modifying system function

## 3) Obstruction

Interrupt delivery of system services by hindering functions

# // Usurpation (Threat to System Integrity)

## 1) Misappropriation

Entity Assumes unauthorized logical or physical control of system resource

## 2) misuse

Cause a system component to perform a function or service that is detrimental to security.

# // Security Design Principles

## 1) Economy of Mechanism

design of security measures should be simple and small as possible.

## 2) Fail-Safe Defaults

Access Decisions should be made by permissions rather than exclusion. Default situation is lack of access and protection scheme identifies access.

## 3) Complete Mediation

Every access must be checked against the access control mechanism and not rely on cache,

## 4) Open Design

Design of a mechanism should be open and not secret. This allows reviewers.

## 5) Separation of Privilege

Multiple Privilege Attributes are required to achieve access to a restricted resource.

## 6) Least Privilege

Every Process and Every user should operate using least privilege, then if needed, request access.

## 7) Least Common Mechanism’

design should minimize the function shared by different users providing mutual security. This reduces number of unintended communication paths and reduce common resource usage.

## 8) Psychological Acceptability

Mechanisms should not interfere with work of users and at the same time meet the needs of those who authorize access.

## 9) Isolation

Public Access System should be isolated from critical resources to prevent disclosure and tampering.

## 10) Encapsulation

Protection is provided by encapsulating a collection of procedures and data objects in a domain of their own.

## 11) Modularity

Development of security functions as separate modules.

## 12) Layering

use of multiple, overlapping protection approaches addressing the people, technology and operations of the system

## 13) Least Astonishment

A program or UI should respond in a way that is least likely to astonish a user.

# // Computer Security Strategy

## 1) Specification

What is the security scheme supposed to do?

## 2) Implementation

How does it do it?

## 3) Correctness

Does it really work?

# // Security Implementation

In developing a security policy, a security manager needs to consider the following factors:
• The value of the assets being protected
• The vulnerabilities of the system
• Potential threats and the likelihood of attacks

Further, the manager must consider the following trade-offs:

- Ease of use VS Security
- Cost of security VS cost of failure and recovery

## 1) Prevention

Attack isnt successful

## 2) Detection

Detect Security Attacks 

## 3) Response

system Responding to an attack

## 4) Recovery

Reload content if damaged

# // Assurance

Assurance is an attribute of an information system that provides grounds for
having confidence that the system operates such that the system’s security policy is
enforced.

# // Evaluation

Evaluation is the process of examining a computer product or system with respect
to certain criteria. Evaluation involves testing and may also involve formal analytic or
mathematical techniques.

# // Standards

# // National Institute of Standards and Technology

NIST is a U.S. federal agency that deals with measurement science, standards, and technology related to U.S. government use and to the promotion of U.S. private sector innovation.

# // Internet Society

ISOC is a professional membership society with worldwide organizational and individual membership. It provides leadership in addressing issues that confront the future of the Internet,

# // International Telecommunication Union

(ITU) is a United Nations agency in which governments and the private sector coordinate global telecom networks and services.

# // The International Organization for Standardization

(ISO) is a worldwide federation of national standards bodies from more than 140 countries. ISO is a nongovernmental organization that promotes the development of standardization and related activities with a view to facilitating the international exchange of goods and services, and to developing cooperation in the spheres of intellectual, scientific, technological, and economic activity.