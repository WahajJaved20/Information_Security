# Chapter 4 ⇒ Access Control

# // Access Control

Process of granting or denying requests to

- obtain and use information and related processing systems.
- enter specific physical facilities.

# // Access Control Principles

## Basic Requirements

- Limit information system access to authorized users, processes acting on behalf of authorized users, or devices (including other information systems).
- Limit information system access to the types of transactions and functions that authorized users are permitted to execute.

# // Access Control Context

## Authentication

Verify that credentials are valid

## Authorization

Granting permission to access resource

## Audit

independent review of system record and activities in order to test for adequacy of system controls, ensure compliance to policy, detect breaches and recommend changes.

![Untitled](Chapter%204%20%E2%87%92%20Access%20Control%204f6cce1990594a56ac9ad689f2e8f6f7/Untitled.png)

# // Access Control Policies

## Discretionary Access Control

- Access based on identity of requestor and on access rules/authorizations stating what requestors are allowed to do
- It is termed “discretionary” because an entity might have permit to enable other entities to access some resource.

## Mandatory Access Control

- access based on security labels (indicate how sensitive information is) with security clearances(which entities are eligible to access resource)
- It is “mandatory” since an entity having access cannot permit another entitiy.

## Role Based Access Control

- Controls Access based on roles that users have within the system and on rules stating what access is given to those roles.

## Attribute Based Access Control

- Access based on attributes of user, the resource to be accessed and environmental conditions

# // Elements of Access Control

## Subject

Entity capable of accessing objects. They are held accountable for the actions they have initiated and an audit trail may be used to record association of subject with security relevant actions.

### Owner

creator of resource

### Group

membership in group gives certain rights

### World

least privilege users

## Object

Resource to which access is controlled

## Access Right

Way in which subject may access object

- Read
- Write
- Execute
- Create
- Delete
- Search

# // Discretionary Access Control

## Access Matrix

- The most general approach is access matrix
- one dimension will have the subjects (users and groups)
- the other dimension will have objects to be accessed.
- each entry determines access of specific subject to a specific object

|  | File 1 | File 2 | File 3 | File 4 |
| --- | --- | --- | --- | --- |
| User A | Own/Read/Write |  | Own/Read/Write |  |
| User B | Read | Own/Read/Write | Write | R |
| User C | Read/Write | Read |  | Own/Read/Write |
- The Matrix is usually sparse and can be decomposed in two ways.

### Access Control Lists (ACL)

- decomposition by columns yields ACL
- an ACL lists users and their permitted access rights
- may have a default right so users not in the list have some privilege
- not good for determining a users’ right to objects
- good know knowing rights of subjects for an object.

![Untitled](Chapter%204%20%E2%87%92%20Access%20Control%204f6cce1990594a56ac9ad689f2e8f6f7/Untitled%201.png)

### Capability Tickets

- decomposition by rows
- specifies authorized objects and operations for a particular user
- each user has a number of tickets and may be authorized to loan or give them to others.
- greater security problem
- Tickets should be unforgeable hence stored in OS inaccessible to users.
- good to determine a set of rights for a user
- bad for listing all users with rights to an object

![Untitled](Chapter%204%20%E2%87%92%20Access%20Control%204f6cce1990594a56ac9ad689f2e8f6f7/Untitled%202.png)

## Access Control Model

- creates an authorization table with subjects, objects and rights.
- three requirements
    - represent protection state
    - enforce access rights
    - allow subjects to access to alter protection state

![Untitled](Chapter%204%20%E2%87%92%20Access%20Control%204f6cce1990594a56ac9ad689f2e8f6f7/Untitled%203.png)

- to represent protection state, the following matrix is extended with:
    - Processes ⇒ delete, stop, wakeup
    - Devices ⇒ Read/Write, Block/Unblock, Operation
    - Memory Location/ Region ⇒ Read/Write
    - Subjects ⇒ Grant/Delete access rights of others.

![Untitled](Chapter%204%20%E2%87%92%20Access%20Control%204f6cce1990594a56ac9ad689f2e8f6f7/Untitled%204.png)

- From a logical or Functional POV, a separate module is assigned to each object. The model evaluates each request by a subject to access an object.
    - A subject So issues request of type (a) for object X
    - The request causes the system to generate a message of the form (So,a,X) to the controller of X
    - The controller checks access matrix A to determine if a is in A[So,X]. If denied, an access violation should trigger a warning and take action.
- An access matrix controller mediates updates in matrix
- Copy Flag indicates the permission to transfer rights.

![Untitled](Chapter%204%20%E2%87%92%20Access%20Control%204f6cce1990594a56ac9ad689f2e8f6f7/Untitled%205.png)

## Protection Domains

- associate capabilities with protection domains
- set of objects together with their access rights
- each user a protection domain
- any spawned process have same domain as user
- can change rights if needed
- Example ⇒ User / Kernel Mode

# // Traditional Unix File Access control

