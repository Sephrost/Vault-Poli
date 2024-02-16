### Closed answer questions
###### Question 1
Which of the following statements correctly describes reusable passwords as authentication factor?
- [ ] they are the least expensive and most secure
- [ ] they are the most expensive and least secure
- [x] they are the least expensive and least secure
- [ ] they are the most expensive and most secure
###### Question 2
Which of the following factors provides stronger authentication?
- [ ] what a person knows
- [x] what a person is
- [ ] what a person has
###### Question 3
How is a challenge/response protocol used with an authentication-token (device)?
- [ ] this protocol is not used; cryptography is used
- [x] an authentication service generates a challenge, then the authentication token generates a response based on the challenge
- [ ] the token challenges the user for a username and password
- [ ] the token challenges the user's password against a database of stored credentials
###### Question 4
What is a dictionary attack?
- [x] the attacker pre-computes a list of hashes of many "words"; the hashes are then compared with a hashed password (sniffed from the communication channel or leaked from a server)
- [ ] the attacker pre—cornputes several hashes (for several iterations) starting from a word in the Dictionary; the hashes are then compared with a hashed password (sniffed from the communication channel or leaked from a server)
- [ ] the attacker uses a Dictionary of common words (e.g. English language dictionary) to pre-compute a big list of their hashes; the hashes are then compared with a hashed password (sniffed from the communication channel (or leaked from a server)
###### Question 5
A salt is used to protect from dictionary attack. A salt is ..
- [ ] a secret number
- [x] a random number, unpredictable
- [ ] a number that must be known only by the user to generate a more secure password
###### Question 6
The advantages of static passwords are (you can choose more than one option):
- [x] are simple, "free", and require no extra device to carry
- [ ] are immune to sniffing
- [ ] are immune to replay attacks
- [x] require no trust in a third party (in contrast, public key certificates require trust in the CA)
- [ ] are immune to MlTM attacks
###### Question 7
The advantages of OTPs are (you can choose more than one option):
- [ ] are simple, "free", and require no extra device to carry
- [ ] sniffing attacks are not efficient
- [ ] are immune to replay attacks
- [ ] require no trust in a third party (in contrast, public key certificates require trust in the CA)
- [ ] are immune to MITM attacks
###### Question 8
A claimant must authenticate to a Verifier by using a symmetric CRA protocol. The advantages in this case are (you can choose multiple options):
- [ ] the Verifier must not store sensitive keys
- [ ] sniffing attacks are not efficient
- [ ] replay attacks cannot be performed
- [ ] require no trust in a third party (in contrast, public key certificates require trust in the CA) or OOB exchange of public keys
- [ ] is fast
- [ ] is immune to involuntary signing or to relay attacks (does not require Verifier authentication)
###### Question 9
A claimant must authenticate to a Verifier by using an asymmetric CRA protocol. The advantages in this case are (you can choose multiple options):
- [ ] the Verifier must not store sensitive keys
- [ ] sniffing attacks are not efficient
- [ ] replay attacks cannot be performed
- [ ] require no trust in a third party (in contrast, public key certificates require trust in the CA) or OOB exchange of public keys
- [ ] is fast
- [ ] is immune to involuntary signing or relay attacks (does not require Verifier authentication)
## Open Answer questions
### Symmetrical Challenge Authentication Systems, Advantages and Disadvantages.
### Symmetric authentication, what it is, how it works, advantages, weaknesses
### Explain what a dictionary attack is: under what hypothesis it can be conducted and what countermeasures to adopt.

### Compare the symmetric and asymmetrical challenge authentication issues by clearly identifying the advantages and disadvantages of each of them.
### What is a rainbow table?

### Explain the asymmetric challenge method by listing the strengths and weaknesses of the method and the individual components participating.
### Asymmetric challenge authentication
### Explain what an asymmetric challenge authentication system is, indicating what messages are exchanged between the client and the server it authenticates and what advantages and disadvantages it has
### Explain what a time-based OTP system is, indicating what information is transmitted from the client to the authentication server and what functionality is associated with each information transmitted
### Briefly explain the concept of OTP and what security problem it solves. Explain, then, with the help of appropriate formulas, the initialization and verification phases in the S / KEY protocol.