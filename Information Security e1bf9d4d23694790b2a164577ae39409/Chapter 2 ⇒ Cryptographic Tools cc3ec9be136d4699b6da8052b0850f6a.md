# Chapter 2 ⇒ Cryptographic Tools

# // Symmetric Encryption

conventional encryption or single-key encryption

## Ingredients

### 1) Plaintext

This is the original message or data that is fed into the algorithm as input.

### 2) Encryption algorithm:

The encryption algorithm performs various substitutions and transformations on the plaintext.

### 3) Secret key:

The secret key is also input to the encryption algorithm. The exact substitutions and transformations performed by the algorithm depend on the key.

### 4) Ciphertext:

This is the scrambled message produced as output. It depends on the plaintext and the secret key. For a given message, two different keys will produce two different ciphertexts.

### 5) Decryption algorithm

This is essentially the encryption algorithm run in reverse. It takes the ciphertext and the secret key and produces the original plaintext.

## Requirements

- Need Strong Encryption algorithm so even if someone knows the algorithm they cant decrypt it.
- Involved Parties should have copies of key stored.

## Attacking SE

### 1) Brute force

try every possible key on a piece of ciphertext until an intelligible translation into plaintext is obtained.

### 2) Cryptanalysis:

This type of attack exploits the characteristics of the algorithm to attempt to deduce a specific plaintext or to deduce the key being used.

![Untitled](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled.png)

# // Block Ciphers

A block cipher processes the plaintext input in fixed-size blocks and produces a block of
ciphertext of equal size for each plaintext block.

![Untitled](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%201.png)

## 1) DATA ENCRYPTION STANDARD

<aside>
💡 Key Size = 56-bit
Plaintext Size = 64-bit
Ciphertext size = 64-bit

</aside>

![Overview of DES](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%202.png)

Overview of DES

![Single Round of DES](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%203.png)

Single Round of DES

![DES Feistel Function](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%204.png)

DES Feistel Function

DES has 8 S-boxes each taking a 6-bit input and producing a 4-bit output.

![Round Key Generator](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%205.png)

Round Key Generator

### Concerns:

- Possible Cryptanalysis
- Key length is small thus possible to brute force

### ALTERNATIVE ⇒ TRIPLE DES

<aside>
💡 Key Size= 112/128 bits
- Computationally Expensive

</aside>

## 2) ADVANCED ENCRYPTION STANDARD

<aside>
💡 Key Size / Rounds = 128 / 10, 192 / 12, 256 / 14
Plaintext Size = 128-bit
Ciphertext size = 128-bit
Roundkey size = 128-bit

</aside>

![Overview of AES](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%206.png)

Overview of AES

![Single Round in AES](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%207.png)

Single Round in AES

![Cipher and Inverse Cipher of AES](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%208.png)

Cipher and Inverse Cipher of AES

### State

The data block being used is called state

### Shift Rows

Byte-wise permutations

![Untitled](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%209.png)

### Mix Columns

Column * Constant = New Column

![Untitled](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%2010.png)

### Add Round Key

Round Key (XOR) State = new state

# // Stream Ciphers

A stream cipher processes the input elements continuously, producing output one element at a time, as it goes along.

![Untitled](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%2011.png)

<aside>
💡 -  Pseudorandom stream is one that is unpredictable without knowledge of the input key and which has an apparently random character. The output of the generator, called a **keystream is XORed one bit at a time with plain text or ciphertext by
-** The primary advantage of a stream cipher is that stream ciphers are almost always faster and use far less code than do block ciphers.

</aside>

# // Authentication using Symmetric Encryption

- only the sender and receiver share a key
- if the message includes an error-detection code and a sequence number, the receiver is assured that no alterations have been made and that sequencing is proper.
- If the message also includes a timestamp, the receiver is assured that the message has not been delayed beyond that normally expected for network transit.

## Block Reordering

If an attacker reorders the blocks of ciphertext, then each block will still decrypt successfully. However, the reordering may alter the meaning of the overall data sequence. Although sequence
numbers may be used at some level (e.g., each IP packet), it is typically not the case that a separate sequence number will be associated with each b-bit block of plaintext. Thus, block reordering is a threat.

# // Message Authentication without Message Encryption

- Broadcasting a message
- Heavy Load on server and cannot decrypt all messages at once
- A computer program can be executed without having to decrypt it every time, which would be wasteful of processor resources.

# // Message Authentication Code

- use of a secret key to generate a small block of data known as MAC and is appended to the message.
- For A to send a message to B
    - A and B have a shared key K.
    - MAC = F(K, Message)
    - Message + MAC transmitted to recipient
    - Receiver does the same after receiving the message.

## Assurances by MAC

