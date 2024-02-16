## Closed Answer questions
### Confidentiality
###### Question 1
DES is an algorithm that allows:
- [x] symmetric encryption of data by splitting data in blocks
- [ ] symmetric encryption of data by processing the data flow
- [ ] creation of digital signatures with asymmetric keys
- [ ] creation of digital signature and encryption of data with asymmetric keys
###### Question 2
The key length to defend from brute force attacks has increased because
- [ ] the use of permutations and transpositions in algorithms has increased
- [ ] as algorithms get stronger, they get less complex, and thus more susceptible to attacks
- [x] processor speed and power have increased
- [ ] key length reduces over time
###### Question 3
What of the following properties should a secure AES key
- [x] confidentiality
- [ ] non-repudiation
- [ ] traceability
- [x] randomness
###### Question 4
The advantages of the ECB mode are:
- [x] parallel encryption
- [x] parallel decryption
- [x] random access to blocks (you can decrypt a block independently from the others)
- [x] simple implementation
- [ ] difficult to perform cryptanalysis because identical blocks encrypt differently
- [x] it's not possible to swap blocks
- [x] it's not possible to delete blocks
- [ ] is resistant to known-plaintext attacks
###### Question 5
If a tool uses AES-256-ECB, you can assume that:
- [ ] the tool can accept as a possible input either a private key or a public key
- [ ] the tool will have a negligible padding size
- [ ] the tool will operate on an Initialization Vector of 128 bit
- [x] the tool adopts a symmetric algorithm, with a 256-bit key, and where each block of ciphertext is related to only one block of plaintext
###### Question 6
Which of the following statements are true for the CBC mode?
- [ ] parallel decryption
- [ ] parallel encryption
- [x] protection on order of blocks
- [x] if one cyphertext block is Iost/deleted, the error propagates to the decryption of all the blocks from that point on
- [x] an IV is used to randomize the first cyphertext block
- [ ] it's resistant to known-plaintext attacks
- [ ] random access to blocks (you can decrypt a block independently from the others)
###### Question 7
If you encrypt 50B of plaintext with AES-128-CBC, how long is the ciphertext?
- [ ] 50B
- [x] 64B
- [ ] 808
In the above case, let's assume the ciphertext is a secret message to be sent by Alice to Bob. Indicate the size of data transmitted so that Bob can recover the plaintext
- [ ] 50B
- [ ] 64B
- [x] 80B
	> 64B+16 of the key
