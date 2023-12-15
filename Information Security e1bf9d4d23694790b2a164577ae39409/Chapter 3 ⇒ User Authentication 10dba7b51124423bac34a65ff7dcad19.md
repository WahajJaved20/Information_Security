# Chapter 3 ⇒ User Authentication

# // Digital User Authentication Model

- Applicant applies to ********************************************************Registration Authority (RA)********************************************************  to become ********************subscriber******************** of a ********************************************************************credential service provider (CSP).********************************************************************
- The RA vouches for the ****************claimant**************** to the CSP and the CSP gives the **********************Credential********************** which authoritatively binds an identity to a subscriber.
- The party authenticating is called Claimant **********and the party verifying is called********** verifier**.**
- The verifier passes an assertion about the identity of subscriber to the ************************************Relying Party (RP)************************************.
- The RP can then perform access control.

![Untitled](Chapter%203%20%E2%87%92%20User%20Authentication%2010dba7b51124423bac34a65ff7dcad19/Untitled.png)

# // Means of Authentication

## Something the individual knows:

Examples include a password, a personal identification number (PIN), or answers to a prearranged set of questions.

## Something the individual possesses:

Examples include electronic keycards, smart cards, and physical keys. This type of authenticator is referred to as a token.

## Something the individual is (static biometrics):

Examples include recognition by fingerprint, retina, and face.

## Something the individual does (dynamic biometrics):

Examples include recognition by voice pattern, handwriting characteristics, and typing rhythm.

## Multifactor authentication

refers to the use of more than one of the authentication means in the preceding list

![Untitled](Chapter%203%20%E2%87%92%20User%20Authentication%2010dba7b51124423bac34a65ff7dcad19/Untitled%201.png)

# // Assurance Level

## Level 1:

Little or no confidence in validity. Consumer registering to participate in discussion with ID and password. 

## Level 2:

Some Confidence. Organizations requiring initial identity proof which is also verified.

## Level 3:

High Confidence. Enables Clients to access restricted services of High value, Patent submission with MFA.

## Level 4:

Very High Confidence. enables clients to access restricted services of highest value. Law enforcement DB.

# // Potential Impact

Levels of impact if there is a breach.

## Low:

An authentication error could be expected to have a limited adverse effect on organizational operations, organizational assets, or individuals.

## Moderate:

An authentication error could be expected to have a serious adverse effect.

## High:

An authentication error could be expected to have a severe or catastrophic adverse effect.

# // Areas of Risk

The Mapping b/w potential impact and assurance level that is satisfactory to deal with PI depends on the context

- Low
- Moderate
- High

# // Vulnerability of Passwords

## Offline Dictionary Attack

- Get the shadow file containing hashes, then try to brute force the password against the dictionary of commonly used passwords.
- Countermeasures include controls to prevent unauthorized access to the password file, intrusion detection measures to identify a compromise, and rapid reissuance of passwords should the password file be compromised.

## Specific Account Attack

- Target a specific account and submit password guesses until correct is discovered.
- The standard countermeasure is an account lockout mechanism, which locks out access to the account after a number of failed login attempts.

## Popular Password Attack

- use a popular password against various IDs
- Countermeasures include policies to inhibit the selection by users of common passwords and scanning the IP addresses of authentication requests and client cookies for submission patterns.

## Guessing Against Single User

- attempt to gain knowledge on the account holder and system password policies and use the knowledge to crack the password.
- Common counter is user training

## Workstation Hijacking

- Wait till you find a logged-in workstation unattended.
- Counter is Log-out on inactivity.

## User Mistake

- Writing password on paper, social engineering, pre-configured password.
- Need training to avoid.

## Multi-password use

- if different devices use the same password, one breach can result in severe loss

## E-monitoring

- If passwords are communicated via networks, then eavesdropping is possible.

# // Hashed Passwords

- hash passwords + salt value
- used by UNIX
- the password is combined with fixed length salt value.
- Then hashes of fixed length are generated
- It is stored alongside plaintext salt
- The hashing algorithm is made (slow) to avoid and delay attacks.

<aside>
💡 On user login, the salt is retrieved based on user ID, then encryption routine is done to match. The salt serves three purposes
- prevent password duplication (unique salt)
- increase difficulty of offline dictionary attack
- almost impossible to tell if a person has same pass on different systems.

</aside>

![Untitled](Chapter%203%20%E2%87%92%20User%20Authentication%2010dba7b51124423bac34a65ff7dcad19/Untitled%202.png)

![Untitled](Chapter%203%20%E2%87%92%20User%20Authentication%2010dba7b51124423bac34a65ff7dcad19/Untitled%203.png)

# // Rainbow Table

A large amount of potential passwords and their hashes with each possible salt value.

# // Password File Access Control

- storing hashed passwords in a file which is only accessible to a privileged user.
- AKA **********************SHADOW FILE**********************

<aside>
💡 A reactive password checking strategy is one in which the system periodically
runs its own password cracker to find guessable passwords. The system cancels any passwords that are guessed and notifies the user.

</aside>

# // Tokens

Objects that a user possesses for authentication

# // Memory Cards

can store but not process data

- bank card with magnetic strip
- ATM, PINS

## Drawbacks

### Requires Special Card Reader

increases token usage cost

### Token Loss

temporarily prevent access, if forged, can get unauthorized access

- user dissatisfaction

# // Smart Cards

## Physical Characteristics

embedded microprocessor, looks like a bank card

