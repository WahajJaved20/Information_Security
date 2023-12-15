# Chapter 13 ⇒ Cloud and IoT Security

# Cloud Computing

The practice of using a network of remote servers hosted on the internet (to store, manage and process data) rather than a local server on personal computer. 

![Untitled](Chapter%2013%20%E2%87%92%20Cloud%20and%20IoT%20Security%20363daaf007a74e64862fce900a5d21bc/Untitled.png)

## Cloud Service Models

| Software as  a Service (SaaS) | Platform as a Service (PaaS) | Infrastructure as a Service (IaaS) |
| --- | --- | --- |
| Provides service to customers in form of software (specifically application software). | Provides service in form of a platform ON WHICH customer can run their applications. | In IaaS, customer has access to resources of underlying cloud infrastructure. |
| Enables customer to use cloud providers applications running on providers cloud infrastructure | PaaS cloud provides useful software building stuff like programming langs, run-time environments etc. | IaaS cloud users dont manage or control the resources of underlying cloud BUT HAS CONTROL over OS, deployed apps, some control on network components. |
| SaaS foregoes complexity of software installation, maintenance and upgrades. | PaaS is an OS in the cloud (with nothing installed) | IaaS provides Virtual Machines and other OS |
| Ex. GMail, MS365, Salesforce, Cisco, etc. | Useful for organizations who want to develop tailored apps while paying only for the resources as needed | IaaS offers the customer: processing, storage, networks and other fundamental resources for customers to deploy and run arbitrary software (such as OS) |
|  | Ex. MS Azure, AppEngine, Heroku, Apache Stratos etc. | Ex. Amazon EC, MS Azure, Google Compute Engine, etc. |

![Untitled](Chapter%2013%20%E2%87%92%20Cloud%20and%20IoT%20Security%20363daaf007a74e64862fce900a5d21bc/Untitled%201.png)

## Cloud Deployment Models

### 1. Public Cloud

Public Cloud infrastructure is made available to the public or large industry organizations, and is owned ****************************by the people/organization providing you the cloud services.****************************

Here, the cloud provider is responsible for cloud infrastructure and for control of data within cloud.

A public cloud may be owned, managed and operated by a business, academic, or govt. organizations (or a combination).

A major advantage is the cost.

A major concern is the security.

### 2. Private Cloud

Usually implemented within the internal IT organization or environment.

Organization may choose to manage the cloud services in-house or through a third-party cloud service provider.

Cloud servers and storage may be present inside or outside the organization.

Private clouds can deliver IaaS internally to employees through intranet, VPN, as well as storage services to its branch offices.

Ex. of services include database on demand, email on demand and storage on demand

A major advantage is the security, easy resource shareability and rapid deployment to org entitites.

### 3. Community Cloud

Shares characteristics of public & private clouds.

- Has restricted access like private cloud
- The cloud sources are present within a number of independent organizations like public cloud.

The organization that share community clouds usually have similar business interests/requirements and often need to exchange data.

- Ex. Health care industry

Cloud infrastructure may be managed by in-house or a third party and may exist on or off premises.

- In community clouds, the cost is distributed among fewer people rather than few organizations so only so much cost saving is achieved.

### 4. Hybrid Clouds

Composition of two or more clouds (above) that remain unique entities but are bound together by standardized technology that enables data and app **portability.**

With hybrid, we can place less sensitive information on a public cloud and more sensitive information on a private cloud.

Hybrid clouds a re particularly attractive for smaller businesses.

As mentioned above, we can offload applications that have less security concerns which helps in cost savings without moving more sensitive data to a public cloud.

![Untitled](Chapter%2013%20%E2%87%92%20Cloud%20and%20IoT%20Security%20363daaf007a74e64862fce900a5d21bc/Untitled%202.png)

---

![Untitled](Chapter%2013%20%E2%87%92%20Cloud%20and%20IoT%20Security%20363daaf007a74e64862fce900a5d21bc/Untitled%203.png)

---

# Cloud Security Concepts

Security is a ****************************major concern**************************** when augmenting or replacing on-premise systems with cloud services.

During migration of core transaction service like ERP, availability and auditability must be ensured.

Businesses should perform due diligence on security threats from inside and outside premises. 

- cloud users are responsible for application-level security
- cloud vendors are responsible for physical security and some software security
- security for intermediate layers is shared between users and vendors