###### Question 8
If you encrypt 50B of plaintext with AES-256-CBC, how long is the ciphertext?
- [ ] 50B
- [x] 64B
- [ ] 80B
In the above case, let's assume the ciphertext is a secret message to be sent by Alice to Bob. Indicate the size of data transmitted so that Bob can recover the plaintext
- [ ] 50B
- [ ] 64B
- [ ] 80B
- [x] 96B
###### Question 9
If you encrypt 32B of plaintext with AES-128-CBC, how long is the ciphertext?
- [x] 32B
- [ ] 48B
- [ ] 64B
If you encrypt 32B of plaintext with AES-128-CTR, how long is the ciphertext?
- [x] 32B
- [ ] 48B
- [ ] 64B
###### Question 10
Assume Alice wants to protect her data (1 TB) on disk, but she does not want to increase the space occupied on disk.
Moreover, she would like to perform the encryption very fast and to keep her data protected for 10 years. Which algorithm should she use?
- [ ] AES-128-CBC
- [ ] AES-128-ECB
- [x] AES-256-CTS-CBC
- [ ] 3DES-168-CTS-CBC
- [ ] AES-512-CTS-CBC
###### Question 11
Assume Alice wants to protect her data (1 TB) on disk, she has more space, but she would like to perform the encryption very fast. Which algorithm should she use?
- [ ] AES-128-CBC
- [ ] AES-128-ECB
- [ ] AES-256-CTR
- [ ] 3DES-168-CTR
- [ ] AES-512-CTS-CBC
- [x] Chacha20-256
- [ ] Chacha20-512
- [ ] RC4-128
###### Question 12
Which of the following statements are true for the CTR mode:
- [x] allows parallel encryption of plaintext
- [x] allows parallel decryption of plaintext
- [x] allows random access to groups
- [ ] if a ciphertext block is modified, then (only) that group is erroneously decrypted (but not the successive ones)
- [ ] it is difficult to perform cryptanalysis because identical plaintext groups encrypt differently
- [ ] it's possible to rearrange/swap cyphertext groups
- [ ] if a ciphertext group is deleted, all successive cyphertext groups will be decrypted erroneously
###### Question 13
Which of the following algorithm is based on the fact that it is hard to factor large numbers into two prime numbers?
- [ ] ECC
- [x] RSA
- [x] Diffie-Hellman
- [ ] DES
###### Question 14
Assume Alice wants to communicate to Bob her public key.
She decides to sends the key over an unprotected channel, because the public key is public. Assume Eve can control the communication channel between Alice and Bob. 
What kind of security attacks could do Eve to damage the secure communication between Alice and Bob?
- [ ] replay attack — Eve sends the public key of Alice 10 times
- [ ] sniffing attack — Eve reads the public key of Alice
- [x] man in the middle — Eve modifies the public key of Alice by changing some bits
- [x] man in the middle — Eve replaces the public key of Alice with her own
- [x] filtering — Eve deletes the public key of Alice
###### Question 15
A sender (Alice) wants to send a digitally signed message to a receiver (Bob). Which key is used to create a digital signature?
- [ ] The receiver's private key
- [ ] The sender's public key
- [ ] The sender's private key
- [x] The receiver's public key 
###### Question 16
What is the advantage of RSA over DSA?
- [x] lt can provide digital signature and encryption functionality.
- [ ] lt uses fewer resources and encrypts faster because it uses symmetric keys.
- [ ] lt is a block cipher rather than a stream cipher.
- [ ] lt employs a one-time encryption pad.
###### Question 17
Which of the following best describes a digital signature?
- [ ] A method of transferring a handwritten signature to an electronic document
- [ ] A method to encrypt confidential information
- [ ] A method to provide an electronic signature and encryption
- [x] A method to let the receiver of the message verify the source (data origin) and integrity of a message
###### Question 18
Diffie-Hellman is a:
- [ ] symmetric algorithm
- [x] asymmetric algorithm
- [ ] hash algorithm
- [ ] keyed-digest algorithm
... that is frequently used for:
- [ ] creating digital signatures
- [x] agreeing on a secret key
- [ ] creating an HMAC
###### Question 19
Alice wants to send a secret key K to Bob by using asymmetric cryptography. 
Which operation must Alice do?
- [x] encrypt the key K with the public key of Bob, by using RSA
- [ ] encrypt the key K with the public key of Bob, by using DSA
- [ ] encrypt the key K with her own public key, by using RSA
- [ ] encrypt the key K with the private key of Bob, by using DSA
### Integrity
###### Question 1
Which of the following ones are properties or characteristics of a one-way function?
- [ ] converts an arbitrary length message into a fixed-length value (the digest)
- [x] given the digest value $h(m)$, it should be computationally infeasible to find the corresponding message m
- [x] it should be impossible or infrequent to derive the same digest from two different messages
- [ ] converts a fixed-length message to an arbitrary length value
###### Question 2
Assume Alice sends to Bob a Plain message m along with its digest $md=h(m)$ over an insecure channel. 
Assume Eve is an active attacker controlling the channel between Alice and Bob (i.e. can read, delete, modify, inject data). 
Bob receives both the message and the digest. What would tell Bob that the message has been modified?
- [ ] the public key has been altered
- [ ] the message digest has been altered
- [ ] the message digest computed by Bob is different from the one sent by Alice
- [ ] the message extracted by Bob from the digest — i.e. $mBob=h^{-1}(md)$ — is different from the message received m
- [x] none of the above
###### Question 3
If different messages generate the same hash value, how is this called?
- [ ] secure hashing
- [x] collision
- [ ] MAC generation
- [ ] HMAC generation
###### Question 4
Given a message $m_1$, after 100,000 random attempts Alice finds a message $m_2$ that generates the same hash value when calculated with the algorithm H.
Is H a secure hash algorithm?
- [ ] yes
- [x] no
- [ ] it depends on the length of the output generated by H
- [ ] it depends on the key used in the computation
###### Question 5
HMAC is an algorithm that allows:
- [x] to combine a message with a symmetric key to provide data authentication and integrity
- [ ] to combine a message with an asymmetric private key to provide data authentication and integrity
- [ ] to combine a message with an asymmetric public key to provide data authentication and integrity
- [ ] to combine a message with a symmetric key to provide data authentication, integrity, and non-repudiation
- [ ] to combine a message with an asymmetric private key to provide data authentication, integrity, and non-repudiation
###### Question 6
Which of the following best describes the difference between HMAC and CBC-MAC?
- [ ] HMAC creates a message digest and is used for integrity; CBC-MAC is used to encrypt blocks of data for confidentiality
- [ ] HMAC uses a symmetric key and a hash algorithm; CBC- MAC uses the first encrypted block as a checksum
- [x] HMAC and CBC-MAC provide integrity and data authentication; HMAC uses a hash function, while CBC-MAC uses a block encryption algorithm
- [ ] HMAC encrypts a message with a symmetric key and then puts the results through a hash algorithm; CBC-MAC encrypts the whole message
###### Question 7
Alice wants to protect some messages $m_1, m_2, \dots, m_N$ for data authentication and integrity. 
She constructs for each message a MAC in the following manner: 
```
for (i=1; i<=N i++) 
	mac(i) = HMAC-SHA256( i, m_i) 
```
She sends each message m and the corresponding mac(i) to Bob over an unprotected channel.
Is data authentication and integrity achieved for all messages mi? (justify your answer)
- [ ] yes
- [x] no
> In this way the key is not random.
###### Question 9 
Authenticated Encryption provides:
- [ ] confidentiality and authentication/integrity in one step with two different keys
- [x] confidentiality and authentication/integrity in one step with one key
- [ ] confidentiality and authentication/integrity in two steps with one key
### X.509v3 certificates, CRL, OCSP, digital signatures
###### Question 1
Which of the following best describes a Certification Authority?
- [ ] an organization that issues private keys and the corresponding algorithms
- [ ] an organization that certifies encryption algorithms
- [ ] an organization that certifies encryption keys
- [ ] an organization that issues public-key certificates to entities
###### Assume a CA issues an X.509v3 certificate to Alice. Which of the following values are included in the certificate issued to Alice? Select all that apply.
- [ ] Alice's public key
- [ ] Alice's private key
- [ ] A signature on Alice's X.509v3 certificate, calculated with the CA's private key
- [ ] A signature of the Alice's X.509v3 certificate, calculated with the CA's public key
- [ ] An indication of the owner of the certificate, such as the Alice's name or e-mail address
- [ ] A time period, indicating the lifetime of the certificate
- [ ] An indication of the issuer of the certificate, such as the CA's name
###### Question 4
Why would a Certification Authority revoke a certificate?
- [ ] if the subject's public key has been compromised
- [ ] if the subject's private key has been compromised
- [ ] if the subject sent the certificate over an unprotected channel
- [ ] none of the above
###### Question 5
Which of the following statements about CRL and OCSP are correct?
- [ ] CRL is a list of revoked certificates issued by a CA
- [ ] CRL is a list of revoked certificates issued by a root CA
- [ ] OCSP is a protocol to query a server about the validity of a single specific certificate at a specified time
- [ ] OCSP is a protocol to query a server about the validity of a single specific certificate at the current time
###### Question 6
Alice sends a digitally signed message to Bob and attaches her X.509v3 certificate (and a certificate chain up to a trusted root CA). Which steps must Bob perform to verify the signature on the message? (you can select multiple responses from the ones below)
- [ ] verify the signature on the message by using the certificate of Alice
- [ ] verify that the certificate of Alice is authentic by constructing the chain up to a trusted root and verifying the signatures on each certificate in the chain
- [ ] verify that each certificate in the chain (except the one of the trusted root) has not been revoked
- [ ] do not check the trusted root CA certificate that Alice sent him because he should have it already configured it as trusted
### Open Answer questions
### Describe HMAC indicating its strengths and weaknesses.
HMAC is a technique to generate cryptographic digests of fixed length to provide both confidentiality and integrity of the data.

