# Chapter 5 ⇒ DB and Data Centre Security

# // Need for DB Security

1. Modern database management systems (DBMS) face a significant security challenge due to their complexity. Despite advancements in security techniques, the intricate nature of DBMS, with numerous features and services, introduces new vulnerabilities and potential misuse.
2. Database interaction relies on the Structured Query Language (SQL), a sophisticated protocol compared to protocols like HTTP. Effective database security hinges on understanding SQL's security vulnerabilities.
3. Organizations often lack dedicated database security personnel, leading to a gap between security requirements and capabilities. Database administrators, focused on availability and performance, may have limited security knowledge. Security personnel may lack understanding of database technology.
4. Enterprise environments often involve a mix of diverse database, enterprise, and operating system platforms, adding complexity for security personnel.

# // DBMS Architecture

![Untitled](Chapter%205%20%E2%87%92%20DB%20and%20Data%20Centre%20Security%2086637089266443a583da7e1b5a81dbb1/Untitled.png)

# // Relational DB

- The basic building block of a relational database is a table of data, consisting of rows and columns, similar to a spreadsheet.
- Users and applications use a relational query language to access the database.
- The query language uses declarative statements rather than the procedural instructions of a programming language.

![Untitled](Chapter%205%20%E2%87%92%20DB%20and%20Data%20Centre%20Security%2086637089266443a583da7e1b5a81dbb1/Untitled%201.png)

## Relation

Building Block / Table

## Tuples

Rows of a table

## Attributes

Columns of a table

## Primary Key

a portion of a row used to uniquely identify a row in a table

## Foreign Key

To create a relationship between two tables, the attributes that define the primary key in one table must appear as attributes in another table, where they are referred to as a foreign key.

## View

A view is a virtual table. In essence, a view is the result of a query that returns selected rows and columns from one or more tables.

![Untitled](Chapter%205%20%E2%87%92%20DB%20and%20Data%20Centre%20Security%2086637089266443a583da7e1b5a81dbb1/Untitled%202.png)

# // SQL Injection

The Attack exploits a security vulnerability occurring in the DB layer of an application.

## Typical SQLi Attack

1. Hacker finds a vulnerability in a custom Web application and injects an SQL command to a database by sending the command to the Web server. The command is injected into traffic that will be accepted by the firewall.
2. The Web server receives the malicious code and sends it to the Web application server.
3. The Web application server receives the malicious code from the Web server and sends it to the database server.
4. The database server executes the malicious code on the database. The database returns data from credit cards table.
5. The Web application server dynamically generates a page with data including credit card details from the database.
6. The Web server sends the credit card details to the hacker.

![Untitled](Chapter%205%20%E2%87%92%20DB%20and%20Data%20Centre%20Security%2086637089266443a583da7e1b5a81dbb1/Untitled%203.png)

## Injection Technique

- premature string termination with comment ‘- -’ and add new command.
- Following is a simple SQL query

```sql
var Shipcity;
ShipCity = Request.form (“ShipCity”);
var sql = “select * from OrdersTable where ShipCity = ‘” +
ShipCity + “‘”;
```

- If the intentional input is given like the ship city, it simply converts the query as:

```sql
SELECT * FROM OrdersTable WHERE ShipCity = ‘Redmond’
```

- However, if the user enters the following:

```sql
Boston’; DROP table OrdersTable--
```

- The resultant query becomes:

```sql
SELECT * FROM OrdersTable WHERE ShipCity =
‘Redmond’; DROP table OrdersTable--
```

## SQLi Attack Avenues

### User Input

- user crafted injection
- HTTP GET/POST requests

### Server Variables

- variables containing HTTP headers, network protocol headers and environment variables.
- webservers use them for logging and statistics
- without sanitization, if they are put into DB, they can be forged.

### Second-Order Injection

### User Input

- a malicious user relies on the incomplete prevention mechanism Data already in system or DB to trigger a SQL injection attack so when an attack occurs, it does not come from user but the system itself

### Cookies

- Cookies are used to store clients’ state information
- webserver builds query based on cookie content so that can be forged.

### Physical User Input

- user input with attack aside from web requests.
- Barcode, RFID tags, paper forms which are scanned.

## SQLi Attack Types

### In-band Attack

- use the same communication channel for injection and result retrieval.

### Tautology

- uses conditionals so it always evaluates to true.
- For the simple query

```php
$query = “SELECT info FROM user WHERE name =
’$_GET[“name”]’ AND pwd = ‘$_GET[“pwd”]’”;
```

- If the attacker submits “ ‘ OR 1=1 --” for name field, the resulting query evaluates to true and becomes

```sql
SELECT info FROM users WHERE name = ‘ ‘ OR 1=1 -- AND pwd = ‘ ‘
```

### End-of-Line Comment

- adding “ - -” after malicious payload.

### Piggy-backed Queries

- attacker adds additional queries aside from intended query, piggybacking over a legitimate query
- requires server to support multi-queries in a single statement.

### Inferential Attack

no transfer of data but the attacker is able to reconstruct particular information by sending particular requests and observing results.

### Logically incorrect Queries

- gather information about type or structure of backend DB
- information gathering step
- information disclosure at error page

### Blind SQLi

- allow attackers to infer data even when the system is secure enough to not return results.
- based on True/False questions and watching responses.

### Out-of-Band Attack

- data retrieval using a different channel (an email with result of query is generated and sent to tester). This can be used when Information Retrieval is limited but outbound connectivity from DB is lax.

## Countermeasures

### Input Validation

- defensive coding practices
- input sanitization
- pattern matching for abnormal input

### Parametrized Query Injection

- pass parameters to query post-cleanup by taking into separate variables.