Cloud providers need to guard against DoS attacks and theft of data.

## NIST Guidelines on Cloud Security and Privacy Issues recommendations.

**Governance:** Extend organizational practices pertaining to the policies, procedures, and standards used for application development and service provisioning in the cloud, as well as the design, implementation, testing, use, and monitoring of deployed or engaged services.

**Compliance**:  Understand the various types of laws and regulations that impose security and privacy obligations on the organization and potentially impact cloud computing initiatives

**Trust**: Ensure that service arrangements have sufficient means to allow visibility into the security and privacy controls and processes employed by the cloud provider, and their performance over time. Establish clear, exclusive ownership rights over data.

**Architecture**: Understand the underlying technologies that the cloud provider uses to provision services, including the implications that the technical controls involved have on the security and privacy of the system, over the full system lifecycle and across all system components.

**Identity and Access Management:** Ensure that adequate safeguards are in place to secure authentication, authorization, and other identity and access management functions, and are suitable for the organization.

**Software Isolation**: Understand virtualization and other logical isolation techniques that the cloud provider employs.

**Data Protection**: Evaluate the suitability of the cloud provider’s data management solutions for the organizational data concerned and the ability to control access to data; to secure data while at rest, in transit, and in use; and to sanitize data.

**Availability**: Understand the contract provisions and procedures for availability, data backup and recovery, and disaster recovery, and ensure that they meet the organization’s continuity and contingency planning requirements.

**Incident Response**: Understand the contract provisions and procedures for incident response and ensure that they meet the requirements of the organization.

## Control Function and Classes

NIST SP 800-146 also lists the overall security controls that are relevant in a cloud computing environment and that must be assigned to the different cloud actors

| Technical | Operational | Management |
| --- | --- | --- |
| - Access control
- Audit and Accountability
- Identification and Authentication
- System and Communication Protection | - Awareness and training 
- Configuration & management
- Contingency planning
- Incident Response
- Maintenance
- Media Protection
- Physical and Environment protection
- Personal security
- System & information integrity | - Certification, accreditation, and security assessment
- Planning
- Risk Assessment 
- System and services acquisition |

---

# Cloud Security Approaches

| RISK | COUNTERMEASURE |
| --- | --- |
| Abuse and nefarious use of cloud computing | - stricter initial registration and validation process
- enhanced credit card fraud monitoring |
| Insecure interfaces and APIs | - understanding dependency chain of APIs
- ensure strong auth controls and access controls are implemented |
| Malicious insiders | - specify HR requirements as a part of legal contract
- require transparency in overall practices
- enforce strict supply chain management 
- determine security breach notification process |
| Shared technology issue | - implement best practices for installation/configuration
- monitor environment for unauthorized changes
- enforce SLA for patching and vulnerability remediation |
| Data Loss leakage | - implement strong API access controls
- encrypt and protect data integrity in transit or at rest
- implement strong key generation, storage, management and destruction |
| Account or service hijacking | - prohibit sharing of account credentials b/w users and services
- leverage strong 2FA techniques |
| Unknown risk profile | - disclosure of applicable logs and data
- partial/full disclosure of infrastructure details
- monitoring and alerting on neccesary information |

## Data Protection in Cloud

| Multi-instance model | Multi-tenant model |
| --- | --- |
| Provides a unique DBMS running on VM instance on each cloud subscriber | Provides pre defined environment which is shared between cloud subscribers or tenants, typically tagging each subscriber with a unique subscriber identifier. |
| This gives user complete control over role definition, user authorization and administrative tasks related to security | Tagging makes it seem like exclusive usage of an instance, BUT it relies on cloud provider to establish and maintain SECURE DBMS environment |

![Untitled](Chapter%2013%20%E2%87%92%20Cloud%20and%20IoT%20Security%20363daaf007a74e64862fce900a5d21bc/Untitled%204.png)

## Cloud Security as a Service (SecaaS)

It is a segment of SaaS offered by the Cloud Service Provider (CSP)

SecaaS is defined as provision for security applications/services via cloud either on:

- cloud-based infrastructures
- customers on-premise system

Services provided by SecaaS:

- IAM
- Data loss prevention
- Web security
- Email security
- Intrusion management
- Security assessments
- Encryption
- Network Security
- etc.