Given a key $K$ and a message $M$, $HMAC(K,M)$ computes as follows
- If |K|>B then K'=H(K) otherwise K'=K with '0' padded to reach the length of the block B
- K' is XORed with an opad(0x36 repeated B/8 times)
- Add the block obtained at the beginning of the data and apply the hash function
- Compute $K'\oplus opad$, where opad is 0x5C repeated B/8 times, and add it at the beginning of the digest obtained from the previous step
- Compute the digest again to obtain the HMAC

In this way we are able to provide both confidentiality and integrity with a single hash function, that is quicker, computationally speaking, than a keyed digest.
On the other hand, collision on the digest can still occur.
### Describe the authentication and integrity properties of HMAC with respect to the digital signature.
An digital signature is a way to provide non-repudiation of the data, because it is the result of the combination of the data with the private key of the creator.
HMAC provides both integrity, the proof that the data has not been modified, and authentication of the data.
By adding the HMAC to the digital signature it is possible to also authenticate the sender.
### What is integrity? Mention some possible attacks related to it?
Integrity is a property of the the data or a system that provides guarding against improper data modification or destruction, including means for nonrepudiation and authenticity.
Some possible attacks related to it are the Man-in-the-middle type ones.
### Calculate how much data must be saved on disk to decrypt and authenticate a 1kB large file with SHA-1 digest and 1024-bit RSA key.
SHA-1 hash has a digest length of 160 bit so for integrity, so we need to save that.
Suppose that we want to encrypt the data with AES-