- The receiver is assured that the message has not been altered. If an attacker alters the message but does not alter the code, then the receiver’s calculation of the code will differ from the received code.
- The receiver is assured that the message is from the alleged sender. Because no one else knows the secret key, no one else could prepare a message with a proper code.
- If the message includes a sequence number then the receiver can be assured of the proper sequence, because an attacker cannot successfully alter the sequence number.

![Untitled](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%2012.png)

# // One Way Hash Function

- A hash function accepts a variable-size message M as input and produces a fixed-size message  digest H(M) as output
- the message is padded out to an integer multiple of some fixed length (e.g., 1024 bits) and the padding includes the value of the length of the original message in bits.

![Untitled](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%2013.png)

## Message Authentication with Hash Functions

<aside>
💡 ******************************************Symmetric Encryption:******************************************
If it is assumed that only sender and reciever share the encryption key, then authenticity is assured.

![Untitled](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%2014.png)

</aside>

![Untitled](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%2015.png)

<aside>
💡 ******************************************Public-Key Encryption******************************************

message digest can also be encrypted using public-key encryption, It provides a digital signature as well as message authentication, and it does not require the distribution of keys to communicating parties.

</aside>

![Untitled](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%2016.png)

<aside>
💡 ******************************Hash Function
-****************************** No Encryption is needed, incase of hash functions.
- This technique called as “Keyed MAC” assumes that both parties share a common key 
- Append the key before and after message, then hash, same process for decryption.

</aside>

![Untitled](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%2017.png)

# // Hash Function Requirements

The purpose of a hash function is to produce a “fingerprint” of a file, message, or other block of data. To be useful for message authentication, a hash function H must have the following properties:

1. H can be applied to a block of data of any size.
2. H produces a fixed-length output.
3. H(x) is relatively easy to compute for any given x, making both hardware and
software implementations practical.
4. For any given code h, it is computationally infeasible to find x such that H(x) = h.
A hash function with this property is referred to as one-way or preimage
resistant.
5. For any given block x, it is computationally infeasible to find y ≠ x with H(y) = H(x). A hash function with this property is referred to as second preimage resistant. This is sometimes referred to as weak collision resistant.
6. It is computationally infeasible to find any pair (x, y) such that H(x) = H(y).
A hash function with this property is referred to as collision resistant. This is
sometimes referred to as strong collision resistant.

# // Public Key Encryption

- public-key cryptography is asymmetric involving the use of two separate keys
- Ingredients are same as normal encryption except a public and private key.

The essential steps are the following:

1. Each user generates a pair of keys to be used for the encryption and decryption
of messages.
2. Each user places one of the two keys in a public register or other accessible file.
This is the public key. The companion key is kept private. As Figure 2.6a suggests,
each user maintains a collection of public keys obtained from others.
3. If Bob wishes to send a private message to Alice, Bob encrypts the message using
Alice’s public key.
4. When Alice receives the message, she decrypts it using her private key. No other recipient can decrypt the message because only Alice knows Alice’s private key.

![Untitled](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%2018.png)

![Untitled](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%2019.png)

# // Asymmetric Key Encryption

## RSA

RSA is a block cipher in which the plaintext and ciphertext are integers between 0 and n - 1 for some n.

## Diffie–Hellman Key Agreement

## Digital Signature Standard

## Elliptic Curve Cryptography

# // Digital Signatures

- Public Key Encryption for Authentication
- The digital signature does not provide confidentiality.
- “The result of a cryptographic transformation of data that, when properly implemented, provides a mechanism for verifying origin authentication, data integrity and signatory non-repudiation”

![Untitled](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%2020.png)

# // Public Key Certificates

- Avoid Identity Forgery
- Certificate = Public Key + UID of key owner
    - Signed by a trusted third-party
- Certificate Authority (CA)
    - validity of certificate
1. User software (client) creates a pair of keys: one public and one private.
2. Client prepares an unsigned certificate that includes the user ID and user’s
public key.
3. User provides the unsigned certificate to a CA in some secure manner. This might
require a face-to-face meeting, the use of registered e-mail, or happen via a Web
form with e-mail verification.
4. CA creates a signature as follows:
    
    a. use hash function to calculate hash
    
    b. generate digital signature using CAs private key.
    

5. CA attaches the signature to the unsigned certificate to create a signed certificate.

1. CA returns the signed certificate to client.
2. Client may provide the signed certificate to any other user.
3. Any user may verify that the certificate is valid as follows:
a. User calculates the hash code of certificate (not including signature).
    
    b. use digital sign verification with CA public key.
    

![Untitled](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%2021.png)

# // Digital Envelope

- public-key encryption
- protect message and symmetric key without key sharing

![Untitled](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%2022.png)

![Untitled](Chapter%202%20%E2%87%92%20Cryptographic%20Tools%20cc3ec9be136d4699b6da8052b0850f6a/Untitled%2023.png)