- each user has an assigned number (UID)
- groups have group id (GID)
- when a file is created, it is designated as owned by a particular user and their primary group
- each file has 12 protection bits
- owner ID, GID and protection bits are part of Inodes.
- Nine of the protection bits are read/write/execute for owners, group, others.
- two bits are set UID and set GID
    - if set on executable file
        - when a user with execute permission executes the file, the OS temporarily allocated the file owner rights to the user. These are called effected UID/GID in addition to the real UID/GID for Access control decisions.
    - If set on directory
        - newly created sub-directories inherit the group of the directory.
- Final bit is a sticky bit.
    - On files, it tells CPU to retain its contents during execution.
    - On directories, it tells that only owner can make changes.
- superuser = unrestricted access

![Untitled](Chapter%204%20%E2%87%92%20Access%20Control%204f6cce1990594a56ac9ad689f2e8f6f7/Untitled%206.png)

# // ACL In UNIX

- Free BSD, Open BSD, Linux, Solans
- Free BSD = Extended ACL
- any number of users and groups can be associated with a file with three protection bits.
- additional bit that tells if a file has extended ACL
    - owner class and other classes have same meaning as minimal ACL
    - the group class entry specifies permissions for owner group. It acts as a mask and tells max permissions a group can have.
    - Additional named groups and users may be associated with a file with 3-protection bits. Any permission outside the mask is disallowed.
- When a process requests access to a file,
    - Closest ACL entry is picked
    - then ACL is scanned in order of user, named user, groups, others
    - then finally access is given or denied.
    
    ![Untitled](Chapter%204%20%E2%87%92%20Access%20Control%204f6cce1990594a56ac9ad689f2e8f6f7/Untitled%207.png)
    

# // Role Based Access Control

- Role = Job Function in an organization
- roles the access rights.
- the relationship of roles to users and roles to resources is many-to-many.
- role assignments can be static/ dynamic depending on the environment.

![Untitled](Chapter%204%20%E2%87%92%20Access%20Control%204f6cce1990594a56ac9ad689f2e8f6f7/Untitled%208.png)

- access matrix can be used on RBAC with users in rows and roles in columns.

![Untitled](Chapter%204%20%E2%87%92%20Access%20Control%204f6cce1990594a56ac9ad689f2e8f6f7/Untitled%209.png)

![Untitled](Chapter%204%20%E2%87%92%20Access%20Control%204f6cce1990594a56ac9ad689f2e8f6f7/Untitled%2010.png)

- leads to effective implementation of least privilege

## Reference Models

### BASE-MODEL (RBAC-0)

→ User ⇒ an individual with access to computer system with UID

→ Role ⇒ Named job function for computer, has description of authority.

→ Permission ⇒ Particular mode of access (access right/privilege/authorization)

→ Session ⇒ a mapping between user and the current subset of roles they are assigned. 

![Untitled](Chapter%204%20%E2%87%92%20Access%20Control%204f6cce1990594a56ac9ad689f2e8f6f7/Untitled%2011.png)

### ROLE-HIERARCHIES (RBAC-1)

- reflect hierarchical structure of roles in organization
- job functions with greater responsibility have greater authority.
- a subordinate job function may have subset of access rights of superior job function
- role hierarchies use concept of inheritance

![Untitled](Chapter%204%20%E2%87%92%20Access%20Control%204f6cce1990594a56ac9ad689f2e8f6f7/Untitled%2012.png)

### CONSTRAINTS (RBAC-2)

- defined relationship among roles and conditions related to roles
- ************************************Mutually exclusive************************************
    - a user can have only one role in a set.
    - static if permanently assigned
    - dynamic if session based assignment
    - any permission can be granted to only one role in a set
    - two users will have non-overlapping permissions
    - the purpose is to increase difficulty of collusion
- **********************Cardinality**********************
    - set the maximum number of users that can be given to a role
    - can set a number of roles for a user per session
    - set a max number of roles that can have some permission
    - risk mitigation technique for powerful roles
- **************************************Pre-requisite Roles**************************************
    - A user can have some role if they already have some assigned role.
    - can be used to structure least privilege

### CONSOLIDATED-MODEL (RBAC-3)

- Simplify system administration
- separation of duties
- good auditing support

![Untitled](Chapter%204%20%E2%87%92%20Access%20Control%204f6cce1990594a56ac9ad689f2e8f6f7/Untitled%2013.png)

# // Attribute Based Access Control

- can define authorization that express conditions on properties of both the resource and the subject.
- key elements ⇒ attributes, policy model, architecture model

## Attributes

- characteristics that define specific aspects of subject, object, environmental conditions.
- indicate class of information by (attribute, name, value)

### Subject Attributes

- active entity that changes system state
- identifier, name, organization, job title, role

### Object Attributes

- passive information system entity containing/ recieving information
- metadata

### Environment Attributes

- operational, technical, situational context for information access.
- date/time, virus/hacker activities
- not necessarily related to subject or object

→ logical access control model

→ controls access to objects by evaluating rules against attributes of entities

→ can enforce DAC, RBAC, MAC

→ enables fine grained access control which allows higher number of discrete inputs into a decision

## Logical Architecture

accessing an object by a subject has these steps