## User Interface

includes a keypad and display for human computer interaction

## E-interface

### Contact

smart card reader

### Contactless

proximity to the reader

## Authentication Protocol

### Static

User → token → computer

### Dynamic

2FA

## Challenge-Response

computer system generates a challenge, such as random string of numbers. the token generates a response based on the challenge.

# // EID Cards

## ePass

reserved for government, stores a digital representation of card holders identity. e.g: Passport

## eID

general purpose use, stores ID record that authentication service can access with cardholder permission, option to allow.

## eSign

optional, store private key and certificate verifying the key, generates digital signature

![Untitled](Chapter%203%20%E2%87%92%20User%20Authentication%2010dba7b51124423bac34a65ff7dcad19/Untitled%204.png)

# // Biometric Authentication

authenticate a user based on their unique physical characteristics.

- Facial characteristics
- Iris scan
- Fingerprints
- Signature
- Hand Geometry
- Voice
- Retinal Pattern

![Untitled](Chapter%203%20%E2%87%92%20User%20Authentication%2010dba7b51124423bac34a65ff7dcad19/Untitled%205.png)

![Untitled](Chapter%203%20%E2%87%92%20User%20Authentication%2010dba7b51124423bac34a65ff7dcad19/Untitled%206.png)

![Untitled](Chapter%203%20%E2%87%92%20User%20Authentication%2010dba7b51124423bac34a65ff7dcad19/Untitled%207.png)

# // Local Authentication

The simplest form of user authentication is local authentication, in which a user attempts to access a system that is locally present, such as a stand-alone office PC or an ATM machine.

# // Remote User Authentication

- authentication takes place over the internet
- more vulnerable to attacks
- rely on challenge-response for protection.

# // Password Protocol

- User transmits identity to remote host
- Host generates a random number (nonce) (r) and returns it to user
- host specifies two functions h() and f() to be used in response
- The user response is quantity f(r’, h(P’)) where r’  = r and P’ is user password.
- The h() is the hash function.
- So response consists of hash function of password combined with random numebr
- Host stores h() of each registered user password. When response arrives, host compares it with calculated value, if they match, user is authenticated.

![Untitled](Chapter%203%20%E2%87%92%20User%20Authentication%2010dba7b51124423bac34a65ff7dcad19/Untitled%208.png)

# // Token Protocol

- User transmits identity to remote host
- Host generates a random number (nonce) (r) and returns it to user
- host specifies two functions h() and f() to be used in response
- token provides a passcode W′. The token either stores a static passcode or generates a one-time random passcode.
    - For a one-time random pass-code, the token must be synchronized in some fashion with the host.
- user activates the passcode by entering a password P′. This password is shared only between the user and the token and does not involve the remote host.
- For a static passcode, the host stores the hashed value h(W(U)); for a dynamic passcode, the host generates a one-time passcode (synchronized to that generated by the token) and takes its hash.
- When response arrives, host compares it with calculated value, if they match, user is  authenticated.

![Untitled](Chapter%203%20%E2%87%92%20User%20Authentication%2010dba7b51124423bac34a65ff7dcad19/Untitled%209.png)

# // Static Biometric Protocol

- User transmits identity to remote host
- Host generates a random number (nonce) (r) and returns it to user
- host specifies one function E() to be used in response
- On the user side is a client system that controls a biometric device. The system generates a biometric template BT′ from the user’s biometric B′ and returns the ciphertext E(r′, D′, BT′), where D′ identifies this particular biometric device.
- The host decrypts the incoming message to recover the three transmitted parameters and compares these to locally stored values.
- Also, the matching score between BT′ and the stored template must exceed a predefined threshold.

![Untitled](Chapter%203%20%E2%87%92%20User%20Authentication%2010dba7b51124423bac34a65ff7dcad19/Untitled%2010.png)

# // Dynamic Biometric Protocol

- User transmits identity to remote host
- host provides a random sequence as well as a random number as a challenge.
- The sequence challenge is a sequence of numbers, characters, or words.
- The human user at the client end must then vocalize (speaker verification), type (keyboard dynamics verification), or write (handwriting verification) the sequence to generate a biometric signal BS′(x′).
- The client side encrypts the biometric signal and the random number.
- At the host side, the incoming message is decrypted. The incoming random number r′
must be an exact match to the random number that was originally used as a challenge
(r).
- the host generates a comparison based on the incoming biometric signal BS′(x′), the stored template BT(U) for this user and the original signal x. If the comparison value exceeds a predefined threshold, the user is authenticated.

![Untitled](Chapter%203%20%E2%87%92%20User%20Authentication%2010dba7b51124423bac34a65ff7dcad19/Untitled%2011.png)

# // SECURITY ISSUES FOR USER AUTHENTICATION

## Client Attacks

- adversary attempts to acheive user authentication without access to remote host or intervening communications
- Password/Tokens can be exhaustively searched and biometric can be false matched.

## Host Attacks

- directed at the user file at host where passwords, tokens, or biometrics are stored.
- Password can be dictionary/exhaustively searched, token can be stolen, biometric templates can be stolen.

## Eavesdropping

- Attempt to learn the password by observing user or finding a written password
- shoulder surfing, keystroke logging, spoofing token/biometric or stealing physical copy

## Replay

- repeating a previously captured user response

## Trojan Horse

- an application acts as an authentic app to capture passwords/tokens.

## Denial of service

- Disable authentication service by numerous attempts.