### SQL-DOM

- set of classes that enable automated data type validation and escaping
- changes query building from string concatenation to a systematic one that uses type-checked API.

### Signature Based Detection

- match specific attack patterns from DB
- may not work against new attacks

### Anomaly Based Detection

- define normal behaviors and differentiate abnormal
- has a learning phase for normal behaviors

### Code analysis

- use test suite to check for vulnerabilities
- generate wide range of attacks and asses vulnerabilities

### Runtime Queries

- check queries at runtime to see if they conform to a model of expected queries.

# // Database Access Control

## Administrative Policies

### Centralized

Small number of privileged users with grant + revoke right

### Ownership-Based

Creator of table with grant + revoke

### Decentralized

Owners may give others right as well.

## SQL Based Access Definition

```sql
GRANT            {privileges | role}
[ON              table]
TO               {user | role | PUBLIC}
[IDENTIFIED BY   password]
[WITH            GRANT OPTION]
```

```sql
REVOKE      {privileges | role}
[ON         table]
FROM        {user | role | PUBLIC}
```

## Cascading Authorizations

- grant options allows access right cascade
- based on time, here are the cascaded privileges

![Untitled](Chapter%205%20%E2%87%92%20DB%20and%20Data%20Centre%20Security%2086637089266443a583da7e1b5a81dbb1/Untitled%204.png)

- When bob revokes Davids’ Access, revokes are cascaded to the times before Chris gave David Access

![Untitled](Chapter%205%20%E2%87%92%20DB%20and%20Data%20Centre%20Security%2086637089266443a583da7e1b5a81dbb1/Untitled%205.png)

## Role Based Access Control

- natural fit for DB
- DAC has three roles
    - Application owner
    - End user
    - Administrator
- DB RBAC has following capabilities
    - Create and delete Role
    - define permit of a role
    - Assign and cancel assignment of users-to-roles.
- SQL Server uses RBAC with following roles

### Fixed Server Roles

- defined at server level and exist independent of DB
- intended to spread admin responsibility without full control.

### Fixed DB Roles

- operate at level of individual DB
- some are designed to assist DB Administrator in administrative delegation.

### User-Defined Roles

- assigned access rights to portions of DB
- users with proper authorization may define new roles
    - Standard (authorization based)
    - Application (code based)

# // Inference

- performing authorized queries to deduce unauthorized information from legit responses
- problem arises when combination of data is more sensitive than individual data
- information transfer path = **********************************Inference Channel**********************************
- Two Techniques
    - Analyze Functional Dependencies between attributes
    - merge views with same constraints

![Untitled](Chapter%205%20%E2%87%92%20DB%20and%20Data%20Centre%20Security%2086637089266443a583da7e1b5a81dbb1/Untitled%206.png)

- For the following Table

![Untitled](Chapter%205%20%E2%87%92%20DB%20and%20Data%20Centre%20Security%2086637089266443a583da7e1b5a81dbb1/Untitled%207.png)

- Two views can be generated as

```sql
CREATE view V1 AS 
SELECT Availability, 
FROM Inventory 
WHERE Department = “hardware” 
```

```sql
CREATE view V2 AS
Cost SELECT Item, Department
FROM Inventory
WHERE Department = “hardware”
```

![Untitled](Chapter%205%20%E2%87%92%20DB%20and%20Data%20Centre%20Security%2086637089266443a583da7e1b5a81dbb1/Untitled%208.png)

- The table can be reconstructed if the attackers takes the two views and merges them based on the inferential knowledge.

![Untitled](Chapter%205%20%E2%87%92%20DB%20and%20Data%20Centre%20Security%2086637089266443a583da7e1b5a81dbb1/Untitled%209.png)

## Countermeasures

### Detection During DB Design

- alter DB Structure
- change access control regime
- remove data dependency, split tables
- more fine-grained Access Control

### Query Time Detection

- Terminate Inference Channel during query execution

# // DB Encryption

## Difficulty

### Key Management

Authorized Users must have access to decryption key. due to wide range of users, key maintenence for partitions becomes complex.

### Inflexibility

Record Searching becomes difficult

## Entities Involved

### Data Owner

Organization that produces data to be made available

### User

Human that gives queries

### Client

Frontend that transforms queries into encrypted versions

### Server

Receives Data from owner and makes it available

![Untitled](Chapter%205%20%E2%87%92%20DB%20and%20Data%20Centre%20Security%2086637089266443a583da7e1b5a81dbb1/Untitled%2010.png)

A user at the client can retrieve a record from the database with the following sequence:

1. The user issues an SQL query for fields from one or more records with a specific value of the primary key.
2. The query processor at the client encrypts the primary key, modifies the SQL query accordingly, and transmits the query to the server.
3. The server processes the query using the encrypted value of the primary key and returns the appropriate record or records.
4. The query processor decrypts the data and returns the results.

## Encryption Techniques

- Each row in the DB is encrypted as a block. Thus each row is termed as a sequence of bits and all attributes are concatenated to form a single block. For each row in DB, there is one row in encrypted DB
    - The row is represented with x as attributes as:
        
        ```sql
        Bi = (x1 || x2 || x3 || ... || xn)
        ```
        
    - The encrypted block is given as:
        
        ```sql
        E(K,Bi) = E(k, (x1 || x2 || x3 || ... || xn))
        ```
        
- Assume Employee ID is in range [1,1000]. Divide into 5 partitions [1,200], [201,400] - - [801,1000], then assign indexes 1,2,3,4,5 respectively.
    - For text attributes, the first letter could be used.
- To obscure the information such as simple ordering of indexes, the order of partition numbering can also be obscured with information limited to DB schema.