- subject requests access to object. The request is routed to an access control mechanism.
- Access control mechanism is governed by set of rules(2a) that are defined by pre-configured access control policy. Based on rules, ACM assesses the attributes of subject(2b), object(2c) and environmental conditions(2d) for authorization.
- ACM grants access to subject if authorized, else denied

![Untitled](Chapter%204%20%E2%87%92%20Access%20Control%204f6cce1990594a56ac9ad689f2e8f6f7/Untitled%2014.png)

## ABAC Policies

- policy is a set of rules that govern allowable behavior within an organization.
- privileges represent authorized behavior of a subject defined by an authority and embodies in a policy

### YUAN O5 MODEL

- S, O, E are subjects, objects and environment
- SA, OA, EA are predefined attributes for subject, object and environment.
- ATTR(s), ATTR(o) and ATTR(e) are attribute assignment relations.
    - ATTR(s) **⊆** SA1 x SA2 x … x SAk
    - ATTR(o) **⊆** OA1 x OA2 x … x OAm
    - ATTR(e) ****⊆**** EA1 x EA2 x … x EAn
- function notation for value assignment of each attribute
    - Role(s) = “Service Company”
    - ServiceOwner(o) = “XYZ, Inc”
    - CurrentDate(e) = “01-02-2005”
- A policy rule for object access is a boolean function of S,O,E
    - Rule : can_access(s,o,e) ← f(ATTR(s), ATTR(o), ATTR(e))
    - if true, permission is given
- A policy rule base or policy store may consist of a number of policy rules, covering many subjects or objects within a security domain.

### Online Entertainment Store Scenario

| Movie Rating | Users Age |
| --- | --- |
| R | ≥ 17 |
| PG-13  | ≥ 13 |
| G | Everyone |
- In RBAC, every user will have one of the three roles: Adult, Juvenile and Child. Both user-to-role and role-to-permission is manual administrative task.
- In ABAC, a user(u) can view a movie(m) in an environment(e) by following policy:

```jsx
R1: can_access(u,m,e) <- (
							(Age(u) >= 17 /\ Rating(m) ∈ {R,PG-13,G}) V
							(Age(u) >= 13 /\ Rating(m) ∈ {PG-13,G}) V
							(Age(u) < 13 /\ Rating(m) ∈ {G})
```

- reduces manual administrative tasks

Suppose moves are released as newer/older and users are classified as Premium/Regular based on fee paid.

- In RBAC, the roles and permissions will be doubled

![Untitled](Chapter%204%20%E2%87%92%20Access%20Control%204f6cce1990594a56ac9ad689f2e8f6f7/Untitled%2015.png)

- On the other hand, in case of ABAC

```jsx
R2: can_access(u, m, e) <-
(MembershipType(u) = Premium) V
(MembershipType(u) = Regular /\ MovieType(m) = OldRelease)

R3: can_access(u, m, e) <- R1 /\ R2
```

# // Identity, Credential and Access Management

- managing and implementing digital entities.
- created trusted digital identity representations of indivduals and what ICAM does refer to as non-person entities (NPE).
    - NPE includes processes, apps, automated devices.
- Bind those identities to credentials that may serve as proxy for individuals or NPE transactions.
- Use Credentials to provide authorized access to agency resource

## Identity Management

- assign attributes to a digital identity
- connect digital identity to user or NPE
- goal is to establish a trustworthy digital identity independent of context and application
- traditional approach is context specific identity which gives it application level prority.
- concept of enterprise identity is that individuals will have a single digital representation that can be accessed through multiple departments including access control.
- Lifecycle management
    - Mechanism, policy, procedures for identity protection
    - control access to identity data
    - technique for sharing data when needed
    - Revocation of an enterprise identity.

## Credential Management

a credential is an object or data structure that authoritatively binds an identity (and optionally, additional attributes) to a token possessed and controlled by a subscriber.

- Logical Components
    - An authorized individual sponsors an individual or entity for a credential to establish the need for the credential. For example, a department supervisor sponsors a department employee.
    - The sponsored individual enrolls for the credential, a process which typically consists of identity proofing and the capture of biographic and biometric data. This step may also involve incorporating authoritative attribute data, maintained by the identity management component.
    - A credential is produced. Depending on the credential type, production may involve encryption, the use of a digital signature, the production of a smartcard, or other functions.
    - The credential is issued to the individual or NPE.
    - Finally, a credential must be maintained over its life cycle, which might include revocation, reissuance/replacement, reenrollment, expiration, personal identification number (PIN) reset, suspension, or reinstatement.
    
    ## Access Management
    
    The access management component oversees entity access to resources, ensuring proper identity verification for security-sensitive areas. It covers both logical and physical access, internal or external. Access control uses credentials and digital identity.
    
    Three key elements for enterprise-wide access control:
    
    1. **Resource Management:** Defines rules, including credential requirements and conditions for resource access.
    2. **Privilege Management:** Maintains an individual's access profile, linking attributes to a digital identity.
    3. **Policy Management:** Governs allowable actions based on requester and resource attributes, specifying user-object interactions.