### What do the following acronyms mean: DSA, RC-4, RIPEMD? Give a brief description of them
### Difference between stream and block algorithms
A block cypher is a cryptographic system that divides the plaintext into N block of the same length b, adding padding if necessary, and encrypts them with a key individually, following some operational modes and with operational mode and performing various operations like permutations or logical ones.

A stream cypher adopts another approach: instead of dividing the plaintext into blocks, it treats it like a stream of bit, performing the XOR logical operator with its key.
Stream cyphers are also faster, because they allow decryption in constant time and performs simpler operations, but require synchronization between the sender and the receiver, that block cyphers doesn't require.
### Why are stream algorithms faster?
Stream cyphers are faster in comparison to block ones because they perform simpler operations between data and key(a logical XOR), but require constant synchronization between sender and receiver.
### A company must exchange files with another but they can only use a key of 12 characters max; indicate how the system is to be implemented (NOTE: they also wanted to talk about kdf in the solution)
Considering that that one ASCII character is usually 1 byte, if we would use it as a symmetric key to encrypt the data on the channel it wouldn't be enough to provide confidentiality, because any symmetric encryption algorithm with a key under 128 bit is considered not secure, and that key wouldn't be random at all, in all probability.
Fist of all we could use a key derivation function(or KDF) to get a key of the desired length. We could use PBKDF2 to get a 128 bit key necessary for an algorithm like AES-CBC by providing a:
- a cryptographic salt
- the 12 bit key
- the desired length
- the number of iterations
- the pseudorandom function like a HMAC one
After that they could use that key to encrypt the files with the key obtained this what with something like AES-CBC and send them to guarantee its confidentiality with the other party.

If they also want confidentiality and sender authentication, they could also use IPsec in tunnel mode.
### A 28-byte message is encrypted with DES-CBC: how many bytes will be sent in total?
DES has a block size of 64 bit, or $8B$.
IN CBC mode it is necessary to add padding to the last block because $28 \mod 8$ is not 0, adding 4 byte to it.
The length of the encrypted message is 32B if the initialization vector has not been concatenated to the plaintext before encryption, or 40B otherwise.
### If I have to encrypt an 84-byte file in DES-CBC mode, how many bytes will I send over the network?
DES has a block size of 64 bit, or $8B$.
IN CBC mode it is necessary to add padding to the last block because $84 \mod 8$ is not 0, adding 4 byte to it.
The length of the encrypted message is 88B if the initialization vector has not been concatenated to the plaintext before encryption, or 96B otherwise.
### Having a 1500 byte file, if I encrypt it with 3DES-CBC how big will the final file be?
3DES has a block size of 64 bit, or $8B$.
IN CBC mode it is necessary to add padding to the last block because $187 \mod 8$ is not 0, adding 4 byte to it.
The length of the encrypted message is 1504B if the initialization vector has not been concatenated to the plaintext before encryption, or 1512B otherwise, if the same IV is used in all the steps.
### CBC vs CTR: how they work, advantages and disadvantages
Cyber Block Chaining is an operational mode of a block cipher that combines each block with the result of a previous one before encryption(for the first one is used an initialization vector). With this approach, two identical blocks will not produce identical outputs like in ECB mode, but we still need to add padding if necessary and errors propagates to the following blocks.

Counter mode if another operational mode  that uses a nonce and a counter( incremented for each block), which once encrypted are XORed with the actual block to produce the encrypted one.
This allows to add no padding and to have direct access to each block, allowing to parallelize encryption and decryption, that is not possible with CBC.
### Two users wish to exchange a series of ASCII (.TXT) documents over the network. Suggest what operations should be performed on these documents before transmitting them to resist attacks on the (insecure) network. Please note that the documents do not contain confidential information. Note: Do not use complex protocols or data formats. Express the solution by formula (using appropriate terms, such as aes (k, d) rather than enc (k, d))
If confidentiality is not required, only integrity and authentication are.
Suppose that the content of the txt file is $M$, 
Then $HMAC-SHA256-CBC(K,M)$
### User A wants to send a secret and authenticated message to users B and C, all three have a pair of RSA keys each. Describe the format of the data block to send the message with the required security properties.
### Talk about the keyed digest mechanism (what it is, when and how to use it, advantages and disadvantages).
### Talk about the keyed-digest and digital signature, what are their properties, advantages and disadvantages?
### A company wants to digitally sign all its documents and keep both documents and signatures so that they can be verified in the future. What to use? What should it memorize with the signature?
### What security properties does the digital signature offer, how it works, which parts of the signature offer those security properties.
### Why is the SHA-1 algorithm deprecated? Suggest a viable alternative and motivate why this is better than SHA-1.
### Sort the following algorithms from fastest to slowest: SHA, AES_ECB, AES_CBC, RC4
### Given the following encryption algorithms, sort them from slowest to fastest: AES, DES, RC4, 3DES
3DES-DES-RC4-
### Describe elliptic curve cryptography.
### Say the two main advantages of ECC-based algorithms
### Describe the CBC-MAC keyed-digest algorithm.
### One of the first methods to encrypt data?
### On embedded systems, ECDSA is often preferred over RSA: why?
### What is the main advantage of the CTR encryption mode?
### Indicate which integrity attack is possible if data D is protected with a MAC calculated as follows (k is the key and h is the hash function): MAC = h (k || D).
### Advantages and disadvantages of encryption made with enc (enc (p, k1), k2) with k1 and k2 different keys but of equal length
### Describe the ECB cryptographic technique identifying its advantages and disadvantages.
### Which of the following techniques - digital signature, symmetric encryption, keyed-digest - would be preferred to protect the integrity of a 1 Gbps packet stream? Justify the choice
### Which technique is best used to protect data transmitted over the network from replay attacks? Symmetric encryption, asymmetric encryption, keyed-digest, more? To justify 
### Two users must exchange non-confidential ASCII format (txt) text files. How do they ensure they are not changed during transit? Explain which security functions to use and state the formula that produces the transmitted document X against the original document. Use meaningful nouns (e.g. aes (K, D) with respect to enc (K, D).
### Having to encrypt a 12-character password with 2 bytes of salt with AES, is it better to use ECB, CBC or CTR?
### Digital signature with SHA256 digest, RSA-2048 private key on a 10MB file. What is the size of the signature?
### A 10MB document must be signed with SHA-1 digest and RSA key. How big exactly is the document signature?
### What algorithms can be used to exchange secret keys?
### What algorithms can be used to communicate a certain secret key to a counterparty?
### For which application was the CTS invented?
### Explain what the CTS operating mode is, what is the main idea on which its implementation is based and why it is becoming increasingly important
### Why don't you use 2DES and prefer 3DES?
### Calculate how much data must be saved on disk to decrypt and authenticate a 1 kB large file with SHA-1 digest and 1024-bit RSA key.
### What basic algorithms (not complex data structures) can be used to ensure the confidentiality of a file located on a server that you do not trust?
### Explain the term security through obscurity. Explain why some say it's good and others don't.
### Explain authenticated encryption.
Authenticated encryption is a schema used to provide both authentication and encryption in one stem, intead of the usual 2 required.
### Someone sent you a digitally signed file with RSA and SHA-. . . , along with the signer's certificate and his CA's certificate. Describe how to validate the signature, identify the required information and obtain access to it
### Describe DH, his problems and solutions to them
### RSA, RC4, SHA-1,. . . : who is the intruder and why?
Both RSA and RC4 are encryption algorithms, whereas SHA-1 is a hashing algorithm.
### Briefly explain the type of symmetric and asymmetric encryption, indicating the advantages and disadvantages of each type.
###  Alice wants to send Bob a plaintext P protected for confidentiality, authentication, and integrity Alice and Bobs share two symmetric keys K1 and K2 Alice and Bob agreed on two algorithms, A1 (for MAC) and A2 (for symmetric encryption). which operations should Alice perform on P and what data should she transmit to Bob so that he can recover the plaintext and verify its integrity and authenticity? explain the advantages and disadvantages of your solution